import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#img=cv.imread('vehicle2.jpg');
img=cv.imread('detect_blob.png');

img=cv.cvtColor(img, cv.COLOR_BGR2RGB);

kernel=np.ones((5, 5), np.float32)/25; # defining the kernel for homogeneous filtering!!

# defining the destination image using the kernel
dst=cv.filter2D(img, -1, kernel); # first argument -> image; second argument -> desired depth of the destination image; third argument -> kernel.

#The averaging algorithm(blur).
blur=cv.blur(img, (5, 5)); # first argument -> image; second argument -> kernel(the dimensions of the kernel inside tuple).

#The Gaussian filter algorithm
"""
Gaussian filter is nothing but using different-weight-kernel, in both x and y direction.
Pixels located at the center have the higher weight. It removes high frequency noise from an image.
"""

gblur=cv.GaussianBlur(img, (5, 5), 0); # first two arguments are the same as blur(); it takes a third argument called sigmaX value;


#Median filter
"""
Median filter is something that replaces each pixel's value with the median of its neighboring pixels. This method is great when dealing with salt-and-pepper noise.
"""

median=cv.medianBlur(img, 5); # first argument -> image; second argument -> kernel size which should be odd(except 1);

#Bilateral filter
"""
Bilateral filter is highly effective in noise removal while keeping the edge sharp!!
"""

bflt=cv.bilateralFilter(img, 9, 75, 75); # first argument -> image; second argument -> diameter of each pixel neighborhood that is used during the filter; third argument -> sigma color; fourth argument -> sigma space;

titles=['image', '2D convolution', 'blur', 'Gaussian Blur', 'median', 'bilateral filter'];
images=[img, dst, blur, gblur, median, bflt];

for i in range(6):
    plt.subplot(3, 3, i+1);
    plt.imshow(images[i], 'gray');
    plt.title(titles[i]);
    plt.xticks([]);
    plt.yticks([]);
    pass;
plt.show();
