# Changelog

## v0.2.2 - 2025-05-16

- fix: instancia CascadeClassifier dentro do método run de face_detector para evitar erro de pickle em multiprocessing

## v0.2.1 - 2025-05-16

- fix: atualizar index.html para seleção de câmera e WebSocket dinâmico
- feat: index route inclui lista de câmeras no contexto do template

## v0.2.0 - 2025-05-16

- feat: implementa CameraManager para múltiplas câmeras dinâmicas
- feat: adiciona rotas GET/POST/DELETE em /cameras
- refactor: adapta camera.py e face_detector.py para injeção de filas por câmera
- feat: atualiza WebSocket para /ws/{camera_id}

## v0.1.1 - 2025-05-16

- docs: adiciona link do repositório e email de contato

## v0.1.0 - 2025-05-16

- Scaffold inicial da aplicação RTSP com FastAPI e detecção facial usando processos paralelos 