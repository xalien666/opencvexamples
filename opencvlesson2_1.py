import cv2
import numpy as np

img=np.zeros([512,512,3])
cv2.imshow("pencere",img)

#img = cv2.imread("C:\Python_Practice\opencv\lena.jpg",1)

img = cv2.line(img, (0,0),(400,255),(0,0,255),1)

img = cv2.arrowedLine(img, (0,255),(255,255),(0,0,255),1)

img=cv2.rectangle(img, (384,0), (510,128),(0,134,0),5)
img=cv2.rectangle(img, (384,0), (510,128),(0,134,0),-1) #-1 kvadratin icini doldurur thicknessde

img=cv2.circle(img, (447,63), 63,(0,0,255),5)

font = cv2.FONT_HERSHEY_SIMPLEX

img=cv2.putText(img,"OpenCv",(10,400),font,4,(255,255,255),10, cv2.LINE_AA)

cv2.imshow("pencere",img)


cv2.waitKey(0)
cv2.destroyAllWindows