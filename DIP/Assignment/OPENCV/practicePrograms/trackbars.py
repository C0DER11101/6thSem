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

switch='0:OFF\n1:ON';

cv.createTrackbar(switch, 'image', 0, 1, nothing);

while True:
    cv.imshow('image', img);


    if (cv.waitKey(1) & 0XFF) == ord('q'):
        break;
    # get the position/value set by you in the trackbar.
    b=cv.getTrackbarPos('B', 'image'); # first argument -> name of the trackbar for which you want to get the value; second argument -> name of the window in which this trackbar is present(i.e. it's the second argument given to createTrackbar()).
    g=cv.getTrackbarPos('G', 'image');
    r=cv.getTrackbarPos('R', 'image');
    s=cv.getTrackbarPos(switch, 'image');

    if(s==0):
        img[:]=0;
    else:
        img[:]=[b, g, r];

cv.destroyAllWindows();
