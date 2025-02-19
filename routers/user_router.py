# from fastapi import APIRouter, HTTPException
# from controllers.user_controllers import (
#     create_user_controller,
#     read_user_controller,
#     read_users_controller,
#     update_user_controller,
#     delete_user_controller,
#     delete_user_id_controller,
# )
# from models.userModel import User

# router = APIRouter()

# @router.delete("/delete/{user_id}")
# async def delete_user_id(user_id: str):
#     return delete_user_id_controller(user_id)


# @router.post("/user")
# async def create_user(user: User):
#     return create_user_controller(user)


# @router.get("/user/{name}")
# async def read_user(name: str):
#     return read_user_controller(name)


# @router.get("/users")
# async def read_users():
#     return read_users_controller()


# @router.put("/update/{name}")
# async def update_user(name: str, user: User):
#     return update_user_controller(name, user)


# @router.delete("/delete/{name}")
# async def delete_user(name: str):
#     return delete_user_controller(name)

from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from utils.auth import decode_token
from controllers.user_controllers import upload_file_controller, add_note_controller
from models.userModel import Note

router = APIRouter()

def get_current_user(token: str):
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    return payload["sub"]

@router.post("/upload")
async def upload_file(file: UploadFile = File(...), user_email: str = Depends(get_current_user)):
    return upload_file_controller(file, user_email)

@router.post("/note")
async def add_note(note: Note, user_email: str = Depends(get_current_user)):
    return add_note_controller(user_email, note)