from fastapi import FastAPI
from app.camera_manager import manager
from app.routes.stream import router as stream_router
from app.routes.cameras import router as cameras_router
from app.routes.events import router as events_router
from app.routes.faces import router as faces_router
from app.routes.dashboard import router as dashboard_router
from app.database.session import engine, Base

app = FastAPI()

# Inclui rotas de streaming e gerenciamento de câmeras
app.include_router(stream_router)
app.include_router(cameras_router, prefix="/cameras")
app.include_router(events_router)
app.include_router(faces_router)
app.include_router(dashboard_router)

@app.on_event("startup")
def on_startup():
    # Cria tabelas no banco de dados
    Base.metadata.create_all(bind=engine)
    # Inicia captura e detecção nas câmeras configuradas
    manager.start_all()

@app.on_event("shutdown")
def on_shutdown():
    manager.stop_all() 