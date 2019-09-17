#!/usr/bin/env python
import rospy
from std_msgs.msg import String

rospy.init_node('even_nums_talker')
pub = rospy.Publisher('my_chat_topic', String, queue_size=10)
rate = rospy.Rate(10)

def start_talker():
    msg = String()
    even_nums = 0
    while not rospy.is_shutdown():
        hello_str = str(even_nums) + " %s" % rospy.get_time()
        rospy.loginfo(hello_str)

        msg.data = hello_str
        pub.publish(msg)
        even_nums += 2
        rate.sleep()

try:
    start_talker()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')