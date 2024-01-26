from fastapi import FastAPI
import models
from router import users
from database import Base, engine  # Update this import based on your actual file structure

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
app.include_router(users.router)
