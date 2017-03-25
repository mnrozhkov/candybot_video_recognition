#!/usr/bin/env python3

import rospy
import json

def main():
	config = json.load(open('coffebot.config', 'r'))
	for key in list(config.keys()):
		rospy.set_param(key, config[key])

	decision_table = json.load(open('DT.json', 'r'))
	rospy.set_param('decision_table', decision_table['table'])

if __name__ == '__main__':
	main()
