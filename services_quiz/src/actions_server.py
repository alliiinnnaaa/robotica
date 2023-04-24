#! /usr/bin/env python

import rospy
import time
from services_quiz.srv import CustomActMess, CustomAcyMessResponse
from math import sqrt
from geometry_msgs.msg import Twist



def my_callback(request):
    rospy.loginfo("Service move in square has been called")
    vel.linear.x = 0.5
    vel.angular.z = 0


    pub.publish(vel)

    return CustomAcyMessResponse(True)


rospy.init_node('service_server')
my_service = rospy.Service('/move_in_square', CustomActMess, my_callback)
pub = rospy.Publisher('/mobile_base_controller/cmd_vel', Twist, queue_size=1)
vel = Twist()
rate = rospy.Rate(2)
rospy.spin()


