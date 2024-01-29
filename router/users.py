from typing import List
from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from starlette import status
import app.core.models.user as user
import schemas
import utils
from database import get_db
from app.core.dependencies import get_user_controller

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

user_controller = get_user_controller()

@router.get('/', response_model=List[schemas.UserOutput])
def get_users(db: Session = Depends(get_db)):
    return user_controller.get_users(db=db)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.UserOutput)
def create_user(user: schemas.CreateUser, db: Session = Depends(get_db)):
    return user_controller.create_user(user=user, db=db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.UserOutput)
def get_user(id: int, db: Session = Depends(get_db)):
    return user_controller.get_user(user_id=id, db=db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, db: Session = Depends(get_db)):
    return user_controller.delete_user(user_id=id, db=db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=schemas.UpdateUser)
def update_user(id: int, user: schemas.UpdateUser, db: Session = Depends(get_db)):
    return user_controller.update_user(user_id=id, user=user, db=db)
