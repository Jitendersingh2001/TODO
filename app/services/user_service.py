from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from passlib.context import CryptContext
from app.constants.message import UserMessages, DBMessages, AuthMessages
from app.utils.helper import create_access_token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    def __init__(self, db: Session):
        self.db = db

    # Function to create a new user
    def create_user(self, user: UserCreate) -> User:
        try:
            # Check if the user already exists
            existing_user = self.db.query(User).filter(User.email == user.email).first()

            if existing_user:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=UserMessages.EXISTS
                )
            
            # Hash the password before storing it
            hashed_password = self._hash_password(user.password) 


            new_user = User(
                username=user.username,
                email=user.email,
                password=hashed_password
            )
            self.db.add(new_user)
            self.db.commit()
            self.db.refresh(new_user)
            return new_user
        except SQLAlchemyError as e:
            self.db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=DBMessages.ERROR
            )

    # Private method to hash passwords
    def _hash_password(self, password: str) -> str:
        return pwd_context.hash(password)

    # Private method to verify passwords
    def _verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)
    
    # function to authenticate user during login
    def authenticate_user(self, email: str, password: str):
        user = self.db.query(User).filter(User.email == email).first()
        if not user or not self._verify_password(password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=UserMessages.INVALID_CREDENTIALS
            )
        else:
            token = create_access_token(data={"sub": user.email})
            return {"message": AuthMessages.LOGGED_IN , "token": token, "token_type": "bearer"}
