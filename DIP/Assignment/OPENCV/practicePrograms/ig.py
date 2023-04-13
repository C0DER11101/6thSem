import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img =cv.imread('sudoku.png', 0);

# Laplacian gradient of an image!!
lap=cv.Laplacian(img, cv.CV_64F, ksize=3); # first argument -> image; second argument -> data type which we are going to use; third argument(optional) -> kernel size
lap=np.uint8(np.absolute(lap)); # converting the absolute value of laplacian image transformation into unsigned 8 bit integer which is suitable for our output.
#------------------

#SobelX and SobelY methods(they are also called sobel gradient representation).

sobelX=cv.Sobel(img, cv.CV_64F, 1, 0); #first argument -> image; second argument -> cv.CV_64F; third argument -> dx(can be 1 or 0), when dx=1 that means we want to use the sobelX method, when dx=0 that means we want to use the sobelY method; fourth argument -> dy(can be 0 or 1) dy=1 means that we want to use sobelY method, dy=0 meant that we want to use the sobelX method; fifth argument(optional) -> kernel size.
sobelX=np.uint8(np.absolute(sobelX)); # converting the absolute value of sobelX image into unsigned 8 bit integer which is suitable for our output.

sobelY=cv.Sobel(img, cv.CV_64F, 0, 1);
sobelY=np.uint8(np.absolute(sobelY)); # converting the absolute value of sobelY image into unsigned 8 bit integer which is suitable for our output.


# combining the intensities of sobelX and sobelY images
sobelComb=cv.bitwise_or(sobelX, sobelY);

titles=['image', 'Laplacian', 'sobelX', 'sobelY', 'sobel combined'];
images=[img, lap, sobelX, sobelY, sobelComb];

for i in range(5):
    plt.subplot(2, 3, i+1);
    plt.imshow(images[i], 'gray');

    plt.title(titles[i]);
    plt.xticks([]);
    plt.yticks([]);
    pass;

plt.show();
