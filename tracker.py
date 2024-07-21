"""

CSRT Algorithm (Discrimiative correlation filter with channel and spatial reliability)

HOG: extracts useful information from the image
  Calculate the probability of the object appearing in the next frame -> random Markov test

"""

import cv2

# Test the import of OpenCV and check the version
# print(cv2.__version__)

# Create the CSRT Tracker
tracker = cv2.TrackerCSRT.create()

# Load the video
content = cv2.VideoCapture('Video/rua.mp4')

# Check if the video was loaded correctly
if not content.isOpened():
    print("Error opening video.")
    exit()

# Read the first frame of the video
load, frame = content.read()  # "read" the video and returns (load: boolean) (Frame: 1st frame of the video)
if not load:
    print("Error reading the first frame.")
    exit()

# Create the Region Of Interest (ROI) to be tracked in the video
roi = cv2.selectROI(frame)  # Creates the Region Of Interest to be tracked in the video
# print(roi) returns the position of ROI and its size

# Initialize the tracker with the frame and the ROI
load = tracker.init(frame, roi)
print(load)

while True:
    load, frame = content.read()
    if not load:
        break
    load, roi = tracker.update(frame)
    # print(roi) Object location
    # (660, 515, 90, 312) EXAMPLE

    if load:
        (x, y, w, h) = [int(v) for v in roi]
        """
        Assigns the values from the roi tuple to the variables x, y, w, and h. The values are extracted from the 
        roi tuple and converted to integers before being assigned to the variables.
        EXAMPLE:
        (660, 515, 90, 312)
        x=660, y=515, w=90, h=312 
        """


        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255, 0), 2, 1)
    else:
        cv2.putText(frame, "Tracking failed", (400, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 5)
        """
        Displays tracking failed when the object exits the video
        """

    cv2.imshow("tracker", frame)
    if cv2.waitKey(1) & 0x0ff == 27:  # if ESC pressed the program will stop
        break

