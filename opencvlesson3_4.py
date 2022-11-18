import cv2
import numpy as np

def click_event(event,x,y,flags,parameter):

    if event ==cv2.EVENT_LBUTTONDOWN:
        print(x,", ",y)

        font = cv2.FONT_HERSHEY_SIMPLEX

        strXY=str(x)+ ", " + str(y)


        cv2.putText(img,strXY,(x,y),font,1,(255,255,255),2)


        cv2.imshow("Pencere",img)
 


img = cv2.imread("C:\Python_Practice\opencv\lena.jpg")

cv2.imshow("Pencere",img)

cv2.setMouseCallback("Pencere",click_event)


cv2.waitKey(0)
cv2.destroyAllWindows