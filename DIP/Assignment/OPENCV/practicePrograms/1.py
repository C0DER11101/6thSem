import cv2

#img=cv2.imread('butterfly.jpg', 0)
img=cv2.imread('Happyfish.jpg', -1)
print(img);

cv2.imshow('Image', img);
#cv2.waitKey(5000);
key=cv2.waitKey(0) & 0xFF ;

if(key==27):
    cv2.destroyAllWindows();

elif(key==83 or key==115):
    cv2.imwrite('HappyfishCopy.jpg', img);
    cv2.destroyAllWindows();
