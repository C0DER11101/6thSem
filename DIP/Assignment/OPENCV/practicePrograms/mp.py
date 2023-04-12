import cv2 as cv
from matplotlib import pyplot as plt

img=cv.imread('HappyFish.jpg', -1);
cv.imshow('image', img);


# matplotlib reads the image in rgb format, so the color of the image may be different from that of cv.imshow(); so we will convert img from BGR to RGB format so that the image appears the same color as cv.imshow().
img=cv.cvtColor(img, cv.COLOR_BGR2RGB);
plt.imshow(img);

#hide the x and y coordinates that are displayed in the cartesian plane where the image is displayed.
plt.xticks([]);
plt.yticks([]);
#--------------

plt.show();

cv.waitKey(0);
cv.destroyAllWindows();
