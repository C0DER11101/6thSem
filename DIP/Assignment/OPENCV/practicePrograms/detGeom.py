# detect simple geometrical shapes

import cv2 as cv
import numpy as np

img=cv.imread('shapes.png');
imgray=cv.cvtColor(img, cv.COLOR_BGR2GRAY);

# find the threshold
_, thresh=cv.threshold(imgray, 240, 255, cv.THRESH_BINARY);

# finding the contours
contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE);


for contour in contours:
    """ arcLength() calculates a contour's parameter or a curve length."""
    approx=cv.approxPolyDP(contour, 0.01*cv.arcLength(contour, True), True); # this method approximates a polygon and curve with a specific precision.
    """
    approxPolyDP()
    first argument -> contour
    second argument -> epsilon: it's a parameter specifying the approximation accuracy.
    third argument -> a boolean asking if the contour is closed or opened(this is the same argument that we have passed to arcLength()'s second argument.
    """

    cv.drawContours(img, [approx], 0, (0, 0, 0), 5); # 0 because it's in a loop and we will work only with one contour at a time.

    x=approx.ravel()[0];
    y=approx.ravel()[1];

    if(len(approx))==3:
        cv.putText(img, "Triangle", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0));

    elif(len(approx))==4:
        x1, y1, w, h = cv.boundingRect(approx);
        aspectRatio=float(w)/h;
        print(aspectRatio);

        if(aspectRatio >=0.95 and aspectRatio <=1.05):
           cv.putText(img, "Square", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0));
        else:
           cv.putText(img, "Rectangle", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0));

    elif(len(approx))==5:
        cv.putText(img, "Pentagon", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0));

    elif(len(approx))==10:
        cv.putText(img, "Star", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0));

    else:
        cv.putText(img, "Circle", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0));


cv.imshow('shapes', img);
cv.waitKey(0);
cv.destroyAllWindows();
