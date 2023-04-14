import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img=cv.imread('opencv-logo-white.png');
imgray=cv.cvtColor(img, cv.COLOR_BGR2GRAY);

_, thresh=cv.threshold(imgray, 127, 255, cv.THRESH_BINARY);

contours, hierarchy=cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE); # first argument -> thresh; second argument -> contour retrieval mode; third argument -> contour approximation method;

"""
contours is a python list of all the contours in the image. Each individual contour is a numpy array of (x, y) coordinates of boundary points of the object.
"""

print(f"Number of contours: {len(contours)}\n");

# drawing the contours!!
cv.drawContours(img, contours, -1, (0, 255, 0), 3); # first argument -> original image; second argument -> contours; third argument -> contour indices(if -1 is given in this argument then it will draw all the contours; fourth argument -> color(inside of tuple); fifth argument -> thickness;

cv.imshow('image', img);
cv.imshow('gray image', imgray);
cv.waitKey(0);
cv.destroyAllWindows();
