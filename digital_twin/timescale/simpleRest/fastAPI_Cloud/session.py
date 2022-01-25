from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import settings


SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)