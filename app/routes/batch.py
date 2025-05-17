from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import List

from app.services.batch import process_batch_images

router = APIRouter()

@router.post("/batch/upload-images")
async def batch_upload_images(files: List[UploadFile] = File(...)):
    """Recebe múltiplos arquivos de imagem e persiste embeddings no banco."""
    try:
        results = process_batch_images(files)
        return {"processed": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 