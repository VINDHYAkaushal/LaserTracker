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

Open the Colab notebook: (Paste the code above into Colab).
Upload a video (e.g., Bouncing Red Ball.mp4 from YouTube).
Run the cell to process and download:
output_tracked.avi: Tracked video.
output_mask.avi: Detection mask.
Adjust HSV ranges in the code if needed for different colors.
How It Works
Converts video frames to HSV for color detection.
Uses contour detection to track the largest object in the specified range.
Overlays a yellow circle and red dot on the tracked object.
Results
Test Video: Successfully tracks a red ball with HSV ranges:
Lower1: [0, 100, 100], Upper1: [20, 255, 255]
Lower2: [160, 100, 100], Upper2: [180, 255, 255]
Output saved locally via Colab downloads.
Future Enhancements
Add multi-object tracking.
Integrate with real laser hardware.
Use ML models (e.g., YOLO) for complex objects.
