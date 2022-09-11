#!/bin/env python3
import roslib
roslib.load_manifest('learning_tf')
import rospy
import math
import math
import tf
import geometry.msgs.msg
import turtlesim.srv

if __name__ == '__main__':
	rospy.init_node('turtle_publisher')
	sub = tf.TransformListener()

	rospy.wait_for_service('spawn')
	spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
	spawner(4,2,0, 'turtle2')

	vel = rospy.Publisher('turtle2/cmd_vel',geometry_msgs.msg.Twist,queue_size=10)

	rate = rospy.Rate(10)
	while True:
		try:
			(trans,rot) = sub.lookupTransform('/turtle2','/turtle1', rospy.Time(0))
		except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
			contiue

		angular = 4 * math,atan2(trans[1], trans[0])
		linear = 0.5 * math.sqrt(trans[0] ** 2 + trans[1] ** 2)
		cmd = geometry_msgs.msg.Twist()
		cmd.linear.x = linear
		cmd.angular.z = angular
		turtle_vel.publish(cmd)
		rate.sleep()
