from sqlalchemy.orm import Session
from app.models.todo import Todo
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from app.constants.message import Messages
from sqlalchemy import update


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

    def complete_todo(self, todo_id: int):
        try:
            todo = self.db.get(Todo, todo_id)
            self._checkTodoExists(todo)
            update(Todo).where(Todo.id == todo_id).values(
                is_completed=True)
            return {"message": "Todo marked as completed"}
        except SQLAlchemyError as e:
            self.db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=Messages.ERROR
            )
        except Exception as e:
            self.db.rollback()
            return {"error": str(e)}

    def delete_todo(self, todo_id: int):
        try:
            todo = self.db.get(Todo, todo_id)
            self._checkTodoExists(todo)
            self.db.delete(todo)
            self.db.commit()
            return {"message": "Todo deleted successfully"}
        except SQLAlchemyError as e:
            self.db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=Messages.ERROR
            )
        except Exception as e:
            self.db.rollback()
            return {"error": str(e)}

    def edit_todo(self, todo_id: int, title: str, description: str):
        try:
            todo = self.db.get(Todo, todo_id)
            self._checkTodoExists(todo)
            self._checkTodoIsCompleted(todo)
            update(Todo).where(Todo.id == todo_id).values(
                title=title, description=description)
            return {"message": "Todo updated successfully"}
        except SQLAlchemyError as e:
            self.db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=Messages.ERROR
            )
        except Exception as e:
            self.db.rollback()
            return {"error": str(e)}

    def _checkTodoIsCompleted(self, todo: Todo):
        if todo.is_completed:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Completed tasks cannot be edited"
            )

    def _checkTodoExists(self, todo: Todo):
        if not todo:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=Messages.NOT_FOUND
            )
        
    def get_todos(self, user_id: int):
        try:
            todos = self.db.query(Todo).filter(Todo.created_by == user_id).all()
            return todos
        except SQLAlchemyError as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=Messages.ERROR
            )
        except Exception as e:
            return {"error": str(e)}
