from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, scoped_session
from app.models import Base
from sqlalchemy.engine import Engine


# DATABASE_URL = "mysql://sql12734751:ZizYaiKgYj@sql12.freesqldatabase.com:3306/sql12734751"
DATABASE_URL ="sqlite:///./mydb.db"



engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))



@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON;")
    cursor.close()

def create_db_and_tables():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
