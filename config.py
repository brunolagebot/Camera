import os
from dotenv import load_dotenv
import json

# Carrega variáveis de .env
load_dotenv()

# URL RTSP da câmera
RTSP_URL = os.getenv("RTSP_URL")

# URL de conexão com banco de dados
DATABASE_URL = os.getenv("DATABASE_URL")

# Carrega a variável CAMERAS_JSON, fallback para lista vazia
_raw = os.getenv("CAMERAS_JSON", "").strip()
if not _raw:
    _raw = "[]"
# Remove aspas simples ou duplas externas
if _raw and _raw[0] in ('"', "'") and _raw[-1] == _raw[0]:
    _raw = _raw[1:-1]
# Desserializa JSON com tratamento de erro
try:
    CAMERAS = json.loads(_raw)
except json.JSONDecodeError:
    print(f"[WARNING] CAMERAS_JSON inválido: '{_raw}', usando lista vazia.")
    CAMERAS = [] 