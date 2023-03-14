# Import the camera server
import cscore

# Import OpenCV and NumPy
import cv2
import numpy as np


# Initialize the camera server and publish the video stream
cs = cscore.CameraServer
cam = cs.startAutomaticCapture(1)
cam.setResolution(320, 240)

# Create a CvSink object and set it to grab frames from the camera server
cv_sink = cs.getVideo()
cv_sink.setSource(cam)

# Initialize the video stream output and set the pixel format to MJPEG
output_stream = cs.putVideo("output", 320, 240)
output_stream.setPixelFormat(cscore.VideoMode.PixelFormat.kBGR)

# Initialize the human detection algorithm (here we use OpenCV's HOGDescriptor)
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Start the video capture loop
while True:
    # Create an empty numpy.ndarray to store the grabbed frame
    frame = np.zeros(shape=(480, 640, 3), dtype=np.uint8)

    # Grab a frame from the camera server using the CvSink object
    _, frame = cv_sink.grabFrame(frame)

    # Apply the human detection algorithm to the frame
    found, _ = hog.detectMultiScale(frame)

    # Draw bounding boxes around the detected humans
    for (x, y, w, h) in found:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Publish the processed frame to the camera server
    output_stream.putFrame(frame)
