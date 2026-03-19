# 🎭GradeMyMood

A real-time modular human emotion detection system that grades human-AI interaction based on facial expressions using YOLOv11.

## 📝 Description

This system doesn't just detect emotions; it understands the room. By identifying 7 key facial expressions (Happy, Sad, Angry, Disgust, Neutral, Surprise, Fear) in real-time, it calculates a dynamic interaction grade.

Positive expressions boost the score while negative ones lower it, providing immediate, actionable feedback for empathetic AI tutors, reactive UI/UX, or mood-based analytics.

Built with a threaded, non-blocking architecture, this project is designed as a modular building block. It handles the heavy computer vision math in the background so you can focus on building empathetic AI tutors, reactive UIs, or smart feedback loops.


## Prerequisites
Requires a basic installation of [Python](https://www.python.org/)

    python 3.11.4 or later

### Linux
    Install via your package manager(apt, rpm, pacman etc.).

### Windows/MacOS
>install from [python](https://www.python.org/)

## Getting Started

### Note(optional):-You may create a virtual environment or install the requirements systemwide.
### Create virtual environment:
```sh
python -m venv venv
```

### Activate virtual environment:

* Linux/Mac
```sh
source venv/bin/activate
```

* Windows
```sh
venv\Scripts\activate
```

### 📥 Installation

1. clone the repo
```sh
git clone https://github.com/DynamicLinker/grade-my-mood.git
```

2. Install Dependencies
```sh
pip install -r requirements.txt
```

#### (NOTE): You may use the program as-is via detect.py or utilize its Threaded Engine capabilities as a modular building block in your own Python projects.



## 🏗 Developer Integration (How to Use)

You can import the EmotionGrader class into your own project to add "Emotional Intelligence" with just a few lines of code.

```python
from grademymood import EmotionGrader
import time

# 1. Initialize the engine
grader = EmotionGrader(weights_path="weights/Emotion_Detection.pt", source=0)

# 2. Start the non-blocking background thread
grader.start()

# 3. Wait for the engine to synchronize with the hardware
while not grader.is_ready:
    time.sleep(0.1)

# 4. Access live data in your main loop
try:
    while grader.is_running:
        score, mood = grader.mood()
        print(f"Current State -> Grade: {score} | Mood: {mood}")
        time.sleep(0.5)
except KeyboardInterrupt:
    grader.stop()
```

## 🏃 Run the demo

* Linux/MacOS
```sh
python3 detect.py
```
* Windows
```sh
python detect.py
```

### Choose your input:
- Enter `0` for webcam
- Enter video file path (e.g., `video.mp4`)

### Controls:
- Press `q` to quit
- Press `r` to reset grade

That's it! The system will display your emotions with bounding boxes and update the grade in real-time.


---
## 👤 Author
**Ajitesh Chaurasia**

Second-year B.Tech CSE student at PSIT, focused on high-performance AI systems.
* 🏆 **AIR 75** | NCIIPC–AICTE Pentathon '25
* 💻 **Global Rank 1142** | TCS CodeVita 2025

**🔗 [Linkedin](https://www.linkedin.com/in/ajitesh-chaurasia/) | 🔗 [GitHub](https://github.com/DynamicLinker/)**