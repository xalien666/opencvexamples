import cv2
import datetime as dt


cap=cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2000)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 2000)

print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

while cap.isOpened():
    ret,frame = cap.read()

    if ret==True:
        text="width: " + str(cap.get(3)) + "height: "+str(cap.get(4))
        date = str(dt.datetime.now())

        font = cv2.FONT_HERSHEY_SIMPLEX

        frame=cv2.putText(frame,text,(10,50),font,1,(0,0,255),2,cv2.LINE_AA)
        frame=cv2.putText(frame,date,(10,100),font,1,(0,0,255),2,cv2.LINE_AA)

        
        
        cv2.imshow("Pencere",frame)

        if cv2.waitKey(1)==ord("q"):
            break
    else:
        break



cap.release()
cv2.destroyAllWindows()

"""
import cv2


cap=cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2000)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 2000)

print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

while cap.isOpened():
    ret,frame = cap.read()

    if ret==True:
        text="OpenCV"
        font = cv2.FONT_HERSHEY_SIMPLEX
        frame=cv2.putText(frame,text,(10,50),font,1,(0,0,255),2,cv2.LINE_AA)
        
        
        cv2.imshow("Pencere",frame)

        if cv2.waitKey(1)==ord("q"):
            break
    else:
        break



cap.release()
cv2.destroyAllWindows()
"""