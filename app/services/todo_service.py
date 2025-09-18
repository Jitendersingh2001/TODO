from sqlalchemy.orm import Session

class TodoService:
    def __init__(self, db: Session):
        self.db = db
