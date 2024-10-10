from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from app.models import File, Folder
from app.schemas.file_schemas import FileCreate
from app.services.folder_service import get_folder


def create_file(file_data: FileCreate, session: Session) -> File:
    file_available = get_folder(file_data.folder_id, session)
    if not file_available:
        raise HTTPException(status_code=404, detail="No folder available")

    new_file = File(name=file_data.name, folder_id=file_data.folder_id)
    session.add(new_file)
    session.commit()
    session.refresh(new_file)
    return new_file


def get_file(file_id: int, session: Session) -> File:
    return session.query(File).filter(File.id == file_id).first()


def delete_file(file_id: int, session: Session) -> bool:
    file = get_file(file_id, session)
    if file:
        session.delete(file)
        session.commit()
        return True
    return False


def move_file(file_id: int, target_folder_id: int, session: Session) -> File:
    file_to_move = get_file(file_id, session)
    target_folder = get_folder(target_folder_id, session)

    if not file_to_move or (target_folder_id and not target_folder):
        return None
    
    file_to_move.folder_id = target_folder_id
    session.commit()
    session.refresh(file_to_move)
    return file_to_move

def get_folder_path(folder, db: Session):
    if folder.parent_id:
        parent_folder = db.query(Folder).filter(
            Folder.id == folder.parent_id).first()
        if parent_folder:
            return get_folder_path(parent_folder, db) + f"/{folder.name}"

    return folder.name


def file_path(db: Session, file_id: int):
    file = db.query(File).filter(File.id == file_id).first()
    if not file:
        raise HTTPException(status_code=404, detail="File not found")

    folder = db.query(Folder).filter(Folder.id == file.folder_id).first()
    if not folder:
        raise HTTPException(status_code=404, detail="Folder not found")

    folder_path = get_folder_path(folder, db)
    return {"file_path": folder_path}
