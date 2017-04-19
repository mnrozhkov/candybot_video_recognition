#!/usr/bin/env python3
import sys
from pathlib import Path
BASE_PATH = Path(__file__).resolve().parents[0].as_posix()
catkin_ws = Path(__file__).resolve().parents[3].as_posix()
sys.path.append(catkin_ws)

import subprocess
import rospy

subprocess.Popen(['roscore'])
ros_started = False
while not ros_started:
	try:
		rospy.get_master().getPid()
		ros_started = True
	except:
		pass

subprocess.call(['python3', BASE_PATH + '/coffebot_config.py'])
subprocess.call(['bash', BASE_PATH + '/run_coffebot.sh'])
