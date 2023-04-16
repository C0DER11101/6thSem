import cv2 as cv
import numpy as np
import pytesseract as pts

img=cv.imread('vehicle.jpg');

cv.imshow('image', img);

cv.waitKey(0) & 0xFF;

cv.destroyAllWindows();
