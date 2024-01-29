from sqlalchemy.orm import Session
from app.core.repositories.user_repository import UserRepository
import schemas

class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def create_user(self, db: Session, user_data: dict):
        return self.user_repository.create_user(db=db, user_data=user_data)
    
    def get_user(self, db: Session, user_id: int):
        return self.user_repository.get_user(db=db, user_id=user_id)
    
    def get_users(self, db: Session):
        return self.user_repository.get_users(db=db)
    
    def delete_user(self, db: Session, user_id: int):
        return self.user_repository.delete_user(db, user_id)
    
    def update_user(self, db: Session, user_id: int, user_data: dict):
        return self.user_repository.update_user(db, user_id, user_data)