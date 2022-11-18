import numpy as np
import cv2

img1 = np.zeros((512,512,3), np.uint8)
img1 = cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)

img2 = cv2.imread("C:\Python_Practice\opencv\lena.jpg")

#bitAnd = cv2.bitwise_and(img1,img2)
#bitOr = cv2.bitwise_or(img1,img2)
#bitxor = cv2.bitwise_xor(img1,img2)
bitnot = cv2.bitwise_not(img1)

#cv2.imshow("W",img1)
#cv2.imshow("W2",img2)

#cv2.imshow("Worginal",bitAnd)

#cv2.imshow("Worginal",bitOr)

#cv2.imshow("Worginal",bitxor)

cv2.imshow("Worginal",bitnot)

cv2.waitKey(0)
cv2.destroyAllWindows