#!/usr/bin/python

# import the necessary packages
import sys
import os
import rospy
import rosparam
from std_msgs.msg import Int8

from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from kri_2021.msg import BolaKoordinat, BallState

from geometry_msgs.msg import Point
from geometry_msgs.msg import Twist

import numpy as np
import cv2
import time


class DeteksiBola_Pink:

    trackbar = False
    hsvLower, hsvUpper, MinRadius = [158, 55, 79], [178, 200, 255], 5
    Kecerahan, Kontras = 0, 0 # default

    fokalLensaKamera = 0.0
    lebarBola_Real = 14.6 #cm

    gmbr1 = '/home/robotis/RobotisSoccer/src/kri_2021/src/image_processing/robot_1/src/bola_pink.png'

    def __init__(self, UseTrackbar = False):
        self.bridge = CvBridge()
        if self.kalibrasiGambar_Bola(DeteksiBola_Pink.gmbr1, jarakObjek_REAL=64.2) is True:
            rospy.loginfo("FOKAL LENSA KAMERA : {} ".format(DeteksiBola_Pink.fokalLensaKamera))
        else :
            rospy.warninfo("GAGAL KALIBRASI GAMBAR BOLA PINK")

        self.image_sub = rospy.Subscriber("usb_cam_node/image_raw", Image, self.callback_image)
        self.mask_pub = 0
        self.koordinatBola = rospy.Publisher("KRSBI/image_processing/deteksi_bola/coordinate/", BolaKoordinat, queue_size=10)
        self.ballState = rospy.Publisher("KRSBI/image_processing/deteksi_bola/ball_state", BallState, queue_size=10)
        self.ballState_LastPos = -1
        if UseTrackbar is True:
            DeteksiBola_Pink.trackbar = True

            rosparam.set_param('/bola_h_low', str(DeteksiBola_Pink.hsvLower[0]))
            rosparam.set_param('/bola_s_low', str(DeteksiBola_Pink.hsvLower[1]))
            rosparam.set_param('/bola_v_low', str(DeteksiBola_Pink.hsvLower[2]))
            rosparam.set_param('/bola_h_up', str(DeteksiBola_Pink.hsvUpper[0]))
            rosparam.set_param('/bola_s_up', str(DeteksiBola_Pink.hsvUpper[1]))
            rosparam.set_param('/bola_v_up', str(DeteksiBola_Pink.hsvUpper[2]))

            rosparam.set_param('/cam_kecerahan', str(DeteksiBola_Pink.Kecerahan))
            rosparam.set_param('/cam_kontras', str(DeteksiBola_Pink.Kontras))

        else:
            self.mask_pub = 0
            DeteksiBola_Pink.trackbar = False

        self.rate = rospy.Rate(30)

    def nothing(self):
        pass

    def state_bola(self, status, pos_y = -1, last_pos_y = -1):

        stateBola = BallState()
        if status == 1:
            stateBola.bola_state = bool(True)
        else:
            stateBola.bola_state = bool(False)

        stateBola.bola_inFrame_Pos = str(pos_y)
        stateBola.last_bola_inFrame_Pos =str(last_pos_y)

        self.ballState.publish(stateBola)

    def resizeFrame (self, image, width=None, height=None, interpolasi=cv2.INTER_AREA):
        dim = None
        w = image.shape[1]
        h = image.shape[0]

        if width is None and height is None:
            return image

        if width is None:
            r = height / float(h)
            dim = (int(w * r), height)

        else:
            r = width / float(w)
            dim = (width, int(h * r))

        resized = cv2.resize(image, dim, interpolation=interpolasi)
        return resized

    def filterFrame(self, frame):
        frame = self.resizeFrame(frame, width=450)
        return frame

    def get_Kontur(self, kontur):
        if len(kontur) == 2:
            kontur = kontur[0]
        elif len(kontur) == 3:
            kontur = kontur[1]

        return kontur


    def get_LuasKontur(self, contours):
        all_kontur = []
        for cnt in contours:
            area = cv2.contourArea(cnt)
            all_kontur.append(area)

        return all_kontur
    def kalibrasiGambar_Bola (self, src_gambar, jarakObjek_REAL = 60) :
        src_gambar = cv2.imread(src_gambar)

        lowerHsv = np.array([158, 55, 79])
        upperHsv = np.array([178, 200, 255])
        kernel = np.ones((5, 5), np.uint8)

        src_gambar = self.filterFrame(src_gambar)
        lebarFrame = src_gambar.shape[1]
        tinggiFrame = src_gambar.shape[0]
        mask = cv2.inRange(cv2.cvtColor(src_gambar, cv2.COLOR_BGR2HSV), lowerHsv, upperHsv)

        mask = cv2.dilate(cv2.morphologyEx(mask, cv2.MORPH_CLOSE,
                          cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))),
                          cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)),
                          iterations=3)
        mask = cv2.erode(mask, kernel, iterations=2)
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]  #

        if (len(cnts) > 0):

            sortedKontur = sorted(cnts, key=cv2.contourArea, reverse=True)
            x, y, x_ball, y_ball, radius, center, flag = self.DeteksiBola_Kontur(sortedKontur,
                                                                                 lebarFrame,
                                                                                 tinggiFrame,
                                                                                  5)

            if flag > 0:
                diameter = float(radius * 2)
                DeteksiBola_Pink.fokalLensaKamera = self.fokalKamera(jarakObjek_REAL, DeteksiBola_Pink.lebarBola_Real, diameter)
                return True
            else:
                return False
    def setKecerahan_Kontras(self, gmbr, kecerahan=0.0, kontras=0.0, beta_parameter = 0):
        return cv2.addWeighted(gmbr, 1 + float(kontras) / 100.0, gmbr, beta_parameter, float(kecerahan))

    def fokalKamera (self, lebarObjek_Gambar, jarakRealDariKamera, lebarObjek_Real ):
        fokalKamera = (lebarObjek_Real * lebarObjek_Gambar) / jarakRealDariKamera
        return fokalKamera

    def jarakDariKamera(self,lebarObjek_Real, fokalKamera, lebarObjek_Gambar ):
        jarak =  (lebarObjek_Real * fokalKamera) / lebarObjek_Gambar
        return jarak

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
        # print("PROCESSING")
        try:
            frame = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)

        frame = self.filterFrame(frame)

        lebarFrame =    frame.shape[1]
        tinggiFrame =   frame.shape[0]

        # rospy.loginfo("LEBAR FRAME : {} - TINGGI FRAME : {} ".format(lebarFrame, tinggiFrame))
        frame = cv2.GaussianBlur(frame, (11, 11), 0)


        kernel = np.ones((5, 5), np.uint8)

        if DeteksiBola_Pink.trackbar is True:
            if rospy.has_param("/bola_h_low"):
                DeteksiBola_Pink.hsvLower = [rospy.get_param("/bola_h_low"), rospy.get_param("/bola_s_low"), rospy.get_param("/bola_v_low")]
                DeteksiBola_Pink.hsvUpper = [rospy.get_param("/bola_h_up"), rospy.get_param("/bola_s_up"), rospy.get_param("/bola_v_up")]

                DeteksiBola_Pink.Kecerahan = rospy.get_param("/cam_kecerahan")
                DeteksiBola_Pink.Kontras = rospy.get_param("/cam_kontras")

        H_min = DeteksiBola_Pink.hsvLower[0]
        H_max = DeteksiBola_Pink.hsvUpper[0]
        S_min = DeteksiBola_Pink.hsvLower[1]
        S_max = DeteksiBola_Pink.hsvUpper[1]
        V_min = DeteksiBola_Pink.hsvLower[2]
        V_max = DeteksiBola_Pink.hsvUpper[2]
        Min_Radius = DeteksiBola_Pink.MinRadius

        frame = self.setKecerahan_Kontras(frame, DeteksiBola_Pink.Kontras, DeteksiBola_Pink.Kecerahan)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_yellow = np.array([H_min, S_min, V_min])
        upper_yellow = np.array([H_max, S_max, V_max])

        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
        kernels_0 = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernels_0)
        closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7)))

        mask = cv2.dilate(closing, kernel, iterations=3)
        # mask = cv2.dilate(mask, kernel, iterations=1)
        mask = cv2.erode(mask, kernel, iterations=2)

        result = cv2.bitwise_and(frame, frame, mask=mask)

        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]  #
        flag, pos_y = 0, -1

        if (len(cnts) > 0):

            sortedKontur = sorted(cnts, key=cv2.contourArea, reverse=True)
            x, y, x_ball, y_ball, radius, center, flag = self.DeteksiBola_Kontur(sortedKontur, lebarFrame, tinggiFrame, Min_Radius)
            lokasiBolaFrame = -1
            if flag > 0:
                cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                cv2.circle(frame, center, 3, (0, 0, 255), -1)
                cv2.putText(frame, "BOLA", (center[0] + 10, center[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0), 1)
                cv2.putText(frame, "(" + str(center[0]) + "," + str(center[1]) + ")", (center[0] + 10, center[1] + 15),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)

                diameter = float(radius * 2)
                jarak = self.jarakDariKamera(DeteksiBola_Pink.fokalLensaKamera, DeteksiBola_Pink.lebarBola_Real, diameter)

                x_filter = (x / lebarFrame) * 2 - 1
                y_filter = (y / tinggiFrame) * 2 - 1

                if center[1] < 85 :
                    pos_y = 2
                elif center[1] > (tinggiFrame - 85) :
                    pos_y = 1
                else :
                    pos_y = 0

                self.ballState_LastPos = pos_y

                koordinatMsg = BolaKoordinat()
                koordinatMsg.x_bola = float(x_filter)
                koordinatMsg.y_bola = float(y_filter)
                koordinatMsg.z_bola = float(jarak)

                koordinatMsg.x_pixel = float(x)
                koordinatMsg.y_pixel = float(y)
                koordinatMsg.radius  = float(radius)

                self.koordinatBola.publish(koordinatMsg)
            else:
                pos_y = -1

        self.state_bola(flag, pos_y, self.ballState_LastPos)

        cv2.line(frame, (0, 85), (lebarFrame, 85), (255, 0, 0), 4)

        cv2.line(frame, (0, (tinggiFrame//2)-20), (lebarFrame, (tinggiFrame//2) - 20), (255, 0, 0), 4)
        cv2.line(frame, (0, (tinggiFrame//2)+20), (lebarFrame, (tinggiFrame//2) + 20), (255, 0, 0), 4)
        cv2.line(frame, (0, (tinggiFrame - 85)), (lebarFrame, (tinggiFrame - 85)), (255, 0, 0), 4)

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
        while not rospy.is_shutdown():
            rospy.init_node('processing_image_bola', anonymous=False)
            DeteksiBola_Pink(UseTrackbar=False)
            rospy.spin()
    except rospy.ROSInterruptException:
        cv2.destroyAllWindows()
        pass