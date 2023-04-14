import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

cap=cv.VideoCapture('people.mp4');

_, frame1=cap.read();
_, frame2=cap.read();

while cap.isOpened():
    diff=cv.absdiff(frame1, frame2); # finds the absolute difference between frame1 and frame2.

    # converting the difference to grayscale mode
    gray=cv.cvtColor(diff, cv.COLOR_BGR2GRAY); # it is required because we are going to find the contour and its easier to do that on a grayscale image.

    # we will blur our grayscale frame!!
    blur=cv.GaussianBlur(gray, (5, 5), 0);

    # finding the threshold
    _, thresh=cv.threshold(blur, 20, 255, cv.THRESH_BINARY);

    # dilate the thresholded image(this helps in finding the better contours
    dilated=cv.dilate(thresh, None, iterations=3);

    # find the contours

    contours, _ =cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE);

    #cv.drawContours(frame1, contours, -1, (0, 255, 0), 2);

    for contour in contours:
        # Step-1: getting the co-ordinates, width and height and applying the boundingRect() method on the contour.
        (x, y, w, h)=cv.boundingRect(contour); # this is going to give us the x and y co-ordinates and width and height. We are going to apply this method on the contour.
        """
        x -> x co-ordinate
        y -> y co-ordinate
        w -> width
        h -> height
        """

        # Step-2: finding the area of the contour and drawing a rectangle around that contour
        if(cv.contourArea(contour)<900):
            continue;
        cv.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2);

        # print text on the image
        cv.putText(frame1, "Status: {}".format('Movement'), (10, 20), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3);

    cv.imshow('feed', frame1);

    # before reading the value of frame2, we are assigning the value of frame2 to frame 1.
    frame1=frame2;

    # reading the new frame!!
    ret, frame2=cap.read();

    if(cv.waitKey(25) & 0xFF==27):
        break;
    pass;

cv.destroyAllWindows();
cap.release();
