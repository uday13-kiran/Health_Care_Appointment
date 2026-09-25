from fastapi import FastAPI
from core.settings import settings
from contextlib import asynccontextmanager
from core.database import get_db,Base,engine
from fastapi import status


@asynccontextmanager
async def lifespan(app:FastAPI):
    print("server started")
    db=get_db
    Base.metadata.create_all(bind=engine)
    yield
    print('server disconnected')

app=FastAPI(title=settings.Title,description='hospital queue management system for appointments and visits',version='1.0.1',lifespan=lifespan)

@app.get('/health',status_code=status.HTTP_200_OK)
def health():
    return {'status':"OK"}

