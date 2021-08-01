import rospy
import time
import math
import random
from std_msgs.msg import Bool
from kri_2021.msg import BolaKoordinat, BallState
from std_msgs.msg import Float64

class HeadTracking:
    bolaStatus, bolaPosY, lastBolaPosY = 0, 0, 0
    HeadStatus = 0
    def __init__(self):
        self.HeadState = rospy.Subscriber("/KRSBI/Manuvering/headEnable", Bool, self.headState_Callback)
        self.BallState = rospy.Subscriber("/KRSBI/image_processing/deteksi_bola/ball_state", BallState, self.ballState_Callback)

        self.pub_ManHeadPan = rospy.Publisher("/KRSBI/Manuvering/HeadPan", Float64, queue_size=1)
        self.pub_ManHeadTilt = rospy.Publisher("/KRSBI/Manuvering/HeadTilt", Float64, queue_size=1)
        self.pub_ManHeadScan = rospy.Publisher("/KRSBI/Manuvering/HeadScan", Bool, queue_size=1)

    def ballState_Callback(self, ballStateData):
        HeadTracking.bolaStatus = ballStateData.bola_state
        HeadTracking.bolaPosY = ballStateData.bola_inFrame_Pos
        HeadTracking.lastBolaPosY = ballStateData.last_bola_inFrame_Pos

    def headState_Callback(self, headCallback):
        if headCallback.data == True:
            HeadTracking.HeadStatus = 1
        elif headCallback.data == False:
            HeadTracking.HeadStatus = 0

    def Motion_HeadScan(self, enable):
        self.pub_HeadScan.publish(enable)
        time.sleep(0.1)

    def Motion_HeadControl(self, pan, tilt):
        self.pub_ManHeadPan.publish(pan)
        time.sleep(0.1)
        self.pub_ManHeadTilt.publish(tilt)
        time.sleep(0.1)

    def Ticks(self):
        ticking = int(time.time() * 1000)
        return ticking


if __name__ == '__main__':
    try:
        rospy.init_node('headTacking', anonymous=False)
        HeadTrack = HeadTracking()
        headTilt = 0.0

        HeadTrack.Motion_HeadControl(-0.0, headTilt)
        time.sleep(2.0)
        while not rospy.is_shutdown():
            # print("NANA")
            # print("BALL STATE : {} - LASTBOLAPOS Y PIXL : {} - HEAD AVAILABLE? : {} ".format(HeadTrack.bolaStatus, HeadTrack.lastBolaPosY, HeadTrack.HeadStatus))

            if HeadTrack.HeadStatus == 1: #enable
                if HeadTrack.bolaStatus == True or HeadTrack.bolaStatus == False :
                    if int(HeadTrack.lastBolaPosY) == 2: # Atas
                        headTilt += 0.1
                        if headTilt > 1.5:   # Limit
                            headTilt = 1.5
                        HeadTrack.Motion_HeadControl(-0.0, headTilt)

                    elif int(HeadTrack.lastBolaPosY) == 1:  # bawah
                        headTilt -= 0.1

                        if headTilt < -1.2: # Limit
                            headTilt = -1.2

                        HeadTrack.Motion_HeadControl(-0.0, headTilt)

                    elif int(HeadTrack.lastBolaPosY) == 0:
                        pass

    except rospy.ROSInterruptException:
        pass