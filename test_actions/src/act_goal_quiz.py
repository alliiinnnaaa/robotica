#! /usr/bin/env python
import rospy
import time
import actionlib
from test_actions.msg import CustomActSerFeedback, CustomActSerResult, CustomActSerAction
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty

class CustomActSerClass(object):
    
  _feedback = CustomActSerFeedback()
  _result   = CustomActSerResult()

  def __init__(self):
    self._as = actionlib.SimpleActionServer("action_custom", CustomActSerAction, self.callback, False)
    self._as.start()

    
  def callback(self, goal):
    success = True
    r = rospy.Rate(1)
    
    self._takeoff = rospy.Publisher('/ardrone/takeoff', Empty, queue_size=1)
    self._takeoff_msg = Empty()
    self._land = rospy.Publisher('/ardrone/land', Empty, queue_size=1)
    self._land_msg = Empty()
    
    takeoff_or_land = goal.goal
    
    i = 0
    for i in xrange(0, 4):
    
      if self._as.is_preempt_requested():
        self._as.set_preempted()
        success = False
        break
    
      if takeoff_or_land == 'TAKEOFF':
        
        self._takeoff.publish(self._takeoff_msg)
        self._feedback.feedback = 'Taking off...'
        self._as.publish_feedback(self._feedback)
    
      if takeoff_or_land == 'LAND':
        
        self._land.publish(self._land_msg)
        self._feedback.feedback = 'Landing...'
        self._as.publish_feedback(self._feedback)
    
      r.sleep()
    
    if success:
      self._result = Empty()
      self._as.set_succeeded(self._result)
      rospy.loginfo("Goal succeded...")
      
      
if __name__ == '__main__':
    rospy.init_node('goal_actions')
    CustomActSerClass()
    rospy.spin()