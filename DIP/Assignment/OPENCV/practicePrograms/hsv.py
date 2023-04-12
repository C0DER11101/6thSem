import cv2
import numpy as np

def nothing(x):
    pass;

cv2.namedWindow('Tracking');

cap=cv2.VideoCapture(0);

#Lower Hue, Saturation and Value
cv2.createTrackbar('LH', 'Tracking', 0, 255, nothing);
cv2.createTrackbar('LS', 'Tracking', 0, 255, nothing);
cv2.createTrackbar('LV', 'Tracking', 0, 255, nothing);

#Upper Hue, Saturation and Value
cv2.createTrackbar('UH', 'Tracking', 255, 255, nothing);
cv2.createTrackbar('US', 'Tracking', 255, 255, nothing);
cv2.createTrackbar('UV', 'Tracking', 255, 255, nothing);


while True:
    _, frame=cap.read();

    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV);


    l_h=cv2.getTrackbarPos('LH', 'Tracking');
    l_s=cv2.getTrackbarPos('LS', 'Tracking');
    l_v=cv2.getTrackbarPos('LV', 'Tracking');

    u_h=cv2.getTrackbarPos('UH', 'Tracking');
    u_s=cv2.getTrackbarPos('US', 'Tracking');
    u_v=cv2.getTrackbarPos('UV', 'Tracking');

    lower_blue=np.array([l_h, l_s, l_v]); # light blue
    upper_blue=np.array([u_h, u_s, u_v]); # dark blue

    #lower_blue=np.array([110, 50, 50]); # light blue
    #upper_blue=np.array([130, 255, 255]); # dark blue

    mask=cv2.inRange(hsv, lower_blue, upper_blue); # thresholding the hsv image to get the blue color

    result=cv2.bitwise_and(frame, frame, mask=mask);

    cv2.imshow("frame", frame);
    cv2.imshow("mask", mask);
    cv2.imshow("result", result);

    if((cv2.waitKey(1) & 0xFF)==ord('q')):
        break;


cap.release();
cv2.destroyAllWindows();
