import cv2
import numpy as np

def click_event(event,x,y,flags,parameter):

    if event ==cv2.EVENT_LBUTTONDOWN:

        cv2.circle(img, (x,y),3,(0,0,255),-1)

        points.append((x,y))

        if len(points)>=2:
            cv2.line(img,points[-1],points[-2],(0,0,255),1)

        cv2.imshow("Pencere",img)
        
    if event ==cv2.EVENT_RBUTTONDOWN:

        cv2.circle(img, (x,y),3,(0,0,255),-1)

        points.pop((x,y))

        if len(points)>=2:
            cv2.line(img,points[-1],points[-2],(0,0,255),1)

        cv2.imshow("Pencere",img)


img = np.zeros([512,512,3])

cv2.imshow("Pencere",img)
points=[]
cv2.setMouseCallback("Pencere",click_event)


cv2.waitKey(0)
cv2.destroyAllWindows
