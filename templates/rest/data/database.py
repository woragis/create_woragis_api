from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# from constants.index import DATABASE_URL

DATABASE_URL = "postgresql+psycopg://postgres:postgres@db:5432/postgres"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()  # THIS is the Base you import in models.py
