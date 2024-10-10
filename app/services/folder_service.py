from sqlalchemy.orm import Session
from app.models import Folder
from app.schemas.folder_schemas import FolderCreate
from fastapi.exceptions import HTTPException


def create_folder(folder_data: FolderCreate, session: Session) -> Folder:
    folder_avaialble = get_folder(folder_data.parent_id, session)
    if not folder_avaialble:
        raise HTTPException(status_code=404, detail= "No folder available.")
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


def move_folder(folder_id: int, target_parent_id: int, session: Session) -> Folder:

    folder_to_move = session.query(Folder).filter(Folder.id == folder_id).first()
    target_parent_folder = session.query(Folder).filter(Folder.id == target_parent_id).first()
    if not folder_to_move:
        return None

    if target_parent_id and not target_parent_folder:
        return None

    current_folder = target_parent_folder
    while current_folder:
        if current_folder.id == folder_id:
            return None 
        current_folder = current_folder.parent

    folder_to_move.parent_id = target_parent_id
    session.commit()
    session.refresh(folder_to_move)

    return folder_to_move
