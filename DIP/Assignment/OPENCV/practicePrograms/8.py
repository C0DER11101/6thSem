import cv2
import numpy as np

cap=cv2.VideoCapture(0);

while(True):
    ret, frame=cap.read();

    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV);

    cv2.imshow('Frame', hsv);

    if(cv2.waitKey(1)==ord('q')):
        break;

cap.release();
cv2.destroyAllWindows();
