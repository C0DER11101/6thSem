# Drawing lines, images, circles and text
import cv2
import numpy as np

# Drawing a line

cap=cv2.VideoCapture(0);

while(True):
    ret, frame=cap.read();

    width=int(cap.get(3));
    height=int(cap.get(4));

    img=cv2.line(frame, (0, 0), (width, height), (255, 0 ,0), 10);
    """
    arguments in cv2.line():
    frame: -> source image.
    (0, 0): -> starting co-ordinate of the line.
    (width, height): -> ending co-ordinate of the line.
    (255, 0, 0): -> value of blue, value of green and value of red for the line to be drawn.
    10: -> thickness of the line.
    """
    img=cv2.line(img, (0, height), (width, 0), (0, 255 ,0), 10); # passed img instead frame so that this line overlaps the first line.


    # drawing a rectangle

    img=cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128), 5);

    """
    again, img is provided instead of frame, so that it overlaps with the previously drawn lines.
    Arguments in cv2.rectangle():
    img: -> source image
    (100, 100): -> starting co-ordinates for the rectangle.
    (200, 200): -> ending co-ordinates for the rectangle.
    (128, 128, 128): -> blue, green, red together with these values make gray color.
    5: -> thickness.
    """

    # drawing a circle

    img=cv2.circle(img, (300, 300), 60, (0, 0, 255), -1);

    """
    arguments in cv2.circle():
    img: -> source image.
    (300, 300): -> co-ordinates of the center.
    60: -> radius.
    (0, 0, 255): -> red color.
    -1: -> this means that it won't be hollow circle, but a filled circle. This parameter can also be used with cv2.rectangle().
    """

    # drawing text
    font=cv2.FONT_HERSHEY_SIMPLEX; # choosing font style
    img=cv2.putText(img, 'Hello', (200, height-10), font, 4, (0, 0, 0), 5, cv2.LINE_AA);

    """
    arguments in cv2.putText()
    img: -> source image
    'Hello': -> string to be displayed on the image.
    (200, height-10): -> co-ordinates(position) for displaying the text(always in bottom-left corner).
    font: -> font style.
    4: -> font scale(or size).
    (0, 0, 0): -> color of font.
    5: -> thickness of line.
    cv2.LINE_AA: -> line type(cv2.LINE_AA is recommended because it makes the text look better).
    """

    cv2.imshow('Frame', img);

    if(cv2.waitKey(1)==ord('q')):
        break;

cap.release();

cv2.destroyAllWindows();
