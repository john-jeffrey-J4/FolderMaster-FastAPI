from sqlalchemy.orm import Session
from app.models import Folder
from app.schemas import FolderCreate

def create_folder(folder_data: FolderCreate, session: Session) -> Folder:
    new_folder = Folder(**folder_data.dict())
    session.add(new_folder)
    session.commit()
    session.refresh(new_folder)
    return new_folder

def get_folder(folder_id: int, session: Session) -> Folder:
    return session.query(Folder).filter(Folder.id == folder_id).first()

def update_folder(folder_id: int, folder_data: FolderCreate, session: Session) -> Folder:
    db_folder = get_folder(folder_id, session)
    if not db_folder:
        return None
    db_folder.name = folder_data.name
    db_folder.parent_id = folder_data.parent_id
    session.commit()
    session.refresh(db_folder)
    return db_folder

def delete_folder(folder_id: int, session: Session) -> bool:
    db_folder = get_folder(folder_id, session)
    if not db_folder:
        return False
    session.delete(db_folder)
    session.commit()
    return True
