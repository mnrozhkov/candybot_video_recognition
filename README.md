to run coffebot package at Raspberry Pi:

	1. run docker container for candybot_vr docker image:

		sudo docker run -ti --privileged --device /dev:/dev candybot_vr

		(or use shell script with this command)

	2. in docker container:

		cd ~/catkin_ws

		python3 run_coffebot.py
