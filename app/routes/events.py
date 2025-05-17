from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel

from app.database.session import SessionLocal
from app.database.models import Event

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class EventSchema(BaseModel):
    id: int
    camera_id: str
    timestamp: datetime
    face_id: Optional[int]
    face_type: str

    class Config:
        orm_mode = True

@router.get("/events", response_model=List[EventSchema])
async def list_events(db: Session = Depends(get_db)):
    """Lista todos os eventos de detecção"""
    return db.query(Event).all() 