# Adaptive thresholding

import cv2 as cv
import numpy as np

img=cv.imread('sudoku.png', 0);

cv.imshow('image', img);

_, th1=cv.threshold(img, 127, 255, cv.THRESH_BINARY);

th2=cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2); # first argument -> source image; second argument -> maximum value non-zero value assigned to the pixels for which the condition is satisfied(max value of a pixel = 255); third argument -> adaptive method which decides how the the thresholding value is calculated; fourth argument -> threshold type; fifth argument -> block size which decides the size of the neighborhood; sixth argument -> value of C

th3=cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2);

cv.imshow('th1', th1);
cv.imshow('th2', th2);
cv.imshow('th3', th3);

cv.waitKey(0);
cv.destroyAllWindows();
