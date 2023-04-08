import cv2
import random

img=cv2.imread('HappyFish.jpg', -1);

tag=img[50:120, 45:100];
img[10:80, 20:75]=tag;

cv2.imshow('Image', img);
cv2.waitKey(0);
cv2.destroyAllWindows();
