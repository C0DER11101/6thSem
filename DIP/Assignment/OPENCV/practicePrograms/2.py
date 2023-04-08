import cv2

img=cv2.imread('HappyFish.jpg', 0);

img=cv2.resize(img, (400, 400)); # resizing an image

cv2.imwrite('HappyFishResized.jpg', img);

img=cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE);

cv2.imwrite('HappyFishRotated.jpg', img);

cv2.imshow('Image', img);
cv2.waitKey(0) & 0xFF;
cv2.destroyAllWindows();
