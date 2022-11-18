import numpy as np
import cv2


img = cv2.imread("C:\Python_Practice\opencv\lena.jpg")

print(img.shape) # setir ve sutunlarin, renk kanallarinin sayini verir

print(img.size) # sekildeki piksellerin sayini verir

print(img.dtype) # sekilin daxilinde saxlanilan deyerlerin datatipini verir

b,g,r = cv2.split(img)


#cv2.imshow("Blue",b)
#cv2.imshow("Green",g)
#cv2.imshow("red",r)

img1 = cv2.merge((b,g,r))

cv2.imshow("new",img1)


#print(b,g,r)

cv2.imshow("windows", img)
cv2.waitKey(0)
cv2.destroyAllWindows