from fastapi import APIRouter, HTTPException
from controllers.user_controllers import (
    create_user_controller,
    read_user_controller,
    read_users_controller,
    update_user_controller,
    delete_user_controller,
    delete_user_id_controller,
)
from models.userModel import User

router = APIRouter()

# Delete user by ID
@router.delete("/delete/{user_id}")
async def delete_user_id(user_id: str):
    return delete_user_id_controller(user_id)

# Create user
@router.post("/user")
async def create_user(user: User):
    return create_user_controller(user)

# Fetch user by name
@router.get("/user/{name}")
async def read_user(name: str):
    return read_user_controller(name)

# Fetch all users
@router.get("/users")
async def read_users():
    return read_users_controller()

# Update user by name
@router.put("/update/{name}")
async def update_user(name: str, user: User):
    return update_user_controller(name, user)

# Delete user by name
@router.delete("/delete/{name}")
async def delete_user(name: str):
    return delete_user_controller(name)

