from fastapi import FastAPI
from app.routes import folder, file
from app.database import create_db_and_tables

app = FastAPI()

# Create the database tables on startup
@app.on_event("startup")
def startup():
    create_db_and_tables()

# Include the routes
app.include_router(folder.router)
app.include_router(file.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the File Management System!"}
