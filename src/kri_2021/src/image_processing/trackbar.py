#!/usr/bin/python2

import numpy as np
import cv2

import rosparam
import rospy
import roslib


roslib.load_manifest('processing_image')

hsvLow = (94, 57, 63)
hsvMax = (133, 255,255)
treshold_val = 0


def nothing(x):
    pass

def main():
    pass

cv2.namedWindow("Trackbars")
# cv2.resizeWindow("Trackbars", 600, 600)

if rospy.has_param("/bola_h_low"):
    h_low = int(rospy.get_param("/bola_h_low"))
    s_low = int(rospy.get_param("/bola_s_low"))
    v_low = int(rospy.get_param("/bola_v_low"))
    h_up = int(rospy.get_param("/bola_h_up"))
    s_up = int(rospy.get_param("/bola_s_up"))
    v_up = int(rospy.get_param("/bola_v_up"))

elif rospy.has_param("/garis_h_low"):
    h_low = int(rospy.get_param("/garis_h_low"))
    s_low = int(rospy.get_param("/garis_s_low"))
    v_low = int(rospy.get_param("/garis_v_low"))
    h_up = int(rospy.get_param("/garis_h_up"))
    s_up = int(rospy.get_param("/garis_s_up"))
    v_up = int(rospy.get_param("/garis_v_up"))

elif rospy.has_param("/tiang_h_low"):
    h_low = int(rospy.get_param("/tiang_h_low"))
    s_low = int(rospy.get_param("/tiang_s_low"))
    v_low = int(rospy.get_param("/tiang_v_low"))
    h_up = int(rospy.get_param("/tiang_h_up"))
    s_up = int(rospy.get_param("/tiang_s_up"))
    v_up = int(rospy.get_param("/tiang_v_up"))



if rospy.has_param("/cam_kecerahan"):
	brigtnessCam = int(rospy.get_param("/cam_kecerahan"))
	exposureCam = int(rospy.get_param("/cam_kontras"))

else:
	brigtnessCam = 0
	exposureCam  = 0
	rosparam.set_param('/cam_kecerahan', str(brigtnessCam))
	rosparam.set_param('/cam_kontras', str(exposureCam))

hsvLow = (h_low, s_low, v_low)
hsvMax = (h_up, s_up, v_up)

cv2.createTrackbar("Low Hue", "Trackbars", hsvLow[0], 255, nothing)
cv2.createTrackbar("Low Sat", "Trackbars", hsvLow[1], 255, nothing)
cv2.createTrackbar("Low Val", "Trackbars", hsvLow[2], 255, nothing)
cv2.createTrackbar("Max Hue", "Trackbars", hsvMax[0], 255, nothing)
cv2.createTrackbar("Max Sat", "Trackbars", hsvMax[1], 255, nothing)
cv2.createTrackbar("Max Val", "Trackbars", hsvMax[2], 255, nothing)
cv2.createTrackbar("Treshold", "Trackbars", treshold_val, 100, nothing)

cv2.createTrackbar("Plus (1) - Minus (0)", "Trackbars", 1, 1, nothing)
cv2.createTrackbar("Kecerahan", "Trackbars", exposureCam, 255, nothing)
cv2.createTrackbar("Kontras", "Trackbars", brigtnessCam, 255, nothing)

## Default

contours = []

while True:


    trackbar_LowHue = cv2.getTrackbarPos("Low Hue", "Trackbars")
    trackbar_LowSat = cv2.getTrackbarPos("Low Sat", "Trackbars")
    trackbar_LowVal = cv2.getTrackbarPos("Low Val", "Trackbars")
    trackbar_MaxHue = cv2.getTrackbarPos("Max Hue", "Trackbars")
    trackbar_MaxSat = cv2.getTrackbarPos("Max Sat", "Trackbars")
    trackbar_MaxVal = cv2.getTrackbarPos("Max Val", "Trackbars")
    treshold_val = cv2.getTrackbarPos("Treshold", "Trackbars")
    trackbar_Mode = cv2.getTrackbarPos("Plus (1) - Minus (0)", "Trackbars")

    trackbar_Kontras = cv2.getTrackbarPos("Kecerahan", "Trackbars")
    trackbar_Kecerahan = cv2.getTrackbarPos("Kontras", "Trackbars")

    if rospy.has_param("/bola_h_low"):
        rosparam.set_param('/bola_h_low', str(trackbar_LowHue))
        rosparam.set_param('/bola_s_low', str(trackbar_LowSat))
        rosparam.set_param('/bola_v_low', str(trackbar_LowVal))
        rosparam.set_param('/bola_h_up', str(trackbar_MaxHue))
        rosparam.set_param('/bola_s_up', str(trackbar_MaxSat))
        rosparam.set_param('/bola_v_up', str(trackbar_MaxVal))
        rosparam.set_param('/bola_treshold', str(treshold_val))

    elif rospy.has_param("/tiang_h_low"):
        rosparam.set_param('/tiang_h_low', str(trackbar_LowHue))
        rosparam.set_param('/tiang_s_low', str(trackbar_LowSat))
        rosparam.set_param('/tiang_v_low', str(trackbar_LowVal))
        rosparam.set_param('/tiang_h_up', str(trackbar_MaxHue))
        rosparam.set_param('/tiang_s_up', str(trackbar_MaxSat))
        rosparam.set_param('/tiang_v_up', str(trackbar_MaxVal))
        rosparam.set_param('/tiang_treshold', str(treshold_val))

    elif rospy.has_param("/garis_h_low"):
        rosparam.set_param('/garis_h_low', str(trackbar_LowHue))
        rosparam.set_param('/garis_s_low', str(trackbar_LowSat))
        rosparam.set_param('/garis_v_low', str(trackbar_LowVal))
        rosparam.set_param('/garis_h_up', str(trackbar_MaxHue))
        rosparam.set_param('/garis_s_up', str(trackbar_MaxSat))
        rosparam.set_param('/garis_v_up', str(trackbar_MaxVal))
        rosparam.set_param('/garis_treshold', str(treshold_val))

    if trackbar_Mode == 1: # Plus
        trackbar_Kontras = 1 * trackbar_Kontras
        trackbar_Kecerahan = 1 * trackbar_Kecerahan
    elif trackbar_Mode == 0: # Minus
        trackbar_Kontras = -1 * trackbar_Kontras
        trackbar_Kecerahan = -1 * trackbar_Kecerahan

    rosparam.set_param('/cam_kecerahan', str(trackbar_Kecerahan))
    rosparam.set_param('/cam_kontras', str(trackbar_Kontras))

    #update hsvLow and Max
    hsvLow = np.array([trackbar_LowHue, trackbar_LowSat, trackbar_LowVal])
    hsvMax = np.array([trackbar_MaxHue, trackbar_MaxSat, trackbar_MaxVal])


    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv2.destroyAllWindows()
