#!/usr/bin/env python3

import rospy
import json

def main():
	config = json.load(open('coffebot.config', 'r'))
	for key in list(config.keys()):
		rospy.set_param(key, config[key])
	

if __name__ == '__main__':
	main()
