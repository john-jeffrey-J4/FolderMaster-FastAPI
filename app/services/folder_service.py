from sqlalchemy.orm import Session
from app.models import Folder
from app.schemas.folder_schemas import FolderCreate

def create_folder(folder_data: FolderCreate, session: Session) -> Folder:
    new_folder = Folder(name=folder_data.name, parent_id=folder_data.parent_id)
    session.add(new_folder)
    session.commit()
    session.refresh(new_folder)
    return new_folder

def get_folder(folder_id: int, session: Session) -> Folder:
    return session.query(Folder).filter(Folder.id == folder_id).first()

def delete_folder(folder_id: int, session: Session) -> bool:
    folder = get_folder(folder_id, session)
    if folder:
        session.delete(folder)
        session.commit()
        return True
    return False


