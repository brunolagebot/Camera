import os
from dotenv import load_dotenv

# Carrega variáveis de .env
load_dotenv()

# URL RTSP da câmera
RTSP_URL = os.getenv("RTSP_URL") 