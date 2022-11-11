
import cv2

img = cv2.imread("C:\Python_Practice\opencv\lena.jpg",0)

cv2.imshow("pencere1",img)

k=cv2.waitKey(0)

if k==27:
    cv2.destroyAllWindows()

elif k==ord("s"):

    cv2.imwrite("C:\Python_Practice\opencv\lenagrayscale.jpg",img)


    cv2.destroyAllWindows()

    