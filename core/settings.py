import os
from dotenv import load_dotenv

load_dotenv()

class Settings():
    DataBaseUrl:str=os.getenv('DataBaseUrl')
    Title:str=os.getenv("Title")

settings=Settings()
print(settings.DataBaseUrl)