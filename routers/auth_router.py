from fastapi import APIRouter
from controllers.auth_controller import signup_controller, login_controller
from models.userModel import UserSignup, UserLogin

router = APIRouter()

@router.post("/signup")
async def signup(user: UserSignup):
    return signup_controller(user)

@router.post("/login")
async def login(user: UserLogin):
    return login_controller(user)