import cv2
import numpy as np

# creating an image using numpy zeros() method

img=np.zeros([512, 512, 3], np.uint8);
""" arguments in zeros()

512 -> height of the image.
512 -> width of the image.
3 -> number of channels.
uint8 -> unsigned integer 8 bits.
"""

cv2.imshow('Image', img);

cv2.waitKey(0);
cv2.destroyAllWindows();