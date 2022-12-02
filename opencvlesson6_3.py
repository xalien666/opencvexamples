import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("C:\Python_Practice\opencv\lena.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

kernel = np.ones((5,5),np.float32)/25

dst = cv2.filter2D(img,-1,kernel) #homogenius
blur=cv2.blur(img,(5,5))
gblur=cv2.GaussianBlur(img,(5,5),0)
median=cv2.medianBlur(img,5)
bilater=cv2.bilateralFilter(img,9,75,75)

titles=["image","dst","blur","gblur","median","bilater"]
images=[img,dst,blur,gblur,median,bilater]

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],"gray")
    plt.title(titles[i])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()