# cameras

Aplicação de reconhecimento facial via RTSP.

Repositório: https://github.com/brunolagebot/cameras  
Mantenedor: Bruno Lage <bruno.lage@hotmail.com>

Consulte `docs/structure.md` para detalhes da estrutura e `docs/changelog.md` para histórico de versões.

## Configuração
- Copie o modelo de ambiente e ajuste a variável:
  ```bash
  cp .env.example .env
  ```
- Edite o arquivo `.env` para refletir suas câmeras e URL do banco.
- Instale o PostgreSQL (macOS):
  ```bash
  brew install postgresql
  brew services start postgresql
  ```
- Crie o banco de dados:
  ```bash
  createdb cameras_db
  ```
- No `.env`, defina:
  ```env
  DATABASE_URL=postgresql://user:password@localhost:5432/cameras_db
  ```
- Instale dependências para detecção de faces:
  ```bash
  brew install cmake
  pip install setuptools dlib face-recognition
  # Se receber aviso sobre face_recognition_models, execute:
  pip install git+https://github.com/ageitgey/face_recognition_models
  pip freeze > requirements.txt
  ```

## Endpoints
- GET `/` : página inicial com seleção de câmeras
- WebSocket `/ws/{camera_id}` : envia stream processado para a câmera especificada
- GET `/cameras` : lista todas as câmeras configuradas
- POST `/cameras` : adiciona e inicia uma câmera sob demanda (body JSON: id, url, type, always_on)
- DELETE `/cameras/{camera_id}` : para e remove uma câmera existente 