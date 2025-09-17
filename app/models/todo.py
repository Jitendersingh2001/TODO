from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.config.database import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    is_completed = Column(Boolean, default=False, nullable=False)
    
    # Foreign key to User.id
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Automatically set timestamp when row is created
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    
    # Automatically update timestamp whenever row is updated
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)

    # Relationship to User
    user = relationship("User", back_populates="todos")
