from fastapi import FastAPI, Depends
import app.core.models.user as user
from router import users
from database import Base, engine, get_db

from app.core.dependencies import get_user_controller

app = FastAPI()

user.Base.metadata.create_all(bind=engine)

user_controller = get_user_controller()


app.include_router(users.router,
                    tags=["API"],
                    dependencies=[Depends(get_db),
                    Depends(get_user_controller)])

