import os
from dotenv import load_dotenv

load_dotenv()

class Settings():
    DataBaseUrl=os.getenv('DataBaseUrl')
    Title=os.getenv("Title")

settings=Settings()