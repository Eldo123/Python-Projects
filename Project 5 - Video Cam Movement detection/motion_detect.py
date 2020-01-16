import cv2

cap=cv2.VideoCapture(0)

while(True):
    check,frame=cap.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow("frame",gray)

    key=cv2.waitKey(1)

    if(key==ord('q')):
        break


cap.release()
cv2.destroyAllWindows
