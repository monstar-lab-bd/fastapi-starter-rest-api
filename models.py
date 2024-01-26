from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String)
