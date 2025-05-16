from fastapi import FastAPI
from app.camera_manager import manager
from app.routes.stream import router as stream_router
from app.routes.cameras import router as cameras_router

app = FastAPI()

# Inclui rotas de streaming e gerenciamento de câmeras
app.include_router(stream_router)
app.include_router(cameras_router, prefix="/cameras")

@app.on_event("startup")
def on_startup():
    manager.start_all()

@app.on_event("shutdown")
def on_shutdown():
    manager.stop_all() 