from grademymood import EmotionGrader
import time

print("*" * 50)
print("EMOTION-BASED GRADING SYSTEM")
print("*" * 50)


print("\nVideo Source Options:")
print("  - Enter '0' for webcam")
print("  - Enter video file path (e.g., 'video.mp4')")
source_input = input("\nEnter video source: ").strip()


try:
    source = int(source_input)
except:
    source = source_input

grader = EmotionGrader(source=source)

grader.start()
print("Starting.")

while not grader.is_ready:
    time.sleep(0.1)

try:
    while grader.is_running:
        grade, mood = grader.mood()
        print(f"grade:{grade} | mood:{mood}")

    time.sleep(0.5)
        

except KeyboardInterrupt:
    grader.stop()
    print("Exiting...")


