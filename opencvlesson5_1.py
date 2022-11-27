#tredshold

import cv2
import numpy as np

img = cv2.imread("C:\Python_Practice\opencv\gray.jpeg",0)

_,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY) #ret, th1
_,th2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV) #ret, th1
_,th3=cv2.threshold(img,127,255,cv2.THRESH_TRUNC) #ret, th1
_,th4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO) #ret, th1
_,th5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV) #ret, th1

cv2.imshow("pencere1",img)
cv2.imshow("pencere2",th1)
cv2.imshow("pencere3",th2)
cv2.imshow("pencere4",th3)

cv2.imshow("pencere5",th4)
cv2.imshow("pencere6",th5)

cv2.waitKey(0)
cv2.destroyAllWindows()