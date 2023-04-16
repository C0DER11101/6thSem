# 1. Import modules
import numpy as np
import cv2
import imutils
import easyocr
from matplotlib import pyplot as plt
#-------------------------------------

def show(image):
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB));
        plt.show();
        return;

def filter(image):
    return(cv2.bilateralFilter(gray, 11, 17, 17)); # blurring is applied while keeping the edges sharp

def findEdge(image):
    return(cv2.Canny(filtered, 30, 200));

def FindContours(image):
    return(cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE));

def GetKeyContours(contours):
    return(imutils.grab_contours(contours));

def EmptyMask(image):
    return(np.zeros(gray.shape, np.uint8)); # an empty mask

def MinContour(x, y):
    return(np.min(x), np.min(y))

def MaxContour(x, y):
    return(np.max(x), np.max(y));

# 2. Read the image
img=cv2.imread('vehicle3.jpg');
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
#-------------------------------------

# 3. Apply filter and find edges for localization
filtered=filter(gray);
edged=findEdge(filtered);
#-------------------------------------

# 4. Find contours and apply mask
contours=FindContours(edged);
keyContours=GetKeyContours(contours);
sortedContours=sorted(keyContours, key=cv2.contourArea, reverse=True);

# Loop through each of the contours
pos=None;
for contour in sortedContours:
        rect=cv2.approxPolyDP(contour, 12, True);
        if(len(rect)==4):
                pos=rect;
                break;
        pass;

# Apply the mask
mask=EmptyMask(gray);
contourDrawnMask=cv2.drawContours(mask, [pos], 0, 255, -1);
new_image=cv2.bitwise_and(img, img, mask=contourDrawnMask);

# Isolate the number plate section
(x, y)=np.where(contourDrawnMask==255);
(x1, y1)=MinContour(x, y);
(x2, y2)=MaxContour(x, y);
target_area=gray[x1:x2+1, y1:y2+1];
#-------------------------------------

# 5. Use easy OCR to read text
reader=easyocr.Reader(['en']);
result=reader.readtext(target_area);
print(result);
#-------------------------------------


show(target_area);
