from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
from pydantic import BaseModel

from app.database.session import SessionLocal
from app.database.models import KnownFace, UnknownFace

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class KnownFaceSchema(BaseModel):
    id: int
    name: str
    embedding: dict
    created_at: datetime

    class Config:
        orm_mode = True

@router.get("/faces/known", response_model=List[KnownFaceSchema])
def list_known_faces(db: Session = Depends(get_db)):
    """Lista todas as faces conhecidas"""
    return db.query(KnownFace).all()

class UnknownFaceSchema(BaseModel):
    id: int
    embedding: dict
    detected_at: datetime

    class Config:
        orm_mode = True

@router.get("/faces/unknown", response_model=List[UnknownFaceSchema])
def list_unknown_faces(db: Session = Depends(get_db)):
    """Lista todas as faces desconhecidas"""
    return db.query(UnknownFace).all() 