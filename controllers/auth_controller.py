from fastapi import HTTPException
from database import collection
from models.userModel import UserSignup, UserLogin
from utils.auth import hash_password, verify_password, create_access_token

# Signup
def signup_controller(user: UserSignup):
    user_dict = user.dict()
    user_dict["password"] = hash_password(user_dict["password"])
    
    if collection.find_one({"email": user_dict["email"]}):
        raise HTTPException(status_code=400, detail="Email already exists")
    
    result = collection.insert_one(user_dict)
    if result.inserted_id:
        return {"message": "User created successfully"}

# Login
def login_controller(user: UserLogin):
    db_user = collection.find_one({"email": user.email})
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    access_token = create_access_token(data={"sub": db_user["email"]})
    return {"access_token": access_token, "token_type": "bearer"}