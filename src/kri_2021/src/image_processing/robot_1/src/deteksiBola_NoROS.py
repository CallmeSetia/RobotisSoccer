from imutils.video import FileVideoStream
# from imutils.video import FPS

import numpy as np
import cv2
import time
import imutils

def nothing(x):
    pass

def filterFrame(frame):
    frame = imutils.resize(frame, width=450)
    return frame

cv2.namedWindow('result')

kernel = np.ones((5,5),np.uint8)
# 5, 64, 119 - 255, 255, 255

# Trackbar
cv2.createTrackbar('H_min', 'result',0,255,nothing)
cv2.createTrackbar('H_max', 'result',255,255,nothing)
cv2.createTrackbar('S_min', 'result',0,255,nothing)
cv2.createTrackbar('S_max', 'result',255,255,nothing)
cv2.createTrackbar('V_min', 'result',0,255,nothing)
cv2.createTrackbar('V_max', 'result',255,255,nothing)

cv2.createTrackbar('Min_Radius', 'result',255,255,nothing)

video = FileVideoStream(0, transform=filterFrame).start()
time.sleep(1.0)

while video.running():
    frame = video.read()
    lebar = frame.shape[1]
    tinggi = frame.shape[0]

    frame = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    H_min = cv2.getTrackbarPos('H_min', 'result')
    H_max = cv2.getTrackbarPos('H_max', 'result')
    S_min = cv2.getTrackbarPos('S_min', 'result')
    S_max = cv2.getTrackbarPos('S_max', 'result')
    V_min = cv2.getTrackbarPos('V_min', 'result')
    V_max = cv2.getTrackbarPos('V_max', 'result')

    Min_Radius = cv2.getTrackbarPos('Min_Radius', 'result')
    lower_yellow = np.array([H_min, S_min, V_min])
    upper_yellow = np.array([H_max, S_max, V_max])

    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    kernels_0 = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernels_0)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7)))

    mask = cv2.erode(opening, kernel, iterations=3)
    mask = cv2.dilate(mask, kernel, iterations=3)

    mask = cv2.dilate(mask, kernel, iterations=3)
    mask = cv2.erode(mask, kernel, iterations=3)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    if (len(cnts) > 0):
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)

        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        if radius > int(Min_Radius):
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, center, 3, (0, 0, 255), -1)
            cv2.putText(frame, "BOLA", (center[0] + 10, center[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0), 1)
            cv2.putText(frame, "(" + str(center[0]) + "," + str(center[1]) + ")", (center[0] + 10, center[1] + 15),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)

            x_bola = (x / lebar) * 2 - 1
            y_bola = (y / tinggi) * 2 - 1

            print("X_BOLA : {} - Y_BOLA : {} == STATE BOLA: {}  " . format(x_bola, y_bola, "DETEK"))

        else :
            print(" == STATE BOLA: {}  ".format("NOT DETECTED"))

    cv2.imshow('result', result)
    cv2.imshow('Masking', mask)
    cv2.imshow('OPENNING', opening)
    cv2.imshow('CLOSSING', closing)
    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
video.stop()



