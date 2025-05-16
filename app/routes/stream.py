import asyncio
import base64

from fastapi import APIRouter, WebSocket, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.camera_manager import manager

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    # Pega lista de câmeras configuradas
    cameras = manager.configs
    return templates.TemplateResponse("index.html", {"request": request, "cameras": cameras})

@router.websocket("/ws/{camera_id}")
async def websocket_endpoint(websocket: WebSocket, camera_id: str):
    await websocket.accept()
    while True:
        # Obtém frame processado da câmera específica sem bloquear o event loop
        output_q = manager.processes.get(camera_id, {}).get("output_queue")
        if not output_q:
            break
        jpg_bytes = await asyncio.get_event_loop().run_in_executor(None, output_q.get)
        data = base64.b64encode(jpg_bytes).decode("utf-8")
        await websocket.send_text(data) 