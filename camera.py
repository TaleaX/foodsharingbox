#!/usr/bin/env python3

import cv2
import time
from transfer_img import transfer
from scipy import ndimage

def make_picture():
    time.sleep(2.0)
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite('/home/pi/foodsharingbox/static/image.jpg', frame)
        img = cv2.imread('/home/pi/foodsharingbox/static/image.jpg')
        rotated = ndimage.rotate(img, 180)
        cv2.imwrite('/home/pi/foodsharingbox/static/image.jpg', rotated)

    cap.release()
    transfer()

while True:
    make_picture()