from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional


# Request schema (for creating a user)
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


# Response schema (for returning user info)
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True  # allows SQLAlchemy model → Pydantic conversion
