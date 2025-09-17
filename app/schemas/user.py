from pydantic import BaseModel, EmailStr
from datetime import datetime

# Request schema (for creating a user)
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# Request schema for login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Response schema (for returning user info)
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True  # Enable ORM mode
