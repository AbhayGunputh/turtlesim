#!/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import sys

def move_turtle(line_vel, ang_vel):
	rospy.init_node('turtle_goto_service', anonymous=True)
	pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	rate = rospy.Rate(10)

	vel = Twist()

	while True:
		vel.linear.x = line_vel
		vel.linear.y = 0
		vel.linear.z = 0

		vel.angular.x = 0
		vel.angular.y = 0
		vel.angular.z = ang_vel

		pub.publish(vel)
		rate.sleep()

if __name__ == '__main__':
	try:
		#move_turtle(float(sys.argv[1]), float(sys.argv[2]))
		move_turtle(int(sys.argv[1]), int(sys.argv[2]))
	except rospy.ROSInterruptException:
		pass
