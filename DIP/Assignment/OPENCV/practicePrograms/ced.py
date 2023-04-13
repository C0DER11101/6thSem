# Canny edge detector
import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

#img=cv.imread('messi5.jpg', 0);
#img=cv.imread('sudoku.png', 0);
img=cv.imread('vehicle2.jpg', 0);

canny=cv.Canny(img, 100, 200); # first argument -> image source; second argument -> first threshold value; third argument -> second threshold value;



titles=['image', 'canny'];
images=[img, canny];

for i in range(2):
    plt.subplot(1, 2, i+1);
    plt.imshow(images[i], 'gray');
    plt.title(titles[i]);
    plt.xticks([]);
    plt.yticks([]);
    pass;
plt.show();
