from core.settings import settings
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine=create_engine(settings.DataBaseUrl)
Base=declarative_base()
SessionLocal=sessionmaker(
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

