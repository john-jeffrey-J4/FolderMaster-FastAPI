from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from typing import List, Optional

Base = declarative_base()

class Folder(Base):
    __tablename__ = "folder"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)  # Specify a length for the VARCHAR field
    parent_id = Column(Integer, ForeignKey("folder.id"), nullable=True)

    # Relationships
    sub_folders = relationship("Folder", backref="parent_folder", remote_side=[id])
    files = relationship("File", backref="folder")

class File(Base):
    __tablename__ = "file"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)  # Specify a length for the VARCHAR field
    folder_id = Column(Integer, ForeignKey("folder.id"))
