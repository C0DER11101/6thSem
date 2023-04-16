import cv2
import easyocr
from matplotlib import pyplot as plt

# Load the image and convert it to grayscale
image = cv2.imread('vehicle3.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a median blur to reduce noise
gray = cv2.medianBlur(gray, 5)

# Perform edge detection using Canny
edged = cv2.Canny(gray, 100, 200)

# Find contours in the edged image
contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Sort the contours by area in descending order
contours = sorted(contours, key=cv2.contourArea, reverse=True)

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

# Loop over the contours
for contour in contours:
    # Get the coordinates of the contour
    x, y, w, h = cv2.boundingRect(contour)
    
    # Check if the contour has the right aspect ratio and size
    if w / h > 2 and w / h < 6 and w > 80 and h > 20:
        # Extract the region of interest (ROI) containing the plate
        roi = gray[y:y + h, x:x + w]
        
        # Apply adaptive thresholding to binarize the ROI
        thresh = cv2.adaptiveThreshold(roi, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)
        
        # Run OCR on the binarized ROI
        result = reader.readtext(thresh, detail=0)
        
        # If the result is not empty, print it and draw a bounding box around the plate
        if result:
            print(result)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the image with the detected plates
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB));
plt.show();
