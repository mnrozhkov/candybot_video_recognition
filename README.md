1. Setup

	1.1. install docker image candybot_vr
	
		sudo docker pull funrobots/candybot_vr
		
	1.2. install python3 libraries in docker:
		
		pip3 install luma.core git+https://github.com/adafruit/Adafruit_Python_PCA9685.git
		

2. Run candybot_vr image

	sudo docker run -ti --privileged --device /dev:/dev candybot_vr
	(or use shell script with this command)


3. Run coffebot ROS package:

	if coffebot package does not exist localy:
	
		go into folder catkin_ws:
	
			cd ~/catkin_ws/src
	
		clone coffebot package:
		
			git clone https://github.com/FunRobots/candybot_vr.git -b dev coffebot
		
	run coffebot package:
	
		cd ~/catkin_ws
		
		rosrun coffebot run.py
	
	run just one coffebot package node:
		
		cd ~/catkin_ws
		
		roscore
		
		in another terminal:
			
			cd ~/catkin_ws
			
			source devel/setup.bash
			
			rosrun coffebot <node_name>
			
4. Open new terminal in running candybot_vr docker container:

	in new window (for example, in new browser tab with dataplicity.com):
	
		sudo docker container ls
	
	keep in mind name or id of candybot_vr container
	
		sudo docker exec -ti <container_name>/<container_id> /bin/bash
		
	OR
	
	if you are sure candybot_vr is the last running container:
	
		sudo docker exec -ti $(sudo docker container ls -lq) /bin/bash
		
		
		
5. Run tests:
	
	1. go into folder catkin_ws:
	
		cd ~/catkin_ws
	
	2. export packages setups:
	
		source devel/setup.bash
		
	3. to run tests:
	
		3.1.сommon way to run test:
		
				rosrun coffebot <test_file_name>
			
		3.2. some tests require the test module to be started
			in this case:
		
			1. run the test module (for example, motion_body_controller)
		
			2. in another terminal (see 4.) do 5.1 - 5.3.1
