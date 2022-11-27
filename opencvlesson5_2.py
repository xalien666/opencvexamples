#tredshold

import cv2
import numpy as np

img = cv2.imread("C:\Python_Practice\opencv\sudoku.jpeg",0)

_,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY) #ret, th1
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

cv2.imshow("pencere1",img)
cv2.imshow("pencere2",th1)
cv2.imshow("pencere3",th2)
cv2.imshow("pencere4",th3)


cv2.waitKey(0)
cv2.destroyAllWindows()