#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import sys


def turtle_circle(radius,x,y):
	rospy.init_node('turtle_circle', anonymous=True)
	pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	rate = rospy.Rate(10)

	vel = Twist()
	while True:
		vel.linear.x = radius
		vel.linear.y = x
		vel.linear.z = y

		vel.angular.x = 0
		vel.angular.y = 0
		vel.angular.z = 1

		rospy.loginfo("The radius = %f", radius)

		pub.publish(vel)
		rate.sleep()

if __name__ == '__main__':
	try:
		turtle_circle(float(sys.argv[1]), float(sys.argv[2]),float(sys.argv[3]))
	except rospy.ROSInterruptException:
		pass

