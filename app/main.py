import multiprocessing

from fastapi import FastAPI
from config import RTSP_URL

from app.camera import CameraProcess
from app.detectors.face_detector import DetectionProcess
from app.routes.stream import router as stream_router

app = FastAPI()

# Inclui rotas
app.include_router(stream_router)

# Processos de captura e detecção
camera_process = CameraProcess(RTSP_URL)
detection_process = DetectionProcess()

@app.on_event("startup")
def on_startup():
    camera_process.start()
    detection_process.start()

@app.on_event("shutdown")
def on_shutdown():
    camera_process.stop()
    detection_process.stop() 