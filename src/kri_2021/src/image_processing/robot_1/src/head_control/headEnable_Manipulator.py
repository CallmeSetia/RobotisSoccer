#!/usr/bin/python

import rospy
from std_msgs.msg import Bool

def HeadEnable():
    pub = rospy.Publisher('/KRSBI/Manuvering/headEnable', Bool, queue_size=10)
    rospy.init_node('headEnable_Manipulator', anonymous=False)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        inputCommand = int(input('Head Enable / Disable <1/0> : '))
        rospy.loginfo(inputCommand)
        pub.publish(inputCommand)
        rate.sleep()

if __name__ == '__main__':
    try:
        HeadEnable()
    except rospy.ROSInterruptException:
        pass
