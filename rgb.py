import numpy as np
import cv2

cap = cv2.VideoCapture(0) # Modify the arg in VideoCapture if it didnt work. It shows the camera that you are using
while True:
    ret, frame = cap.read()
    width = int(cap.get(3)) # Search cv2.get values for more information about 3 and 4.
    height = int(cap.get(4))

    HSVFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lblue = np.array([90,50,50]) # lblue stands for the lower range of blue
    ublue = np.array([130,255,255]) # hblue stands for the higher range of blue
    mask = cv2.inRange(HSVFrame, lblue, ublue)

    result = cv2.bitwise_and(frame, frame, mask=mask)



    cv2.imshow('frame', result)
    cv2.imshow('mask', mask)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()