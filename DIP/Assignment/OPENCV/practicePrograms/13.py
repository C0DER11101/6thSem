import cv2
import numpy as np


blue = np.uint8([[[255, 0, 0]]]);

hsv_blue=cv2.cvtColor(blue, cv2.COLOR_BGR2HSV);

print(hsv_blue);
