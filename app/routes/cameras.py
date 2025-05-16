from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

from app.camera_manager import manager

router = APIRouter()

class CameraConfig(BaseModel):
    id: str
    url: str
    type: str
    always_on: bool = False

@router.get("/", response_model=List[CameraConfig])
async def list_cameras():
    """Retorna configuração de todas as câmeras"""
    return manager.configs

@router.post("/", response_model=dict)
async def add_camera(config: CameraConfig):
    """Adiciona e inicia uma câmera sob demanda"""
    if config.id in manager.processes:
        raise HTTPException(status_code=400, detail="Câmera já existe")
    manager.start(config.dict())
    manager.configs.append(config.dict())
    return {"status": "started", "id": config.id}

@router.delete("/{camera_id}", response_model=dict)
async def remove_camera(camera_id: str):
    """Para e remove uma câmera"""
    if camera_id not in manager.processes:
        raise HTTPException(status_code=404, detail="Câmera não encontrada")
    manager.stop(camera_id)
    manager.configs = [c for c in manager.configs if c["id"] != camera_id]
    return {"status": "stopped", "id": camera_id} 