#!/usr/bin/python

from __future__ import print_function
from collections import deque

import numpy as np
import cv2
import imutils
import time
import sys
# from GUI_KRSBI import *

# penambahan baru
import rosparam
import rospy
import roslib

from std_msgs.msg import String
from std_msgs.msg import Float64
from std_msgs.msg import Int8
from std_msgs.msg import Bool
from std_msgs.msg import Int64

from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
# from op3_ball_detector.msg import CircleSetStamped
from geometry_msgs.msg import Point
from geometry_msgs.msg import Twist


def nothing():
    pass


roslib.load_manifest('processing_image')

hsvLow = (86, 0, 113)
hsvMax = (116, 255, 255)

treshold_val = 0
contours = []


class DeteksiTiang:

    def __init__(self):
        global hsvMax, hsvLow, treshold_val

        self.image_pub = rospy.Publisher("KRSBI/image/garis_tiang/image_out", Image, queue_size=10)
        self.image_sub = rospy.Subscriber("usb_cam_node/image_raw", Image, self.callback)

        self.mask_pub = rospy.Publisher("KRSBI/image/garis_tiang/mask_out", Image, queue_size=10)

        self.tiang_x_y = rospy.Publisher("KRSBI/image/garis_tiang/koordinat/x_y", Point, queue_size=10)

        self.pub_w = rospy.Publisher("KRSBI/image/garis_tiang/koordinat/w", Float64, queue_size=10)
        self.pub_h = rospy.Publisher("KRSBI/image/garis_tiang/koordinat/h", Float64, queue_size=10)

        self.pub_w_lacth = rospy.Publisher("KRSBI/image/garis_tiang/koordinat/w_lacth", Float64, queue_size=10)
        self.pub_h_lacth = rospy.Publisher("KRSBI/image/garis_tiang/koordinat/h_lacth", Float64, queue_size=10)

        self.rate = rospy.Rate(30)

        self.aspectRatio = rospy.Publisher("KRSBI/image/garis_tiang/koordinat/aspectRatio", String, queue_size=10)
        self.hsv = rospy.Publisher("KRSBI/image/garis_tiang/image_param/hsv", Twist, queue_size=10)
        self.hsv_sub = rospy.Subscriber("KRSBI/image/garis_tiang/image_param/hsv", Twist, self.hsvcallback)

        # self.tresholding = rospy.Publisher("KRSBI/image/garis_tiang/image_param/tresh", Int8, queue_size=10)
        # self.tresholding_sub = rospy.Subscriber("KRSBI/image/garis_tiang/image_param/tresh", Int8, self.treshold_callback)

        # self.image_sub = rospy.Subscriber("usb_cam_node_node/image_raw", Image, self.callback)

        self.state = rospy.Publisher("KRSBI/image/garis_tiang/image/state", String, queue_size=10)

        if rospy.has_param("/tiang_garis_h_low"):

            hsvLower = (rospy.get_param("/tiang_garis_h_low"), rospy.get_param("/tiang_garis_s_low"), rospy.get_param("/tiang_garis_v_low"))
            hsvUpper = (rospy.get_param("/tiang_garis_h_up"), rospy.get_param("/tiang_garis_s_up"), rospy.get_param("/tiang_garis_v_up"))
            # treshold_val = rospy.get_param("/tiang_garis_treshold")
        else:

            hsvLow = (86, 0, 113)
            hsvMax = (116, 255, 255)

        # rosparam.set_param('/usb_cam_node_node/brightness', '10')
        # rosparam.set_param('/usb_cam_node_node/exposure', '10')
        self.i = 0
        # self.ParamUpdate()
        self.bridge = CvBridge()

    def state_tiang(self, status):
        if status == 1:
            self.state.publish("OK")
        elif status == 0:
            self.state.publish("NOTDETECT")

    def hsvcallback(self, data):
        rosparam.set_param('/tiang_garis_h_low', str(data.linear.x))
        rosparam.set_param('/tiang_garis_s_low', str(data.linear.y))
        rosparam.set_param('/tiang_garis_v_low', str(data.linear.z))
        rosparam.set_param('/tiang_garis_h_up', str(data.angular.x))
        rosparam.set_param('/tiang_garis_s_up', str(data.angular.y))
        rosparam.set_param('/tiang_garis_v_up', str(data.angular.z))

    def treshold_callback(self, data):
        rosparam.set_param('/tiang_garis_v_up', str(data.data))

    def callback(self, data):
        global hsvLow, hsvMax, treshold_val

        rosparam.set_param('/usb_cam_node/brightness', '8')
        rosparam.set_param('/usb_cam_node/exposure', '3')

        # tresholding_val = Int8()

        hsvMsg = Twist()
        if rospy.has_param("/tiang_garis_h_low"):

            hsvMsg.linear.x = rospy.get_param("/tiang_garis_h_low")
            hsvMsg.linear.y = rospy.get_param("/tiang_garis_s_low")
            hsvMsg.linear.z = rospy.get_param("/tiang_garis_v_low")
            hsvMsg.angular.x = rospy.get_param("/tiang_garis_h_up")
            hsvMsg.angular.y = rospy.get_param("/tiang_garis_s_up")
            hsvMsg.angular.z = rospy.get_param("/tiang_garis_v_up")
            # tresholding_val.data = rospy.get_param("/tiang_garis_treshold")

        else:
            hsvMsg.linear.x = 86
            hsvMsg.linear.y = 0
            hsvMsg.linear.z = 113
            hsvMsg.angular.x = 116
            hsvMsg.angular.y = 255
            hsvMsg.angular.z = 255
            # tresholding_val.data = 0

        self.hsv.publish(hsvMsg)
        # self.tresholding(tresholding_val)

        hsvLow = np.array([hsvMsg.linear.x, hsvMsg.linear.y, hsvMsg.linear.z])
        hsvMax = np.array([hsvMsg.angular.x, hsvMsg.angular.y, hsvMsg.angular.z])
        # treshold_val = tresholding_val.data

        try:
            # encoding ke blue green red 8 bit
            frame = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)

        # Resize Frame
        lebar = 640
        tinggi = 360
        frame = imutils.resize(frame, width=640)


        # cut_frame = frame[0:360, 0:300]
        # output_blurred = cv2.GaussianBlur(frame, (3, 3), 0)
        # hsv = cv2.cvtColor(output_blurred, cv2.COLOR_BGR2HSV)

        # mask = cv2.inRange(frame, hsvLow, hsvMax)

        ret, frame = cv2.threshold(frame, 127, 255, 0)

        # Step 1: Create an empty skeleton
        size = np.size(frame)
        skel = np.zeros(frame.shape, np.uint8)

        # Get a Cross Shaped Kernel
        element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))

        # Repeat steps 2-4
        while True:
            # Step 2: Open the image
            open = cv2.morphologyEx(frame, cv2.MORPH_OPEN, element)
            # Step 3: Substract open from the original image
            temp = cv2.subtract(frame, open)
            # Step 4: Erode the original image and refine the skeleton
            eroded = cv2.erode(frame, element)
            skel = cv2.bitwise_or(skel, temp)
            frame = eroded.copy()
            # Step 5: If there are no white pixels left ie.. the image has been completely eroded, quit the loop
            if cv2.countNonZero(frame) == 0:
                break

        # Displaying the final skeleton

        cv2.imshow('Shape image', frame)
        cv2.imshow("skel", skel)
        # cv2.imshow('Image Mask', mask)
        # cv2.imshow("out", output)
        # # cv2.imshow('Shape image', img_clone)
        cv2.waitKey(3)

        try:
            self.image_pub.publish(self.bridge.cv2_to_imgmsg(frame, "bgr8"))
            # self.mask_pub.publish(self.bridge.cv2_to_imgmsg(output, "bgr8"))

        except CvBridgeError as e:
            print(e)

        self.rate.sleep()


# ball_detector()


rospy.init_node('processing_image_garis', anonymous=True)

if __name__ == '__main__':
    try:

        objTiang = DeteksiTiang()
        # pubCircle = rospy.Publisher("/ball_detector_node/circle_set", CircleSetStamped, queue_size=1)
        # time.sleep(2.0)
        rospy.spin()
        cv2.destroyAllWindows()

    except rospy.ROSInterruptException:
        pass


