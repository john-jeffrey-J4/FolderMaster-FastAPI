from sqlalchemy.orm import Session
from app.models import File
from app.schemas import FileCreate

def create_file(file_data: FileCreate, session: Session) -> File:
    new_file = File(**file_data.dict())
    session.add(new_file)
    session.commit()
    session.refresh(new_file)
    return new_file

def get_file(file_id: int, session: Session) -> File:
    return session.query(File).filter(File.id == file_id).first()

def update_file(file_id: int, file_data: FileCreate, session: Session) -> File:
    db_file = get_file(file_id, session)
    if not db_file:
        return None
    db_file.name = file_data.name
    db_file.folder_id = file_data.folder_id
    session.commit()
    session.refresh(db_file)
    return db_file

def delete_file(file_id: int, session: Session) -> bool:
    db_file = get_file(file_id, session)
    if not db_file:
        return False
    session.delete(db_file)
    session.commit()
    return True
