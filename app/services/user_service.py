from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError


class UserService:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: UserCreate) -> User:
        try:
            new_user = User(
                username=user.username,
                email=user.email,
                password=user.password
            )
            self.db.add(new_user)
            self.db.commit()
            self.db.refresh(new_user)
            return new_user
        except SQLAlchemyError as e:
            self.db.rollback()  # rollback transaction on failure
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Database error: {str(e)}"
            )
