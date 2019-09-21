#include <ros/ros.h>
#include <study_pkg/Control.h>
#include <sstream>

int main(int argc, char **argv)
{
  ros::init(argc, argv, "cpp_control_talker");

  ros::NodeHandle n;

  ros::Publisher pub = n.advertise<study_pkg::Control>("cpp_chatter", 1000);

  ros::Rate loop_rate(1);

  int count = 0;
  while ( ros::ok() )
  {
  	study_pkg::Control msg;
  	msg.speed = 10; 
  	msg.steer = 20; 

    ROS_INFO("Speed: %d / Steer: %d", msg.speed, msg.steer);

    pub.publish(msg);

    ros::spinOnce();

    loop_rate.sleep();
  }

  return 0;
}