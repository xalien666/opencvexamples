import numpy as np
import cv2

img = cv2.imread("C:\Python_Practice\opencv\lena.jpg")

# print(img.shape) - (512, 512, 3)

burun = img[293:338, 285:324] # [y1:y2, x1,x2] 

#yeni koordinaltlar 437,288 dir. ora kocurdende 338-299=45
# 324-285 = 39 olur
# daha sonra yeni koordinatlar o qeder arta biler
#ona gorede 288+45 = 333 olur, 437 + 39 = 476 olur

img[288:333, 437:476] = burun

cv2.imshow("windows", img)
cv2.waitKey(0)
cv2.destroyAllWindows
