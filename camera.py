import cv2
import time

def make_picture():
    cap = cv2.VideoCapture(0)

    # Capture frame
    ret, frame = cap.read()
    #time.sleep(60.0)
    if ret:
        cv2.imwrite('static/image.jpg', frame)

    cap.release()