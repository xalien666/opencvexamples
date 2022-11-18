import numpy as np
import cv2

img1 = cv2.imread("C:\Python_Practice\opencv\lena.jpg")
img2 = cv2.imread("C:\Python_Practice\opencv\lena1.png")

img1 = cv2.resize(img1,(512,512))
img2 = cv2.resize(img2,(512,512))


#data = cv2.add(img1,img2)

data=cv2.addWeighted(img1, .5, img2,.7,0)

cv2.imshow("pencere",data)


cv2.waitKey(0)
cv2.destroyAllWindows