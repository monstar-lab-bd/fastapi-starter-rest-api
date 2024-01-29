from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from starlette import status
import utils
import schemas
from database import get_db
from app.core.services.user_service import UserService

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

class UserController:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def create_user(self, user: schemas.CreateUser, db: Session = Depends(get_db)):
        return self.user_service.create_user(db=db, user_data=user.dict())
    
    def get_user(self, user_id: int, db: Session = Depends(get_db)):
        return self.user_service.get_user(db=db, user_id=user_id)
    
    def get_users(self, db: Session = Depends(get_db)):
        return self.user_service.get_users(db=db)
    
    def delete_user(self, user_id: int, db: Session = Depends(get_db)):
        return self.user_service.delete_user(db=db, user_id=user_id)
    
    def update_user(self, user_id: int, user: schemas.UpdateUser, db: Session = Depends(get_db)):
        return self.user_service.update_user(db, user_id=user_id, user_data=user.dict())
        