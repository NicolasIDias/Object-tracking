# CSRT Object Tracking

## Overview

This software implements object tracking using the CSRT (Discriminative Correlation Filter with Channel and Spatial Reliability) algorithm. It leverages the Histogram of Oriented Gradients (HOG) for feature extraction and performs tracking based on the object's appearance in a video.

## Features

- **CSRT Tracking**: Utilizes the CSRT tracker from OpenCV for accurate object tracking.
- **HOG Feature Extraction**: Extracts useful information from the image to enhance tracking performance.
- **Error Handling**: Handles errors such as video loading failures and tracking errors.

## Requirements

- Python 3.x
- OpenCV (cv2)

## Installation

1. Install Python 3.x from the [official website](https://www.python.org/downloads/).
2. Install OpenCV using pip:

   ```bash
   pip install opencv-python

## Usage

1. Place your video file in the Video directory and name it rua.mp4, or adjust the filename in the script accordingly.

2. Run the script:

     ```bash
     tracker.py
