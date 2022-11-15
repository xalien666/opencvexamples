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
        cv2.imshow("Pencere",frame)

        if cv2.waitKey(1)==ord("q"):
            break
    else:
        break



cap.release()
cv2.destroyAllWindows()


"""
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("C:\Python_Practice\opencv\output2.avi",fourcc,20.0,(640,480))

print(camera.isOpened())

while camera.isOpened():
#while True:
    ret, frame = camera.read()
    if ret ==True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        print(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)

        cv2.imshow("windowcam2",gray)
    
    #cv2.imshow("windowcam",frame)

        k=cv2.waitKey(1)

        if k==ord("q"):
            break
    else:
        break
camera.release()
out.release()
cv2.destroyAllWindows()
"""
"""
import cv2


cap=cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))


while cap.isOpened():
    ret,frame = cap.read()

    if ret==True:
        cv2.imshow("Pencere",frame)

        if cv2.waitKey(1)==ord("q"):
            break
    else:
        break



cap.release()
cv2.destroyAllWindows()
"""