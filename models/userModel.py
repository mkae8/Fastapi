from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    age: int
    password: str
    email: EmailStr
    jobTitle: str