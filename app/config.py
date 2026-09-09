import os 
from dotenv import load_dotenv 

load_dotenv() # Load environment variables from .env file

class Settings: 
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    SECRET_KEY: str = os.getenv("SECRET_KEY")

settings = Settings()


