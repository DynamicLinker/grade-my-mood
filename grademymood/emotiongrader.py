import threading
from ultralytics import YOLO
import cv2

class EmotionGrader:
    def __init__(self, source = 0, weights_path = "weights/Emotion_Detection.pt", verbose = False):
        self.source = source
        self.weights_path = weights_path
        self.verbose = verbose
        self.model = YOLO(weights_path)
        self.grade = 50
        self.last_mood = "neutral"
        self.is_running = False
        self.is_ready = False

        self.emotion_points = {
            'happy': +0.5,
            'surprise': +0.2,
            'neutral': 0.0,
            'sad': -0.2,
            'anger': -0.5,
            'disgust': -0.5,
            'fear': -0.3
            }
        
        self.colors = {
            'happy': (0, 255, 0), 
            'surprise': (255, 0, 255),
            'neutral': (255, 255, 0), 
            'sad': (255, 0, 0),
            'anger': (0, 0, 255),
            'disgust': (0, 100, 255),
            'fear': (128, 0, 128)
            }
        
    
    def _internal_loop(self):

        cap = cv2.VideoCapture(self.source)

        while self.is_running:
            ret, frame = cap.read()
            
            if not ret: 
                break

            results = self.model(frame, imgsz = 640, conf=0.5, verbose=self.verbose)

            if not self.is_ready:
                self.is_ready = True
                
            for result in results:
                for box in result.boxes:
                    emotion = self.model.names[int(box.cls[0])]

                    self.last_mood = emotion
                    
                    change = 0.2 * self.emotion_points.get(emotion.lower(), 0)
                    self.grade = max(0, min(100, self.grade + change))

                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    color = self.colors.get(emotion.lower(), (255, 255, 255))
                    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 3)
            
            cv2.putText(frame, f"GRADE: {int(self.grade)}", (20, 55), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 215, 255), 2)
            
            cv2.imshow('Emotion Grading Engine', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.is_running = False
        cap.release()
        cv2.destroyAllWindows()

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.is_ready = False

            thread = threading.Thread(target=self._internal_loop, daemon=True)
            thread.start()
            print("🚀 Emotion Engine started in background.")

    def mood(self):
        return int(self.grade), self.last_mood

    def stop(self):
        self.is_running = False