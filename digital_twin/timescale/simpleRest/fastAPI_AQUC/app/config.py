import os
from dotenv import load_dotenv

from pathlib import Path
#ngrok
from pydantic import BaseSettings

env_path = Path('./app') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings(BaseSettings):
    PROJECT_NAME:str = "CDL-MINT Project-Perform CRUD operations for storing sensor data in server with the APIs"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER : str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER","localhost")
    POSTGRES_PORT : str = os.getenv("POSTGRES_PORT",5432) # default postgres port is 5432
    POSTGRES_DB : str = os.getenv("POSTGRES_DB","tdd")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    BASE_URL = "http://localhost:8000/docs"
    USE_NGROK = os.environ.get("USE_NGROK", "False") == "True"

settings = Settings()