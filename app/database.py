from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from app.models import Base

# Replace with your actual database URL
DATABASE_URL = "mysql://sql12734751:ZizYaiKgYj@sql12.freesqldatabase.com:3306/sql12734751"

# Create synchronous engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))

# Create the tables in the database
def create_db_and_tables():
    Base.metadata.create_all(bind=engine)

# Dependency for getting a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
