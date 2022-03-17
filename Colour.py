import cv2

cap = cv2.VideoCapture(0) # Modify the arg in VideoCapture if it didnt work. It shows the camera that you are using
# For colour processing it is better to set the image to a high resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


while True:
    _, frame = cap.read()

    #cv2.imshow('Frame', frame) testing....


    HSVframe = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('Frame', HSVframe)

    height, width, _ = frame.shape
    x = int(width / 2)
    y = int(height / 2)
    # The central pixel of the screen is under the process
    centre = HSVframe[y, x]
    HUEV = centre[0]

# !!!!! This library is not completed yet and will be extended and updated.

    colour = ""
    if HUEV < 5:
        colour = "RED"
    elif HUEV < 22:
        colour = "ORANGE"
    elif HUEV < 33:
        colour = "YELLOW"
    elif HUEV < 78:
        colour = "GREEN"
    elif HUEV < 131:
        colour = "BLUE"
    elif HUEV < 170:
        colour = "VIOLET"
    else:
        colour = "To be calculated"
    print(HUEV)

    centrebgr = frame[y, x]
    B, G, R = int(centrebgr[0]), int(centrebgr[1]), int(centrebgr[2])

    cv2.rectangle(frame, (x - 220, 10), (x + 200, 120), (255, 255, 255), -1)
    cv2.putText(frame, colour, (x - 200, 100), 0, 3, (B, G, R), 5)
    cv2.circle(frame, (x, y), 5, (25, 25, 25), 3)
    cv2.imshow("Frame", frame)

    print(B, G, R)


    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

