import cv2
import time
import multiprocessing

class DetectionProcess(multiprocessing.Process):
    def __init__(self, frame_queue, output_queue):
        super().__init__()
        self._stop_event = multiprocessing.Event()
        self.frame_queue = frame_queue
        self.output_queue = output_queue
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )

    def run(self):
        while not self._stop_event.is_set():
            try:
                frame = self.frame_queue.get(timeout=1)
            except Exception:
                continue
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            ret, jpeg = cv2.imencode(".jpg", frame)
            if ret and not self.output_queue.full():
                self.output_queue.put(jpeg.tobytes())
            time.sleep(0.01)

    def stop(self):
        self._stop_event.set() 