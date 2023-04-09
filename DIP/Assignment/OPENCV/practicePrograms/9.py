# corner detection algorithm(Shi-Tomasi).

import cv2
import numpy as np

img=cv2.imread('left12.jpg');

# converting the image to grayscale image is necessary for the algorithm to work!!
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);


corners=cv2.goodFeaturesToTrack(gray, 100, 0.01, 10);


"""
arguments in goodFeaturesToTrack()

img -> source image.
100 -> number of corners.
0.01 -> degree of confidence.
10 -> minimum Euclidean distance.
"""

corners=np.int0(corners); # converting the floating values in corners into integers

for corner in corners:
    x, y=corner.ravel();
    cv2.circle(img, (x, y), 5, (255, 0, 0), -1);
cv2.imshow('frame', img);
cv2.waitKey(0);
cv2.destroyAllWindows();
