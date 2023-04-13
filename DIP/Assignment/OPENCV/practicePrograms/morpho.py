import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

img=cv.imread('smarties.png', 0);

_, mask=cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV);

kernel=np.ones((3, 3), np.uint8); # a kernel of dimensions 3x3 containing only ones.
"""
np.ones()
first argument -> size of the matrix.
second argument -> data type of each element in the kernel.
"""

# Morphological transformations.
dilation=cv.dilate(mask, kernel, iterations=2); # first argument -> mask(source image); second argument -> kernel; third argument(optional) -> number of iterations.

erosion=cv.erode(mask, kernel, iterations=1); # first argument -> mask(source image); second argument -> kernel; third argument(optional) -> number of iterations.

opening=cv.morphologyEx(mask, cv.MORPH_OPEN, kernel); # first argument -> source image(here: mask); second argument -> type of morphological operation that we want to perform; third argument -> kernel

"""
Opening is just another form of erosion followed by dilation.
First erosion is performed. Then dilation is performed.
"""

closing=cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel);

"""
Closing.
First dilation is performed. Then erosion is performed.
"""
#-------------------------------------------------------------------------------------------------------------------------

titles=['image', 'mask', 'dilation', 'erosion', 'opening', 'closing'];
images=[img, mask, dilation, erosion, opening, closing];


for i in range(6):
    plt.subplot(3, 3, i+1);
    plt.imshow(images[i], 'gray');
    plt.title(titles[i]);
    plt.xticks([]);
    plt.yticks([]);
    pass;

plt.show();
