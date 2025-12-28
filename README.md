# 🎭GradeMyMood

A real-time emotion detection system that grades human-AI interaction based on facial expressions using YOLOv11.

## Description

This system detects emotions (happy, sad, angry, disgust, neutral, surprise, fear) in real-time and updates a grade instantly. Positive emotions boost the grade while negative emotions lower it, providing immediate feedback for human-AI interaction scenarios.


## Prerequisites
Requires a basic installation of [Python](https://www.python.org/)

    python 3.11.4 or later

### Linux
    Install via your pacakge manager(apt, rpm, pacman etc.).

### Windows/MacOS
>install from [python](https://www.python.org/)

## Getting Started

### Note(optional):-You may create a virtual environment or install the requirements systemwide.
### Create virtual environment:
```sh
python -m venv venv
```

### Activate virtual environment:

Linux/Mac
```sh
source venv/bin/activate
```

Windows
```sh
venv\Scripts\activate
```

### Installation

1. clone the repo
```sh
git clone https://github.com/DynamicLinker/Emotions_Detector.git
```

#### (NOTE) You may use the program as is or utilize its capabilities in your own Project.

2. Install Dependencies
```sh
pip install -r requirements.txt
```
3. Run

Linux/MacOS
```sh
python3 detect.py
```
Windows
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