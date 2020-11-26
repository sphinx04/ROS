#! /usr/bin/python
import rospy
import random

from turtlesim.srv import Spawn, Kill

def turtlespawn(x,y,theta,name):
	rospy.wait_for_service('/spawn')
	spawn_func = rospy.ServiceProxy('/spawn', Spawn)
	spawn_func(x,y,theta,name)
	print("Spawned")

def turtlekill(name):
	rospy.wait_for_service('/kill')
	kill_func = rospy.ServiceProxy('/kill', Kill)
	kill_func(name)
	print("Killed")

class spawner:
	def __init__(self,x,y,theta,name):
		rospy.init_node('turtle_spawner')
		try:
			turtlespawn(x,y,theta,name)
		except rospy.service.ServiceException: 
			turtlekill(name)
			turtlespawn(x,y,theta,name)

if __name__== '__main__':
	s = spawner(random.random() * 10.0, random.random() * 10.0, 0.0,'donatello')
