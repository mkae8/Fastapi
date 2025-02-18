from fastapi import FastAPI, HTTPException
from database import collection
from pymongo.errors import DuplicateKeyError
import bcrypt
from models.userModel import User

app = FastAPI()

# Hashed password

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

# Create user 
@app.post("/user")
async def create_user(user: User):
    user_dict = user.dict()
    
    user_dict["password"] = hash_password(user_dict["password"])
    
    try:
        result = collection.insert_one(user_dict)
        if result.inserted_id:
            return {"message": "User created", "id": str(result.inserted_id)}
    except DuplicateKeyError:
        raise HTTPException(status_code=400, detail="Email already exists")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to create user")

# Fetch User
@app.get("/user/{name}")
async def read_user(name: str):
    user = collection.find_one({"name": name}, {"_id": 0, "password": 0})
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")

# Fetch all users 
@app.get("/users")
async def read_users():
    all_users = list(collection.find({}, {"_id": 0, "password": 0}))
    if not all_users:
        raise HTTPException(status_code=404, detail="There is no data")
    return all_users

# Update User
@app.put("/update/{name}")
async def update_user(name: str, user: User):
    user_dict = user.dict()
    
    if "password" in user_dict:
        user_dict["password"] = hash_password(user_dict["password"])
    
    updated_result = collection.update_one({"name": name}, {"$set": user_dict})
    if updated_result.modified_count > 0:
        return {"message": "User updated"}
    raise HTTPException(status_code=404, detail="User not found")

# Delete User
@app.delete("/delete/{name}")
async def delete_user(name: str):
    result = collection.delete_one({"name": name})
    if result.deleted_count > 0:
        return {"message": "User data deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")