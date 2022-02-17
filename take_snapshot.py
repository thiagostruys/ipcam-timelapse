#!/usr/bin/python


# Credit to Tom Catullo https://github.com/Tom25 for starting this project.

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
    
    #Put conditions from weewx onto image

    datafile = open(filename)
    conditions = datafile.read()


    position = (10,1750)
    cv2.putText(
        frame, #numpy array on which text is written
        (conditions), #text
        position, #position at which writing has to start
        cv2.FONT_HERSHEY_COMPLEX, #font family
        1.5, #font size
        (255,255,255), #font color
        3) #font stroke

    datafile.close()
    
    # Save frame as image
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    cv2.imwrite(save_path, frame)
    print("Photo made on" , date,"at",timeclock)
    time.sleep(60)

