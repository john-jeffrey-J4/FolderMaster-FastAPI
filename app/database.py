from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from app.models import Base

DATABASE_URL = "mysql://sql12734751:ZizYaiKgYj@sql12.freesqldatabase.com:3306/sql12734751"

engine = create_engine(DATABASE_URL)

SessionLocal = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))

def create_db_and_tables():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
