from sensor_msgs.msg import JointState
import rospy
#misal
kondisi = 0

pub_ManHeadPan = rospy.Publisher("/KRSBI/Manuvering/HeadPan", Float64, queue_size=1)
pub_ManHeadTilt = rospy.Publisher("/KRSBI/Manuvering/HeadTilt", Float64, queue_size=1)
pub_ManHeadScan = rospy.Publisher("/KRSBI/Manuvering/HeadScan", Bool, queue_size=1)

# pub_HeadJoint = rospy.Publisher("robotis/head_control/set_joint_states", JointState, queue_size=1)
# pub_HeadScan = rospy.Publisher("robotis/head_control/scan_command", String, queue_size=1)

def Motion_HeadScan(enable):
    pub_HeadScan.publish(enable)
    time.sleep(0.1)

def Motion_HeadControl(pan, tilt):
    pub_ManHeadPan.publish(pan)
    time.sleep(0.1)
    pub_ManHeadTilt.publish(tilt)
    time.sleep(0.1)

if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            #misal
            if kondisi == 1:
                headTilt = 0.52
                headPan = 0.20
                Motion_HeadControl(0.0, headTilt)
                Motion_HeadControl(headPan, 0.0)
    except rospy.ROSInterruptException:
        pass



