from pydantic import BaseModel
from typing import Optional, List

class FolderCreate(BaseModel):
    name: str
    parent_id: Optional[int] = None

class FileCreate(BaseModel):
    name: str
    folder_id: int

class FolderRead(FolderCreate):
    id: int
    sub_folders: List["FolderRead"] = []
    files: List["FileRead"] = []

class FileRead(FileCreate):
    id: int

# For recursive models
FolderRead.update_forward_refs()
