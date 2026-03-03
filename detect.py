from ultralytics import YOLO
import cv2


def update_grade(current_grade, emotion, emotion_points):

    emotion = emotion.lower()
    
    if emotion in emotion_points:
        current_grade += emotion_points[emotion]
        
        if current_grade > 100:
            current_grade = 100
        if current_grade < 0:
            current_grade = 0
    
    return current_grade


def get_emotion_color(emotion, colors):

    return colors.get(emotion.lower(), (255, 255, 255))


def main():
    print("*" * 50)
    print("EMOTION-BASED GRADING SYSTEM")
    print("*" * 50)
    

    weights_path = '../weights/Emotion_Detection_v1.0.pt'
    
    print("\nVideo Source Options:")
    print("  - Enter '0' for webcam")
    print("  - Enter video file path (e.g., 'video.mp4')")
    source_input = input("\nEnter video source: ").strip()
    
    
    try:
        source = int(source_input)
    except:
        source = source_input
    

    grade = 50
    
    emotion_points = {
        'happy': +2,
        'surprise': +1,
        'neutral': 0,
        'sad': -1,
        'angry': -2,
        'disgust': -2,
        'fear': -1
    }
    
    colors = {
        'happy': (0, 255, 0),
        'surprise': (255, 0, 255),
        'neutral': (255, 255, 0),
        'sad': (255, 0, 0),
        'angry': (0, 0, 255),
        'disgust': (0, 100, 255),
        'fear': (128, 0, 128)
    }
    

    try:
        model = YOLO(weights_path)
        model.to('cpu')
        print("Model loaded successfully!")
    except Exception as e:
        print(f"Error loading model: {e}")
        return
    
    print(f"Opening video source: {source}")
    cap = cv2.VideoCapture(source)
    
    if not cap.isOpened():
        print(f"Error: Could not open video source '{source}'")
        return
    
    print("\n" + "=" * 50)
    print("SYSTEM STARTED")
    print("=" * 50)
    print("Controls:")
    print("  - Press 'q' to quit")
    print("  - Press 'r' to reset grade to 50")
    print("=" * 50 + "\n")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Video ended or failed to read frame")
            break
        

        results = model(frame, conf=0.5, verbose=False, device='cpu', imgsz=640)
        
    
        for result in results:
            for box in result.boxes:
            
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                confidence = float(box.conf[0])
                emotion = model.names[int(box.cls[0])]
              
                grade = update_grade(grade, emotion, emotion_points)
                
            
                color = get_emotion_color(emotion, colors)
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 3)
                
            
                label = f"{emotion} ({confidence:.2f})"
                cv2.putText(frame, label, (x1, y1-10), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
        
        
        cv2.rectangle(frame, (0, 0), (frame.shape[1], 80), (0, 0, 0), -1)
        
        
        grade_text = f"GRADE: {int(grade)}"
        cv2.putText(frame, grade_text, (20, 55), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1.8, (255, 255, 255), 4)
        
        
        cv2.imshow('Emotion Grading', frame)
        
        
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            print(f"\nFinal Grade: {int(grade)}")
            break
        elif key == ord('r'):
            grade = 50
            print("Grade reset to 50")
    
    
    cap.release()
    cv2.destroyAllWindows()
    print("\nExiting")


if __name__ == "__main__":
    main()
