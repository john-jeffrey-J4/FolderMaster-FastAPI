from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import FileCreate, FileRead
from app.services.file_service import create_file, get_file, update_file, delete_file
from app.database import get_db

router = APIRouter()

@router.post("/files/", response_model=FileRead)
def create_new_file(file: FileCreate, session: Session = Depends(get_db)):
    return create_file(file, session)

@router.get("/files/{file_id}", response_model=FileRead)
def read_file(file_id: int, session: Session = Depends(get_db)):
    file = get_file(file_id, session)
    if not file:
        raise HTTPException(status_code=404, detail="File not found")
    return file

@router.put("/files/{file_id}", response_model=FileRead)
def update_existing_file(file_id: int, file: FileCreate, session: Session = Depends(get_db)):
    updated_file = update_file(file_id, file, session)
    if not updated_file:
        raise HTTPException(status_code=404, detail="File not found")
    return updated_file

@router.delete("/files/{file_id}")
def remove_file(file_id: int, session: Session = Depends(get_db)):
    success = delete_file(file_id, session)
    if not success:
        raise HTTPException(status_code=404, detail="File not found")
    return {"message": "File deleted"}
