from app.core.controllers.user_controller import UserController
from app.core.services.user_service import UserService
from app.core.repositories.user_repository import UserRepository

def get_user_controller():
    user_repository = UserRepository()
    user_service = UserService(user_repository=user_repository)
    return UserController(user_service=user_service)
