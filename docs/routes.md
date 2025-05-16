# Definição de Rotas

## GET /
- Descrição: Página inicial com dropdown de câmeras, template de vídeo e canvas para stream

## WebSocket /ws/{camera_id}
- Descrição: Envia frames JPEG codificados em base64 da câmera especificada para renderização em tempo real

## GET /cameras
- Descrição: Lista configurações das câmeras (id, url, type, always_on)

## POST /cameras
- Descrição: Adiciona e inicia uma câmera sob demanda
- Body: JSON com campos id, url, type e always_on

## DELETE /cameras/{camera_id}
- Descrição: Para e remove uma câmera existente

## GET /events
- Descrição: Lista todos os eventos de detecção

## GET /faces/known
- Descrição: Lista todas as faces conhecidas

## GET /faces/unknown
- Descrição: Lista todas as faces desconhecidas 