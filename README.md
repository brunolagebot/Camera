# cameras

Aplicação de reconhecimento facial via RTSP.

Repositório: https://github.com/brunolagebot/cameras  
Mantenedor: Bruno Lage <bruno.lage@hotmail.com>

Consulte `docs/structure.md` para detalhes da estrutura e `docs/changelog.md` para histórico de versões.

## Configuração
- Edite o arquivo `.env` (baseado em `.env.example`) definindo `CAMERAS_JSON` com array de câmeras.

## Endpoints
- GET `/` : página inicial com seleção de câmeras
- WebSocket `/ws/{camera_id}` : envia stream processado para a câmera especificada
- GET `/cameras` : lista todas as câmeras configuradas
- POST `/cameras` : adiciona e inicia uma câmera sob demanda (body JSON: id, url, type, always_on)
- DELETE `/cameras/{camera_id}` : para e remove uma câmera existente 