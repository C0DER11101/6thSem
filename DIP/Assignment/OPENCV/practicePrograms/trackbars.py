# trackbars in opencv

"""
trackbars are useful whenever you want to change some values in your image at runtime.
"""

import cv2 as cv
import numpy as np

def nothing(x):
    print(x);


img=np.zeros((300, 512, 3), np.uint8);

# this method can be used to create a window with a name!!
cv.namedWindow('image');

# creating a trackbar

# use the method createTrackbar()
cv.createTrackbar('B', 'image', 0, 255, nothing); # first argument -> trackbar name, second argument -> name of the window, third argument -> initial value at which your trackbar is set, fourth argument -> the count(final value that we want to set for the trackbar), fifth argument -> callback function that will be called whenever your trackbar value changes
cv.createTrackbar('G', 'image', 0, 255, nothing);
cv.createTrackbar('R', 'image', 0, 255, nothing);

while True:
    cv.imshow('Image', img);

    if (cv.waitKey(0) & 0Xff) == ord('q'):
        break;

cv.destroyAllWindows();
