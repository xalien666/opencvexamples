import cv2
import numpy as np

def click_event(event,x,y,flags,parameter):

    if event == cv2.EVENT_LBUTTONDOWN:

        blue= img[x,y,0]
        green=img[x,y,1]
        red = img[x,y,2]


        cv2.circle(img, (x,y),3,(0,0,255),3)

        myColorImage = np.zeros((512,512,3),np.uint8)

        myColorImage[:]=[blue,green,red]

        cv2.imshow("Color",myColorImage)

        

img = cv2.imread("C:\Python_Practice\opencv\lena.jpg")

cv2.imshow("Pencere",img)

cv2.setMouseCallback("Pencere",click_event)

cv2.waitKey(0)
cv2.destroyAllWindows

