# Import the camera server
import cscore

# Import OpenCV and NumPy

import cv2
import numpy as np
# Initialize the camera capture
cam = cscore.UsbCamera("camera", 0)
cam.setResolution(640, 480)

# Initialize the camera server and publish the video stream
cs = cscore.CameraServer
output_stream = cs.putVideo("output", 640, 480)
output_stream.setPixelFormat(cscore.VideoMode.PixelFormat.kMJPEG)

# Initialize the human detection algorithm (here we use OpenCV's HOGDescriptor)
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Start the video capture loop
while True:
    # Capture a frame from the camera
    frame = np.zeros(shape=(480, 640, 3), dtype=np.uint8)
    cam.grabFrameNoTimeout(frame)
    if cam.getError() != "":
        print(cam.getError())

    # Apply the human detection algorithm to the frame
    found, _ = hog.detectMultiScale(frame)

    # Draw bounding boxes around the detected humans
    for (x, y, w, h) in found:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Publish the processed frame to the camera server
    output_stream.putFrame(frame)