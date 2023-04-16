import cv2
import numpy as np
import pytesseract as pts

def display(title, image):
    cv2.imshow(title, image);
    return;

img=cv2.imread('vehicle.jpg');
no_noise=cv2.imread('NoNoise.jpg');

display('vehicle', img);
display('no noise', no_noise);

ocr_result=pts.image_to_string(no_noise);

print(ocr_result);

cv2.waitKey(0) & 0xFF;
cv2.destroyAllWindows();
