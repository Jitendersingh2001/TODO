from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .settings import settings

# --- Create SQLAlchemy engine ---
engine = create_engine(settings.db.DB_DATABASE_URL, echo=settings.app.APP_DEBUG)

# --- Create a configured "Session" class ---
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# --- Base class for models ---
Base = declarative_base()

# --- Dependency for FastAPI ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
