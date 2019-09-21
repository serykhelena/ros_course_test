#!/usr/bin/env python
import rospy
from study_pkg.msg import Control

rospy.init_node('control_talker')
pub = rospy.Publisher('my_chat_topic', Control, queue_size=10)
rate = rospy.Rate(1)

def start_talker():
    msg = Control()
    msg.steer = 40
    msg.speed = 10

    while not rospy.is_shutdown():
        rospy.loginfo('PY Speed: %d / Stter: %d' % (msg.speed, msg.steer))

        pub.publish(msg)
        rate.sleep()

try:
    start_talker()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')