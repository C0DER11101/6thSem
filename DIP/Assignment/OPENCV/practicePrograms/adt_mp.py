import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img=cv.imread('gradient.png', 0);

_, th1=cv.threshold(img, 50, 255, cv.THRESH_BINARY);
_, th2=cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV);
_, th3=cv.threshold(img, 127, 255, cv.THRESH_TRUNC);
_, th4=cv.threshold(img, 127, 255, cv.THRESH_TOZERO);
_, th5=cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV);

titles=['Original image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV'];

images=[img, th1, th2, th3, th4, th5];

for i in range(6):
    plt.subplot(2, 3, i+1); # first argument -> number of rows; second argument -> number of columns; third argumet -> index(in our case it will be the index of the image).

    """
    subplot()
    creates a subplot inside a main plot.
    """
    plt.imshow(images[i], 'gray');
    plt.title(titles[i]);

    """
    title()
    provides titles to each of those subplots.
    """

    plt.xticks([]);
    plt.yticks([]);
    pass;

plt.show();
