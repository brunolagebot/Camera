import multiprocessing
from config import CAMERAS
from app.camera import CameraProcess
from app.detectors.face_detector import DetectionProcess

class CameraManager:
    def __init__(self):
        # Manager para criar filas compartilhadas
        self.manager = multiprocessing.Manager()
        # Configurações de câmeras do ambiente
        self.configs = CAMERAS
        # Dicionário de processos ativos: id -> dict(com processos e fila de saída)
        self.processes = {}

    def start_all(self):
        # Inicia todas as câmeras marcadas como always_on
        for conf in self.configs:
            if conf.get("always_on", False):
                self.start(conf)

    def start(self, conf: dict):
        cam_id = conf["id"]
        if cam_id in self.processes:
            return
        # Cria filas dedicadas para esta câmera
        frame_q = self.manager.Queue(maxsize=10)
        output_q = self.manager.Queue(maxsize=10)
        # Instancia processos de captura e detecção
        cam_proc = CameraProcess(conf["url"], frame_q)
        det_proc = DetectionProcess(frame_q, output_q)
        cam_proc.start()
        det_proc.start()
        self.processes[cam_id] = {"camera": cam_proc, "detect": det_proc, "output_queue": output_q}

    def stop(self, cam_id: str):
        # Para processos de captura e detecção de uma câmera
        proc = self.processes.get(cam_id)
        if not proc:
            return
        proc["camera"].stop()
        proc["detect"].stop()
        del self.processes[cam_id]

    def stop_all(self):
        # Para todas as câmeras ativas
        for cam_id in list(self.processes.keys()):
            self.stop(cam_id)

# Instância global do gerenciador
manager = CameraManager() 