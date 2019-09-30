#!/usr/bin/env python

import rospy
rospy.init_node('params_study')

distro = rospy.get_param('/rosdistro')

my_set_param = rospy.get_param('my_set')
my_private_param = rospy.get_param('~private_param', 'default_value')

rospy.set_param('~ros_priv_param', 'Hi, I am private =)')
rospy.set_param('ros_loc_param', 'Hi, I am local =)')
rospy.set_param('/ros_glob_param', 'Hi, I am global =)')