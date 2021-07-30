#!/usr/bin/python
# USAGE
# python ball_tracking.py --video ball_tracking_example.mp4
# python ball_tracking.py

# import the necessary packages


from __future__ import print_function
from collections import deque

import rospy
import rosparam
from std_msgs.msg import Int8

from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from op3_ball_detector.msg import CircleSetStamped
from geometry_msgs.msg import Point
from geometry_msgs.msg import Twist

import numpy as np
import cv2
import imutils


class DeteksiBola_Pink:

    trackbar = False
    hsvLower, hsvUpper, MinRadius = [0,0,0], [255, 255, 255], 5

    def __init__(self, UseTrackbar = False):

        self.bridge = CvBridge()

        self.image_sub = rospy.Subscriber("usb_cam_node/image_raw", Image, self.callback_image)
        self.mask_pub = 0
        self.koordinatBola = rospy.Publisher("KRSBI/image_processing/deteksi_bola/coordinate/bola", CircleSetStamped, queue_size=10)
        self.ballState = rospy.Publisher("KRSBI/image_processing/ball_state", Int8, queue_size=10)


        if UseTrackbar is True:
            DeteksiBola_Pink.trackbar = True
            self.mask_pub = rospy.Publisher("KRSBI/image_processing/deteksi_bola/image/mask_out", Image, queue_size=10)

            rosparam.set_param('/bola_h_low', str(DeteksiBola_Pink.hsvLower[0]))
            rosparam.set_param('/bola_s_low', str(DeteksiBola_Pink.hsvLower[1]))
            rosparam.set_param('/bola_v_low', str(DeteksiBola_Pink.hsvLower[2]))
            rosparam.set_param('/bola_h_up', str(DeteksiBola_Pink.hsvUpper[0]))
            rosparam.set_param('/bola_s_up', str(DeteksiBola_Pink.hsvUpper[1]))
            rosparam.set_param('/bola_v_up', str(DeteksiBola_Pink.hsvUpper[2]))

        else:
            self.mask_pub = 0
            DeteksiBola_Pink.trackbar = False

        self.rate = rospy.Rate(30)

    def nothing(self):
        pass

    def state_bola(self, status):
        if status == 1:
            self.ballState.publish(1)
        elif status == 0:
            self.ballState.publish(0)

    def filterFrame(self, frame):
        frame = imutils.resize(frame, width=450)
        return frame

    def get_LuasKontur(self, contours):
        all_kontur = []
        for cnt in contours:
            area = cv2.contourArea(cnt)
            all_kontur.append(area)

        return all_kontur

    def DeteksiBola_Kontur(self, Kontur, lebarFrame, tinggiFrame, minRadius=5):
        """
        :param Conturs:  Detesi Bola By Kontur
        :param Min_Radius: Minimal Radius
        :return:
        """
        c = max(Kontur, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)

        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        flagDetek, x_bola, y_bola = 0, 0, 0

        if radius > int(minRadius):
            x_bola = (x / lebarFrame) * 2 - 1
            y_bola = (y / tinggiFrame) * 2 - 1
            flagDetek = 1

        else:
            flagDetek = 0

        return x, y, x_bola, y_bola, radius, center, flagDetek

    def callback_image(self, data):
        print("PROCESSING")
        try:
            frame = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)

        frame = self.filterFrame(frame)
        lebarFrame = frame.shape[1]
        tinggiFrame = frame.shape[0]

        frame = cv2.GaussianBlur(frame, (11, 11), 0)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        kernel = np.ones((5, 5), np.uint8)

        if DeteksiBola_Pink.trackbar is True:
            if rospy.has_param("/bola_h_low"):
                DeteksiBola_Pink.hsvLower = [rospy.get_param("/bola_h_low"), rospy.get_param("/bola_s_low"), rospy.get_param("/bola_v_low")]
                DeteksiBola_Pink.hsvUpper = [rospy.get_param("/bola_h_up"), rospy.get_param("/bola_s_up"), rospy.get_param("/bola_v_up")]

        H_min = DeteksiBola_Pink.hsvLower[0]
        H_max = DeteksiBola_Pink.hsvUpper[0]
        S_min = DeteksiBola_Pink.hsvLower[1]
        S_max = DeteksiBola_Pink.hsvUpper[1]
        V_min = DeteksiBola_Pink.hsvLower[2]
        V_max = DeteksiBola_Pink.hsvUpper[2]
        Min_Radius = DeteksiBola_Pink.MinRadius

        lower_yellow = np.array([H_min, S_min, V_min])
        upper_yellow = np.array([H_max, S_max, V_max])

        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)


        # print("HSV LOW: {} - HSV UP: {}".format(lower_yellow, upper_yellow))
        kernels_0 = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernels_0)
        closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7)))

        mask = cv2.erode(closing, kernel, iterations=3)
        mask = cv2.dilate(mask, kernel, iterations=3)

        mask = cv2.dilate(mask, kernel, iterations=3)
        mask = cv2.erode(mask, kernel, iterations=2)
        
        result = cv2.bitwise_and(frame, frame, mask=mask)

        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]  #

        if (len(cnts) > 0):

            sortedKontur = sorted(cnts, key=cv2.contourArea, reverse=True)
            # x, y, x_ball, y_ball, radius, center, flag = DeteksiBola_Kontur(cnts, lebar, tinggi, Min_Radius)
            x, y, x_ball, y_ball, radius, center, flag = self.DeteksiBola_Kontur(sortedKontur, lebarFrame, tinggiFrame, Min_Radius)

            if flag > 0:
                cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                cv2.circle(frame, center, 3, (0, 0, 255), -1)
                cv2.putText(frame, "BOLA", (center[0] + 10, center[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0), 1)
                cv2.putText(frame, "(" + str(center[0]) + "," + str(center[1]) + ")", (center[0] + 10, center[1] + 15),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)

                x = (x / lebarFrame) * 2 - 1
                y = (y / tinggiFrame) * 2 - 1
                # circleMsg = CircleSetStamped()
                # circlePoint = Point()
                # circlePoint.x = (center[0] / lebarFrame) * 2 - 1
                # circlePoint.y = (center[1] / tinggiFrame) * 2 - 1
                # circlePoint.z = radius
                # circleMsg.circles = [circlePoint]
                #
                # self.koordinatBola.publish(circleMsg)

                print("X_Center: {} - Y_Center: {}".format(x, y))

            # self.state_bola(flag)

        cv2.imshow('result', result)
        cv2.imshow('Masking', mask)
        # cv2.imshow('OPENNING', opening)
        cv2.imshow('CLOSSING', closing)
        cv2.imshow("Hsv", hsv)

        cv2.imshow("Image window", frame)

        cv2.waitKey(1)


# ball_detector()
if __name__ == "__main__":

    try:
        print("IMAGE PROCESSING ... INIT")
        rospy.init_node('processing_image_bola', anonymous=False)
        DeteksiBola_Pink(UseTrackbar=True)
        rospy.spin()

    except rospy.ROSInterruptException:
        cv2.destroyAllWindows()
        pass