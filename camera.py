#!/usr/bin/env python

import cv2
import time

def make_picture():
    time.sleep(60.0)
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite('static/image.jpg', frame)

    cap.release()

while True:
    make_picture()