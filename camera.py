#!/usr/bin/env python3

import cv2
import time
from transfer_img import transfer

def make_picture():
    time.sleep(60.0)
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite('static/image.jpg', frame)

    cap.release()
    transfer()

while True:
    make_picture()