#include <ros/ros.h>
#include "study_pkg/Poly.h"

int main(int argc, char **argv)
{
	ros::init(argc, argv, "poly_response_cpp");
	
	ros::NodeHandle n;

	ros::ServiceClient client = n.serviceClient<study_pkg::Poly>("poly");

	study_pkg::Poly srv;
	srv.request.x = 5;

	if (client.call(srv))
	{
	    ROS_INFO("Poly: %ld", (long int)srv.response.y);
	}
	else
	{
	    ROS_ERROR("Failed to call service add_two_ints");
	    return 1;
	}

	return 0;
}