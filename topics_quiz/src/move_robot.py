#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

rospy.init_node("quiz_topics")
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
move_robot = Twist()


def callback(msg):

    if msg.ranges(360) > 1 :
        move_robot.linear.x = 1
        move_robot.angular.z = 0

    if msg.ranges(360) < 1 :
        move_robot.linear.x = 0.5
        move_robot.angular.z = 0.1

    if msg.ranges(0) < 1:
        move_robot.linear.x = 0.5
        move_robot.linear.z = 0.1

    if msg.ranges(719) < 1:
        move_robot.linear.x = 0.5
        move_robot.angular.z = -0.1

    pub.publish(move_robot)




sub = rospy.Subscriber("/scan", LaserScan, callback)


rospy.spin()