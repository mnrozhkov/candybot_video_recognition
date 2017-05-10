#!/usr/bin/env python3
import sys
from pathlib import Path
BASE_PATH = Path(__file__).resolve().parents[0].as_posix()

import rospy
import json

import os

if __name__ == '__main__':
	rospy.init_node('coffebot_config')
	print(BASE_PATH)
	config = json.load(open(BASE_PATH + '/coffebot.config', 'r'))
	for key in list(config.keys()):
		rospy.set_param(key, config[key])
