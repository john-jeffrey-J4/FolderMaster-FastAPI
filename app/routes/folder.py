from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.folder_schemas import FolderCreate, FolderRead
from app.services.folder_service import create_folder, get_folder, delete_folder
from app.database import get_db


router = APIRouter()

@router.post("/folders/", response_model=FolderRead)
def create_new_folder(folder: FolderCreate, session: Session = Depends(get_db)):
    return create_folder(folder, session)

@router.get("/folders/{folder_id}", response_model=FolderRead)
def read_folder(folder_id: int, session: Session = Depends(get_db)):
    folder = get_folder(folder_id, session)
    if not folder:
        raise HTTPException(status_code=404, detail="Folder not found")
    return folder

@router.delete("/folders/{folder_id}")
def remove_folder(folder_id: int, session: Session = Depends(get_db)):
    success = delete_folder(folder_id, session)
    if not success:
        raise HTTPException(status_code=404, detail="Folder not found")
    return {"message": "Folder deleted"}


@router.put("/folders/{folder_id}/move/{target_parent_id}", response_model=FolderRead)
def move_existing_folder(folder_id: int, target_parent_id: int, session: Session = Depends(get_db)):
    moved_folder = move_folder(folder_id, target_parent_id, session)
    if not moved_folder:
        raise HTTPException(status_code=404, detail="Folder not found or invalid target parent")
    return moved_folder

