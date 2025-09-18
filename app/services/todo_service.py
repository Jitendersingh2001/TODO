from sqlalchemy.orm import Session
from app.models.todo import Todo
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from app.constants.message import Messages


class TodoService:
    def __init__(self, db: Session):
        self.db = db

    def create_todo(self, user_id: int, title: str, description: str):
        try:
            todo = Todo(
                title=title,
                description=description,
                is_completed=False,
                created_by=user_id,
            )
            self.db.add(todo)
            self.db.commit()
            self.db.refresh(todo)
            return {"message": "Todo created successfully"}
        except SQLAlchemyError as e:
            self.db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=Messages.ERROR
            )
        except Exception as e:
            self.db.rollback()
            return {"error": str(e)}
