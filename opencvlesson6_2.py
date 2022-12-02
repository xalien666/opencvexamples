import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("C:\Python_Practice\opencv\smart.png",0)

_,mask =cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)

kernal=np.ones((2,2),np.uint8)

dilation=cv2.dilate(mask,kernal,iterations=3)
erosion=cv2.erode(mask,kernal,iterations=3)
opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal) #yuxardaki ikisinin qarisigidi
closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal) #dilation, erosing yuxardakinin eksini edir
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT,kernal)
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT,kernal)


titles=["image","binary","dilation","eros","opening","closing","gradient","tophat"]
images=[img,mask,dilation,erosion,opening,closing,mg,th]

for i in range(8):
    plt.subplot(2,4,i+1)
    plt.imshow(images[i],"gray")
    plt.title(titles[i])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()