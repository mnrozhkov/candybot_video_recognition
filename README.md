to run coffebot package at Raspberry Pi:

	1. run docker container for candybot_vr docker image:

		sudo docker run -ti --privileged --device /dev:/dev candybot_vr

		(or use shell script with this command)

	2. in docker container:

		cd ~/catkin_ws

		python3 run_coffebot.py
		
		
to run tests:
	
	1. go into folder catkin_ws
	
	2. export packages setups:
	
		source devel/setup.bash
		
	3. to run tests:
	
		3.1. test_core_decision_manager.py:
			
			rosrun coffebot test_core_decision_manager.py
			
		3.2. test_motion_<part>_controller.py:
		
				rosrun coffebot motion_<part>_controller.py
			
			and in another terminal:
			
				do 2.
				
				rosrun coffebot test_motion_<part>_controller.py	
				
