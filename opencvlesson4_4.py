import cv2
import numpy as np

def callback(x):
    pass

cv2.namedWindow("Tracking")
cv2.createTrackbar("LH","Tracking",0,255,callback)
cv2.createTrackbar("LS","Tracking",0,255,callback)
cv2.createTrackbar("LV","Tracking",0,255,callback)

cv2.createTrackbar("UH","Tracking",0,255,callback)
cv2.createTrackbar("US","Tracking",0,255,callback)
cv2.createTrackbar("UV","Tracking",0,255,callback)

while True:
    img = cv2.imread("C:\Python_Practice\opencv\smart.png")
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    l_h=cv2.getTrackbarPos("LH","Tracking")
    l_s=cv2.getTrackbarPos("LS","Tracking")
    l_v=cv2.getTrackbarPos("LV","Tracking")

    u_h=cv2.getTrackbarPos("UH","Tracking")
    u_s=cv2.getTrackbarPos("US","Tracking")
    u_v=cv2.getTrackbarPos("UV","Tracking")

    lower_b = np.array([l_h,l_s,l_v])
    upper_b = np.array([u_h,u_s,u_v])



   # lower_b = np.array([110,50,50]) #(h,s,v)
   # upper_b = np.array([130,255,255]) #(h,s,v)

    mask = cv2.inRange(hsv,lower_b,upper_b)
    result = cv2.bitwise_and(img,img,mask=mask)


    cv2.imshow("pencere1",img)
    cv2.imshow("mask",mask)
    cv2.imshow("result",result)

    k=cv2.waitKey(1)

    if k==27:
        break


cv2.destroyAllWindows()


