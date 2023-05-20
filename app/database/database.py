from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config

DATABASE=config('DATABASE')
USER=config('DATABASE_USER')
PASSWORD=config('DATABASE_PASSWORD')
SERVER=config('DATABASE_SERVER')
PORT=int(config('DATABASE_PORT'))
NAME=config('DATABASE_NAME')

SQLALCHEMY_DATABASE_URL = f"{DATABASE}://{USER}:{PASSWORD}@{SERVER}:{PORT}/{NAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)