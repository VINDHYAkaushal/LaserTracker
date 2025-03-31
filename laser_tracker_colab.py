# Install the libraries we need: OpenCV for computer vision and NumPy for math stuff
!pip install opencv-python numpy

# Import the tools we'll use
import cv2  
import numpy as np  
from google.colab import files 
from IPython.display import HTML, display, Image  
import base64  

# Define a function to process our video and track the red ball
def process_video(video_path, output_path='output_tracked.avi', mask_output_path='output_mask.avi'):
    # Open the video file we uploaded
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")  #  the video didn’t load
        return

    # Get the video’s size and speed so we can save the output correctly
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # Width in pixels
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # Height in pixels
    fps = int(cap.get(cv2.CAP_PROP_FPS))  # Frames per second

    # Set up writers to save our processed videos
    fourcc = cv2.VideoWriter_fourcc(*'XVID') 
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height)) 
    mask_out = cv2.VideoWriter(mask_output_path, fourcc, fps, (frame_width, frame_height), isColor=False)  # For the mask (black and white)

    # Define the color range to detect the red ball in HSV (Hue, Saturation, Value)
    # Red can show up in two ranges, so we check both
    lower_red1 = np.array([0, 100, 100])    # Lower red range start
    upper_red1 = np.array([20, 255, 255])   # Lower red range end
    lower_red2 = np.array([160, 100, 100])  # Upper red range start (red wraps around in HSV)
    upper_red2 = np.array([180, 255, 255])  # Upper red range end

    # Show the HSV ranges we’re using so we can tweak them if needed
    print(f"Using HSV ranges: Lower1={lower_red1}, Upper1={upper_red1}, Lower2={lower_red2}, Upper2={upper_red2}")

    # Grab the first frame to show what we’re working with
    ret, frame = cap.read()  # Read the first frame
    if ret:  # If we got a frame successfully
        cv2.imwrite("first_frame.jpg", frame)  # Save it as an image
        display(Image(filename="first_frame.jpg"))  # Show it in Colab
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Rewind the video to the start

    frame_count = 0  # Keep track of how many frames we process
    while True:  # Loop through every frame in the video
        ret, frame = cap.read()  # Get the next frame
        if not ret:  # If there are no more frames, stop
            break

        # Convert the frame to HSV so we can detect colors
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Create masks to find the red ball in both red ranges
        mask1 = cv2.inRange(hsv, lower_red1, upper_red1)  # Check lower red range
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)  # Check upper red range
        mask = cv2.bitwise_or(mask1, mask2)  # Combine them to catch all reds
        mask = cv2.erode(mask, None, iterations=2)  # Clean up small noise
        mask = cv2.dilate(mask, None, iterations=2)  # Fill in gaps

        # Find the outlines of the red stuff in the mask
        contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if contours:  # If we found any shapes
            largest_contour = max(contours, key=cv2.contourArea)  # Pick the biggest one (probably the ball)
            ((x, y), radius) = cv2.minEnclosingCircle(largest_contour)  # Get its center and size
            if radius > 10:  # Only draw if it’s big enough (not tiny noise)
                cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)  # Yellow circle around the ball
                cv2.circle(frame, (int(x), int(y)), 5, (0, 0, 255), -1)  # Red dot in the center (laser)

        out.write(frame)  # Save the frame with circles to the tracked video
        mask_out.write(mask)  # Save the mask to its video
        frame_count += 1  # Count this frame

    # Clean up when we’re done
    cap.release()  
    out.release()  
    mask_out.release()  
    print(f"Processed {frame_count} frames.")  
    print(f"Tracked video saved as {output_path}")  
    print(f"Mask video saved as {mask_output_path}") 

# Let the user upload their video
uploaded = files.upload()  
video_file = list(uploaded.keys())[0]  # Grab the name of the uploaded file, like 'Bouncing Red Ball.mp4'

# Run the video processing function
process_video(video_file)

# Show what files are in the Colab folder to make sure everything saved
!ls -lh /content/

# Download the results to our computer
files.download('output_tracked.avi')  # The video with the yellow circle and red dot
files.download('output_mask.avi')  # The video showing what we detected
files.download('first_frame.jpg')  # The first frame we looked at

# Try to show the videos in Colab (might not always work, but worth a shot)
def display_video(file_path, label="Video"):
    video_file = open(file_path, "rb").read()  # Read the video file
    video_url = f"data:video/mp4;base64,{base64.b64encode(video_file).decode()}"  # Turn it into a web-friendly format
    return HTML(f"""<div><h3>{label}</h3><video width=400 controls><source src="{video_url}" type="video/mp4"></video></div>""")

# Display the results if possible
display_video('output_tracked.avi', "Tracked Video")
display_video('output_mask.avi', "Mask Video")
