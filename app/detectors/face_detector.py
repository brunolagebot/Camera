import cv2
import time
import multiprocessing

from app.queues import frame_queue, output_queue

class DetectionProcess(multiprocessing.Process):
    def __init__(self):
        super().__init__()
        self._stop_event = multiprocessing.Event()
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )

    def run(self):
        while not self._stop_event.is_set():
            try:
                frame = frame_queue.get(timeout=1)
            except Exception:
                continue
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            ret, jpeg = cv2.imencode(".jpg", frame)
            if ret and not output_queue.full():
                output_queue.put(jpeg.tobytes())
            time.sleep(0.01)

    def stop(self):
        self._stop_event.set() 