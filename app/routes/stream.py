import asyncio
import base64

from fastapi import APIRouter, WebSocket, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.queues import output_queue

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        # Obtém frame processado sem bloquear o event loop
        jpg_bytes = await asyncio.get_event_loop().run_in_executor(None, output_queue.get)
        data = base64.b64encode(jpg_bytes).decode("utf-8")
        await websocket.send_text(data) 