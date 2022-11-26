#trackbar
import cv2
import numpy as np

def callback(x):
    print(x)

img = np.zeros((300,512,3), np.uint8)

cv2.namedWindow("image")

cv2.createTrackbar("Blue","image",0,255,callback)
cv2.createTrackbar("Green","image",0,255,callback)
cv2.createTrackbar("Red","image",0,255,callback)

while(1):
    cv2.imshow("image",img)

    k=cv2.waitKey(1)
    if k==27:
        break

    b=cv2.getTrackbarPos("Blue","image")
    g=cv2.getTrackbarPos("Green","image")
    r=cv2.getTrackbarPos("Red","image")

    img[:]=[b,g,r]

cv2.waitKey(0)
cv2.destroyAllWindows