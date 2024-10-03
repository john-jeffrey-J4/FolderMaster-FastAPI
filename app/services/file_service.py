from sqlalchemy.orm import Session
from app.models import File
from app.schemas.file_schemas import FileCreate


def create_file(file_data: FileCreate, session: Session) -> File:
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