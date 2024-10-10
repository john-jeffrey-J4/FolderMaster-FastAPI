# models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Folder(Base):
    __tablename__ = 'folders'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True, unique=True)
    parent_id = Column(Integer, ForeignKey('folders.id'))

    parent = relationship("Folder", remote_side=[id], backref="children")
    files = relationship("File", back_populates="folder")


class File(Base):
    __tablename__ = 'files'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    folder_id = Column(Integer, ForeignKey('folders.id'))

    folder = relationship("Folder", back_populates="files")
