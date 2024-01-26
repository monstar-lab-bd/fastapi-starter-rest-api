from typing import List
from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from starlette import status
import models
import schemas
import utils
from database import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get('/', response_model=List[schemas.CreateUser])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=List[schemas.UserOutput])
def create_user(user: schemas.CreateUser, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"User with {user.email} already exists")
    hashed_value = utils.hash_pass(user.hashed_password)
    user.hashed_password = hashed_value
    user = models.User(**user.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return [user]

@router.get('/{id}', response_model=schemas.CreateUser, status_code=status.HTTP_200_OK)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"User {id} not found")
    return user

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"User {id} not found")
    user.delete(synchronize_session=False)
    db.commit()

from fastapi import HTTPException

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=schemas.CreateUser)
def update_user(id: int, user: schemas.UserBase, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == id).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {id} not found")

    # Update user attributes based on the data provided in the request
    for key, value in user.model_dump().items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)

    return db_user
