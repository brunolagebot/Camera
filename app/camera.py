import cv2
import time
import multiprocessing

from app.queues import frame_queue

class CameraProcess(multiprocessing.Process):
    def __init__(self, rtsp_url: str):
        super().__init__()
        self.rtsp_url = rtsp_url
        self._stop_event = multiprocessing.Event()

    def run(self):
        cap = cv2.VideoCapture(self.rtsp_url)
        if not cap.isOpened():
            print(f"Erro ao abrir stream: {self.rtsp_url}")
            return
        while not self._stop_event.is_set():
            ret, frame = cap.read()
            if not ret:
                time.sleep(0.1)
                continue
            if not frame_queue.full():
                frame_queue.put(frame)
        cap.release()

    def stop(self):
        self._stop_event.set() 