# candybot_video_recognition
Module for CandyBot to help recognise people and objects via web-cam

To run ROS package:

	1. create catkin workspace (http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment) *

	2. copy package content to <catkin_workspace>/scr **

	3. in terminal choose directory: $cd <catkin_workspace> 

	4. build packages: $catkin_make **

	5. add package path and set up $PYTHONPATH: $source devel/setup.bash ***
	
	6. to add to $PYTHONPATH Python 3 libraries path do: $export PYTHONPATH=/usr/local/lib/python3.5/dist-packages:$PYTHONPATH ***

	7. to run nodes: 
		
		7.1. change nodes execution rights *:

			7.1.1. choose folder <catkin_workspace>/scr/candybot_vr/scripts

			7.1.2. $chmod +x desicion_maker.py listener.py viewer.py

		7.2. in new terminal: $roscore ***

		7.3. in another new terminal: $rosrun candybot_vr decision_maker.py ***
		
		7.4. in another new terminal: $rosrun candybot_vr listener.py ***

		7.5. in another new terminal: $rosrun candybot_vr viewer.py ***

* - do once
** -  do where package is changed
*** - do every time to run nodes
