import cv2
import numpy as np
from matplotlib import pyplot as plt


img=cv2.imread("C:\Python_Practice\opencv\spider.jpg",0)

lap = cv2.Laplacian(img, cv2.CV_64F,ksize=3)
lap = np.uint8(np.absolute(lap))

sobelX = cv2.Sobel(img, cv2.CV_64F, dx=1,dy=0)
sobelX = np.uint8(np.absolute(sobelX))

sobelY = cv2.Sobel(img, cv2.CV_64F, dx=0,dy=1)
sobelY = np.uint8(np.absolute(sobelY))

sobelcomb = cv2.bitwise_or(sobelX,sobelY)

titles=["image","lap","sobelx","sobely","comb"]
images=[img,lap,sobelX,sobelY,sobelcomb]



for i in range(5):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],"gray")
    plt.xticks([])
    plt.yticks([])

plt.show()