# Simple Image Thresholding!!
import cv2 as cv
import numpy as np

img=cv.imread('gradient.png', 0);


_, th1=cv.threshold(img, 50, 255, cv.THRESH_BINARY); # first argument -> source image; second argument -> threshold value; third argument -> maximum threshold value; fourth argument -> threshold type;
_, th2=cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV); # THRESHOLD BINARY INVERSE(Opposite of THRESH_BINARY).
_, th3=cv.threshold(img, 127, 255, cv.THRESH_TRUNC);
_, th4=cv.threshold(img, 127, 255, cv.THRESH_TOZERO);
_, th5=cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV);

"""threshold types
1. THRESH_BINARY.
"""

"""
What we are doing:
cv.threshold() basically compares each pixel value to check whether it lies between 50 and 255, if the value lies between 50 and 255 then the resultant image has 1 in it and if the value doesn't lie between 50 and 255 then a 0 is put in the resultant image.
That's why we see two halves(black half and white half) on the thresholded image th1. Also, hence the name THRESH_BINARY.
"""

"""
THRESH_TRUNC
cv.threshold(img, 200, 255, cv.THRESH_TRUNC)

Here, the pixel values till 200 will remain unchanged and theh pixel values after 200(threshold value) will become 200 and will remain that way.
"""

"""
THRESH_TOZERO
cv.threshold(img, 127, 255, cv.THRESH_TOZERO)

When the pixel value is less than the threshold value(127 here), then 0 will be assigned to that pixel.

When the pixel value is greater than the threshold value then the pixel value will be unchanged.

The vice-versa of this is THRESH_TOZERO_INV.
"""


cv.imshow('image', img);
cv.imshow('th1', th1);
cv.imshow('th2', th2);
cv.imshow('th3', th3);
cv.imshow('th4', th4);
cv.imshow('th5', th5);

cv.waitKey(0);
cv.destroyAllWindows();
