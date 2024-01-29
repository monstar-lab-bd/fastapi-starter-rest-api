from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.core.models.user import User as UserModel

import schemas

class UserRepository:
    def create_user(self, db: Session, user_data: dict):
        db_user = db.query(UserModel).filter(UserModel.email == user_data['email']).first()
        if db_user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"User with {user_data['email']} already exists")
    
        user = UserModel(**user_data)
        db.add(user)
        db.commit()
        db.refresh(user)
        # Create an instance of schemas.UserOutput using the data you have
        return schemas.UserOutput(email=user.email, name=user.name, id=user.id, hashed_password=user.hashed_password)

    def get_user(self, db: Session, user_id: int):
        user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {user_id} not found")
        return schemas.UserOutput(email=user.email, name=user.name, id=user.id, hashed_password=user.hashed_password)
    
    def get_users(self, db: Session):
        users = db.query(UserModel).all()
        return users

    def delete_user(self, db: Session, user_id: int):
        user = db.query(UserModel).filter(UserModel.id == user_id)
        if not user.first():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"User {user_id} not found")
        user.delete(synchronize_session=False)
        db.commit()

    def update_user(self, db: Session, user_id: int, user_data: dict):
        db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if not db_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {user_id} not found")

        db_user.name = user_data['name']
        db_user.email = user_data['email']

        db.commit()
        db.refresh(db_user)

        return db_user