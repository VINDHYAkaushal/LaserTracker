# LaserTracker
 detect and track objects, lets sat a colored ball via webcam
# LaserTracker

A real-time computer vision project that tracks a colored object in a video and simulates a laser targeting system by overlaying a red dot. Built with Python and OpenCV, this project demonstrates object detection and tracking skills—perfect for computer vision enthusiasts or portfolio showcasing.

## Features
- Detects and tracks a red object (e.g., a bouncing ball) using HSV color space.
- Overlays a yellow circle around the object and a red dot at its center to simulate a laser.
- Saves the tracked output and mask as video files.

## Demo
Tested with ["Bouncing Red Ball"](https://www.youtube.com/watch?v=UL0ZOgN2SqY):
- **Input**: A red ball bouncing on a plain background.
- **Output**: Yellow circle tracks the ball, red dot marks its center.

*Download `output_tracked.avi` from Colab to see the result!*

## Prerequisites
- Python 3.x
- Dependencies: `opencv-python`, `numpy`
- For Colab: No local webcam needed; use a video file.

## Setup (Local)
1. **Clone the repo**:
   ```bash
   git clone https://github.com/yourusername/LaserTracker.git
   cd LaserTracker
