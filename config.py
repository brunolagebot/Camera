import os
from dotenv import load_dotenv
import json

# Carrega variáveis de .env
load_dotenv()

# URL RTSP da câmera
RTSP_URL = os.getenv("RTSP_URL")

# Lista de câmeras: cada item tem id, url, type e always_on
CAMERAS = json.loads(os.getenv("CAMERAS_JSON", "[]")) 