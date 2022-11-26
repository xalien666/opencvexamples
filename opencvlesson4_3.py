#trackbar
import cv2
import numpy as np

def callback(x):
    print(x)


cv2.namedWindow("image")

cv2.createTrackbar("CP","image",0,255,callback)


cv2.createTrackbar("switch","image",0,1,callback)

while(1):
    img = cv2.imread("C:\Python_Practice\opencv\lena.jpg",1)
    cv2.imshow("image",img)

    
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,"CP",(0,255),font,4,(255,255,255),10, cv2.LINE_AA)


    k=cv2.waitKey(1)
    if k==27:
        break

 
    s=cv2.getTrackbarPos("switch","image")

    if s==0:
        pass
    else:
         img = cv2.cvtColor("image", cv2.COLOR_BGR2GRAY)

cv2.destroyAllWindows