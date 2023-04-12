import cv2
import numpy as np

cv2.namedWindow("Tracking");

cv2.

while True:
    frame=cv2.imread('smarties.png');

    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV);

    lower_blue=np.array([110, 50, 50]);
    upper_blue=np.array([130, 255, 255]);

    mask=cv2.inRange(hsv, lower_blue, upper_blue);

    result=cv2.bitwise_and(frame, frame, mask=mask);

    cv2.imshow("frame", frame);
    cv2.imshow("mask", mask);
    cv2.imshow("result", result);

    if((cv2.waitKey(1) & 0xFF)==ord('q')):
        break;


cv2.destroyAllWindows();
