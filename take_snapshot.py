#!/usr/bin/python
import time
import datetime
import cv2
import os

# Config
stream_url = '.stream'

# Determine save location
while True:
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    timeclock = now.strftime("%H-%M-%S")
    absolute_script_dir = os.path.dirname(os.path.realpath(__file__))
    save_dir = absolute_script_dir + '/snapshots/' + date
    save_path = save_dir + '/' + timeclock + '.jpg'

    # Capture frame from camera stream
    cap = cv2.VideoCapture(stream_url)
    ret, frame = cap.read()

    # Save frame as image
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    cv2.imwrite(save_path, frame)
    print("Photo made on" , date,"at",timeclock)
    time.sleep(60)

