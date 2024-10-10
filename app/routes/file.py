from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.file_schemas import FileCreate, FileRead
from app.services.file_service import create_file, file_path, get_file, delete_file, move_file
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

@router.delete("/files/{file_id}")
def remove_file(file_id: int, session: Session = Depends(get_db)):
    success = delete_file(file_id, session)
    if not success:
        raise HTTPException(status_code=404, detail="File not found")
    return {"message": "File deleted"}


@router.put("/files/{file_id}/move/")
def move_file_api(file_id: int, target_folder_id: int, db: Session = Depends(get_db)):
  
    moved_file = move_file(file_id, target_folder_id, db)

    if moved_file is None:
        raise HTTPException(status_code=404, detail="File or Target Folder not found")

    return {
        "message": "File moved successfully",
        "file_id": moved_file.id,
        "file_name": moved_file.name,
        "new_folder_id": moved_file.folder_id
    }


@router.get("/files/{file_id}/path")
def get_file_path(file_id: int, db: Session = Depends(get_db)):
    return file_path(db, file_id)