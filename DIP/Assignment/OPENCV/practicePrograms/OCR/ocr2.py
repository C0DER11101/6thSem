import cv2
import numpy as np
import pytesseract as pts

def thinFont(image): # dilation and erosion are meant to handle an image that has that has black background and the font and the text is white.
    image=cv2.bitwise_not(image);
    kernel=np.ones((2, 2), np.uint8);
    image=cv2.erode(image, kernel, iterations=1); # erosion is thinning of pixels
    image=cv2.bitwise_not(image);
    return image;

def thickFont(image): # dilation and erosion are meant to handle an image that has that has black background and the font and the text is white.
    image=cv2.bitwise_not(image);
    kernel=np.ones((2, 2), np.uint8);
    image=cv2.dilate(image, kernel, iterations=1); # erosion is thinning of pixels
    image=cv2.bitwise_not(image);
    return image;

def noise_removal(image):
    kernel=np.ones((1, 1), np.uint8);
    image=cv2.dilate(image, kernel, iterations=1);
    kernel=np.ones((1, 1), np.uint8);
    image=cv2.erode(image, kernel, iterations=1);

    #these two functions actually get rid of noise in the background
    image=cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel);
    image=cv2.medianBlur(image, 3);
    #----------------------------------------------------------------
    return image;

def display(string, img):
    cv2.imshow(string, img);
    return;

def toGray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);

def save(name, image):
    cv2.imwrite(name, image);
    return;

img=cv2.imread('vehicle.jpg');

# inverting the image
inverted=cv2.bitwise_not(img);



# Binarization(first the image needs to be converted to a grayscale image).
grayImage=toGray(img);

display('image', img);
display('inverted', inverted);
display('gray', grayImage);
save('inverted.jpg', inverted);
save('gray.jpg', grayImage);

# noise removal!!
thresh, img_bw=cv2.threshold(grayImage, 200, 230, cv2.THRESH_BINARY);
display('blackWhite', img_bw);
save('blackWhite.jpg', img_bw);

no_noise=noise_removal(img_bw);
save('NoNoise.jpg', no_noise);
display('No noise', no_noise);

# dilation and erosion: when you have fonts that looks little too thick or thin.

"""
NOTE:
dilation and erosion will work in the opposite order unless you invert the images in the beginning of the function and at the end of the function
"""

eroded_image=thinFont(no_noise);
save('ErodedImage.jpg', eroded_image);
display('Eroded image', eroded_image);

dilated_image=thickFont(no_noise);
save('DilatedImage.jpg', dilated_image);
display('Dilated image', dilated_image);


# Rotation and deskewing!!
"""
used when dealing with a pdf or an image file that pivoted sideways.
"""

cv2.waitKey(0) & 0xFF;

cv2.destroyAllWindows();
