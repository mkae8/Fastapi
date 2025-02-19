# from fastapi import HTTPException
# from database import collection
# from pymongo.errors import DuplicateKeyError
# from bson import ObjectId
# import bcrypt
# from models.userModel import User

# # Hash password
# def hash_password(password: str) -> str:
#     salt = bcrypt.gensalt()
#     hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
#     return hashed_password.decode('utf-8')

# # Create user
# def create_user_controller(user: User):
#     user_dict = user.dict()
#     user_dict["password"] = hash_password(user_dict["password"])
#     try:
#         result = collection.insert_one(user_dict)
#         if result.inserted_id:
#             return {"message": "User created", "id": str(result.inserted_id)}
#     except DuplicateKeyError:
#         raise HTTPException(status_code=400, detail="Email already exists")
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Failed to create user")

# # Fetch user by name
# def read_user_controller(name: str):
#     user = collection.find_one({"name": name}, {"_id": 0, "password": 0})
#     if user:
#         return user
#     raise HTTPException(status_code=404, detail="User not found")

# # Fetch all users
# def read_users_controller():
#     all_users = list(collection.find({}, {"_id": 0, "password": 0}))
#     if not all_users:
#         raise HTTPException(status_code=404, detail="There is no data")
#     return all_users

# # Update user by name
# def update_user_controller(name: str, user: User):
#     user_dict = user.dict()
#     if "password" in user_dict:
#         user_dict["password"] = hash_password(user_dict["password"])
    
#     updated_result = collection.update_one({"name": name}, {"$set": user_dict})
#     if updated_result.modified_count > 0:
#         return {"message": "User updated"}
#     raise HTTPException(status_code=404, detail="User not found")

# # Delete user by name
# def delete_user_controller(name: str):
#     result = collection.delete_one({"name": name})
#     if result.deleted_count > 0:
#         return {"message": "User data deleted successfully"}
#     raise HTTPException(status_code=404, detail="User not found")

# # Delete user by ID
# def delete_user_id_controller(user_id: str):
#     try:
#         obj_id = ObjectId(user_id)
#     except Exception as e:
#         raise HTTPException(status_code=400, detail="Invalid user Id format")
    
#     result = collection.delete_one({"_id": obj_id})
#     if result.deleted_count > 0:
#         return {"message": "User data deleted successfully"}
#     raise HTTPException(status_code=404, detail="User not found")


from fastapi import HTTPException, UploadFile
from database import collection
from models.userModel import Note


def upload_file_controller(file: UploadFile, user_email: str):
    file_content = file.file.read()
    return {"filename": file.filename, "user_email": user_email}

def add_note_controller(user_email: str, note: Note):
    result = collection.update_one(
        {"email": user_email},
        {"$push": {"notes": note.dict()}}
    )
    if result.modified_count > 0:
        return {"message": "Note added successfully"}
    raise HTTPException(status_code=404, detail="User not found")