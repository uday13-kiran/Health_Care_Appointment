from fastapi import FastAPI
from core.settings import settings


app=FastAPI(title=settings.Title,)