import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("C:\Python_Practice\opencv\smart.png",0)

_,mask =cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)

titles=["image","binary"]
images=[img,mask]

for i in range(2):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i],"gray")
    plt.title(titles[i])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()