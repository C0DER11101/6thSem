# colors and color detection

# HSV: Hue Saturation and Lightness/Brightness

import cv2
import numpy as np

cap=cv2.VideoCapture(0);

while(True):
    ret, frame=cap.read();

    width=int(cap.get(3));
    height=int(cap.get(4));

    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV); # converts the frame captured into hsv colored image

    # colors that we want to extract!!
    lower_blue=np.array([110, 50, 50]); # light blue
    upper_blue=np.array([130, 255, 255]); # dark blue

    #lower_blue=np.array([230, 216, 173]); # light blue
    #upper_blue=np.array([255, 0, 0]); # dark blue

    mask=cv2.inRange(hsv, lower_blue, upper_blue); # returns a new image/a mask that has only the blue pixels in it.

    result=cv2.bitwise_and(frame, frame, mask=mask);
    """
    arguments in cv2.bitwise_and()
    frame: -> first source image.
    frame: -> second source image(here its same as first source image, normally it will be different).
    mask: -> the mask that we just calculated.

    description:
    this function basically perform bitwise AND operation on both the first the second source images and it will use the mask to determine which pixels to keep(in our case it will keep all the blue pixels).
    """

    #cv2.imshow('Frame', frame);
    cv2.imshow('Detect', result);
    #cv2.imshow('mask', mask);

    if(cv2.waitKey(1)==ord('q')):
        break;


cap.release();
cv2.destroyAllWindows();
