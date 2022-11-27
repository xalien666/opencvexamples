
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("C:\Python_Practice\opencv\lena.jpg")

cv2.imshow("pencere1",img)

img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)
#plt.xticks([]) #koordinatsistemini itirmek ucun
#plt.yticks([])
plt.show()



cv2.waitKey()
cv2.destroyAllWindows()