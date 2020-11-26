#! /usr/bin/python

import rospy

from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from math import pow, atan2, sqrt

class my_class:
	def __init__(self):
		rospy.init_node('my_listener')
		
		name = 'donatello'
		self.pub = rospy.Publisher(name + '/cmd_vel', Twist, queue_size = 1)

		self.sub = rospy.Subscriber(name + '/pose', Pose, self.info)
		self.subtarget = rospy.Subscriber('/turtle1/pose', Pose, self.targetinfo)

		self.pose = Pose()
		self.target_pose = Pose()

		self.rate = rospy.Rate(10)
	
	def info(self, msg):		
		self.pose = msg

	def targetinfo(self, msg):		
		self.target_pose = msg

		vel_msg = Twist()
		vel_msg.linear.x = self.linear_velocity()
		vel_msg.linear.y = 0
		vel_msg.linear.z = 0

		vel_msg.angular.x = 0
		vel_msg.angular.y = 0
		vel_msg.angular.z = self.angular_velocity()

		self.pub.publish(vel_msg)

	def euclidean_distance(self):
		return sqrt(pow((self.target_pose.x-self.pose.x), 2) + pow((self.target_pose.y-self.pose.y), 2))

	def linear_velocity(self, constant = 0.33):
		return constant * self.euclidean_distance()
	
	def steering_angle(self):
		return atan2(self.target_pose.y - self.pose.y, self.target_pose.x - self.pose.x)

	def angular_velocity(self, constant = 5):
		return constant * (self.steering_angle() - self.pose.theta)

if __name__== '__main__':
	m = my_class()
	while not rospy.is_shutdown():	
		rospy.spin()


	
