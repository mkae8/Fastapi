# from pydantic import BaseModel, EmailStr

# class User(BaseModel):
#     name: str
#     age: int
#     password: str
#     email: EmailStr
#     jobTitle: str


from pydantic import BaseModel, EmailStr
from typing import Optional


class UserSignup(BaseModel):
    name: str
    email: EmailStr
    password: str
    occupation: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Note(BaseModel):
    note: str
    comment: Optional[str] = None