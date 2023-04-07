import cv2

img=cv2.imread('HappyFish.jpg', 0);

cv2.imshow('HappyFish', img);
key=cv2.waitKey(5000); # stay for 5s.

if(key==27):
    cv2.destroyAllWindows();
elif(key==83 or key==115):
    cv2.destroyAllWindows();
    cv2.imwrite('HappyfishGray.jpg', img);