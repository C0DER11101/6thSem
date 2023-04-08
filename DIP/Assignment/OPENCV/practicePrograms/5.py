import cv2
import numpy as np

cap=cv2.VideoCapture(0); # index of the device(in this case: camera). It's 0 because I have only one camera(the one that comes preinstalled) in my laptop. If I had two then the index of the second camera would have been 1[pretty much like array indices].

"""using the camera to capture"""

while(True):
    ret, frame=cap.read(); # returns the frame(image) in the form of a numpy array. ret will tell us if the capture worked properly or not. It's a BOOLEAN.

    # getting the width and height of the video capture
    width=int(cap.get(3)); # the VideoCapture object cap has some properties which are identified by some integers, here 3 in the argument list of get() means we are using property 3 of cap which gets the width of the video capture
    height=int(cap.get(4));

    # display the frame
    #cv2.imshow('Frame', frame);

    image=np.zeros(frame.shape, np.uint8); #basically takes the shape of the frame and creates a numpy array that is 0-initialized and whose pixel values will be of type unsigned int 8bits(uint8). shape basically tells the number of rows, the number of columns and the number of channels in the image.
    smaller_frame=cv2.resize(frame, (0, 0), fx=0.5, fy=0.5); # shrinking the height and width of the frame by 0.5. Totally we have shrunk the image to 1/4th of the actual frame size.

    # placing the smaller frame in four corners of image.
    """
    image[:height//2, :width//2]=smaller_frame;
    image[height//2:, :width//2]=smaller_frame;
    image[:height//2, width//2:]=smaller_frame;
    image[height//2:, width//2:]=smaller_frame;
    """
    # upside-down images will be shown
    image[:height//2, :width//2]=cv2.rotate(smaller_frame, cv2.ROTATE_180);
    image[height//2:, :width//2]=cv2.rotate(smaller_frame, cv2.ROTATE_180);
    image[:height//2, width//2:]=cv2.rotate(smaller_frame, cv2.ROTATE_180);
    image[height//2:, width//2:]=cv2.rotate(smaller_frame, cv2.ROTATE_180);

    #display image which will display four captures.
    cv2.imshow('Frame', image);
    if(cv2.waitKey(1) == ord('q')): # ord() returns the ASCII value of the letter that passed to it as an argument.
        break;

cap.release(); # release the camera resource(close the camera).
cv2.destroyAllWindows();
