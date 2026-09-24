from core.settings import settings
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session

Base=DeclarativeBase()
engine=create_engine(settings.DataBaseUrl)
SessionLocal=Session(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

