from pydantic import BaseModel

class FileCreate(BaseModel):
    name: str
    folder_id: int

class FileRead(FileCreate):
    id: int
