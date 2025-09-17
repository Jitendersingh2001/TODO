from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse
from app.config.database import get_db
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["User"])


@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.create_user(user)
