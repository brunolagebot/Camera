from fastapi import UploadFile
import cv2
import numpy as np
import face_recognition

from app.services.storage import save_unknown_face, save_event


def process_batch_images(files: list[UploadFile], camera_id: str = None) -> list[dict]:
    """
    Processa lista de imagens: detecta faces, gera embeddings e persiste como unknown_faces.
    Retorna lista de dicionários com {"unknown_id": int, "filename": str}.
    """
    results = []
    for upload in files:
        # lê bytes da imagem
        data = upload.file.read()
        # converte para array numpy
        img_array = np.frombuffer(data, np.uint8)
        image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # detecta embeddings na imagem
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(rgb)
        for encoding in encodings:
            # persiste face desconhecida
            uf = save_unknown_face(encoding.tolist())
            results.append({"unknown_id": uf.id, "filename": upload.filename})
    return results 