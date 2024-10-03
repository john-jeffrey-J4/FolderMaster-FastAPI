from pydantic import BaseModel
from typing import Optional, List
from app.schemas.file_schemas import FileRead

class FolderCreate(BaseModel):
    name: str
    parent_id: Optional[int] = None

class FolderRead(FolderCreate):
    id: int
    children: List["FolderRead"] = []
    files: List[FileRead] = []

FolderRead.update_forward_refs()

