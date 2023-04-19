import cv2
import easyocr
from matplotlib import pyplot as plt

def show(image):
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB));
    plt.show();
    return;

def Blur(image):
    return (cv2.medianBlur(image, 5));

def DetectEdge(image):
    return (cv2.Canny(image, 100, 200));

def FindContours(image):
    return (cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE));

def Threshold(image):
    return (cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2));

# Load the image and convert it to grayscale
image = cv2.imread('car3.jpg');
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);

# Apply a median blur to reduce noise
gray = Blur(gray);

# Perform edge detection using Canny
edged = DetectEdge(gray);

# Find contours in the edged image
contours, hierarchy = FindContours(edged);

# Sort the contours by area in descending order
sortedContours = sorted(contours, key=cv2.contourArea, reverse=True)

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

# Loop over the contours
for contour in sortedContours:
    # Get the coordinates of the contour
    x, y, w, h = cv2.boundingRect(contour)
    # Check if the contour has the right aspect ratio and size
    if w / h > 2 and w / h < 6 and w > 80 and h > 20:
        # Extract the region of interest (ROI) containing the plate
        target = gray[y:y + h, x:x + w]
        # Apply adaptive thresholding to binarize the ROI
        thresh = Threshold(target);
        # Run OCR on the binarized ROI
        result = reader.readtext(thresh, detail=0)
        # If the result is not empty, print it and draw a bounding box around the plate
        if result:
            print(result)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 5)
            break;

# Display the image with the detected plates
show(image);
