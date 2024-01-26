from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    name: str
    email: str
    hashed_password: str

    class Config:
        from_attributes = True

class CreateUser(UserBase):
    class Config:
        from_attributes = True

class UserLogin(UserBase):
    email: str
    password: str

class Token(UserBase):
    access_token: str
    token_type: str

class DataToken(UserBase):
    id: Optional[str] = None

class UserOutput(BaseModel):
    email: EmailStr
    name: str
    id: int
    class Config:
        from_attributes = True