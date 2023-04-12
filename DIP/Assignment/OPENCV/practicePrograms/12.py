import numpy as np
import cv2

cap=cv2.VideoCapture(0);


while(True):
	_, frame=cap.read();# the underscore is just used to signify we are just ignoring the boolean returned by read().

	hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV);

	lower_red=np.array([0, 0, 0]);
	upper_red=np.array([255, 255, 255]);

	mask=cv2.inRange(hsv, lower_red, upper_red);

	res=cv2.bitwise_and(frame, frame, mask=mask);

	cv2.imshow('Frame', frame);
	cv2.imshow('Result', res);
	cv2.imshow('Mask', mask);

	if((cv2.waitKey(1) & 0xFF)==ord('q')):
		break;


cap.release();
cv2.destroyAllWindows();