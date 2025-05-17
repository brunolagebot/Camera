from sqlalchemy.orm import Session
from datetime import datetime

from app.database.session import SessionLocal
from app.database.models import Event, KnownFace, UnknownFace


def save_event(camera_id: str, face_id: int | None, face_type: str) -> Event:
    db: Session = SessionLocal()
    try:
        event = Event(camera_id=camera_id, face_id=face_id, face_type=face_type)
        db.add(event)
        db.commit()
        db.refresh(event)
        return event
    finally:
        db.close()


def save_known_face(name: str, embedding: dict) -> KnownFace:
    db: Session = SessionLocal()
    try:
        kf = KnownFace(name=name, embedding=embedding)
        db.add(kf)
        db.commit()
        db.refresh(kf)
        return kf
    finally:
        db.close()


def save_unknown_face(embedding: dict) -> UnknownFace:
    db: Session = SessionLocal()
    try:
        uf = UnknownFace(embedding=embedding)
        db.add(uf)
        db.commit()
        db.refresh(uf)
        return uf
    finally:
        db.close() 