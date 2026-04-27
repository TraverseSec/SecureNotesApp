from .core.config import DATABASE_URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(engine)

class Base(DeclarativeBase):
    pass