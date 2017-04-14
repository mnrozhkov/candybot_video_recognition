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

subprocess.call(['./coffebot_config.py'])
subprocess.call(['./run_coffebot.sh'])

