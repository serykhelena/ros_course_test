#!/usr/bin/env python
#
import rospy
import tf
from tf.transformations import quaternion_from_euler
from turtlesim.msg import Pose
import math 

# Register node / fake node name - we will rename =)
rospy.init_node('tf_turtle')
# Get private parameter / make it global variable
turtlename = rospy.get_param('~turtle_tf_name')
# Callback function
def handle_turtle_pose(msg):
    # Get broadcaster object
    br = tf.TransformBroadcaster()

    # Broadcast TF trasform (world -> turtlename)
    br.sendTransform((msg.x, msg.y, 0),
                     quaternion_from_euler(0, 0, msg.theta),
                     rospy.Time.now(),
                     turtlename,
                     "world")

def handle_carrot_pose(msg):
    carrot = tf.TransformBroadcaster()
    omega = 100
    info = Pose()
    now = rospy.Time.now()
    carrot_x = info.x + 0.5 * math.cos(omega * now.nsecs)
    carrot_y = info.y + 0.5 * math.sin(omega * now.nsecs)

    carrot.sendTransform((carrot_x, carrot_y, 0),
                         quaternion_from_euler(0, 0, info.theta),
                         rospy.Time.now(),
                         "carrot",
                         turtlename
        )

# Subscribe to /input_pose topic - just gonna remap it to work with
rospy.Subscriber('input_pose',
                 Pose,
                 handle_carrot_pose)
# You spin my head right round, right round - Florida =)
# Just handle all topic messages until node (or ROS) is working
rospy.spin()