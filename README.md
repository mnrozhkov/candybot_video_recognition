1. Setup

	1.1. install docker image candybot_vr

		sudo docker pull funrobots/candybot_vr

	1.2. install python3 libraries in docker:

		pip3 install luma.core git+https://github.com/adafruit/Adafruit_Python_PCA9685.git


	1.3. Run candybot_vr image

	sudo docker run -ti --privileged --device /dev:/dev candybot_vr

	1.4. Install candybot_v2 ROS package (in docker container):

		1.4.1. create catkin workspace:

				mkdir -p ~/catkin_ws/src

				cd ~/catkin_ws

				catkin_make

		1.4.2. clone candybot_v2 package:

				cd ~/catkin_ws/src

				git clone https://github.com/FunRobots/candybot_v2.git

		1.4.3. build candybot_v2 package:

				in ~/catkin_ws/src/candybot_v2/run:

					- rename software_config.scheme.launch to software_config.launch

					- fill parameters values - software configuration


				cd ~/catkin_ws

				catkin_make

				catkin_make install

	1.5 Run candybot_v2 ROS package (in docker container):

		1.5.1. run candybot_v2 package in container interactive mode:

				a) use run python script:

					rosrun candybot_v2 run.py

				b) use roslaunch:

					roslaunch candybot_v2 run.launch

				c) run just one candybot_v2 package node:

					1st method:

						roscore

						in another terminal (see point 3):

							rosrun candybot_v2 <node_name>

					2nd method:

						roslaunch candybot_v2 <node_name>.launch		



		1.5.2. run candybot_v2 ROS package on candybot_vr docker container startup:

				a) run candybot_v2 package:

					1) use run python script

						sudo docker run -w="/root/catkin_ws" -ti --privileged --device /dev:/dev candybot_vr /bin/bash -c "source /opt/ros/kinetic/setup.bash; rosrun candybot_v2 run.py"

					2) use roslaunch:

						sudo docker run -w="/root/catkin_ws" -ti --privileged --device /dev:/dev candybot_vr /bin/bash -c "source /opt/ros/kinetic/setup.bash; roslaunch candybot_v2 run.launch"

				b) run just one candybot_v2 package node:

					sudo docker run -w="/root/catkin_ws" -ti --privileged --device /dev:/dev candybot_vr /bin/bash -c "source /opt/ros/kinetic/setup.bash; roslaunch candybot_v2 <node_name>.launch"


	1.6. save changes in docker image (commit):

		in Raspbian terminal:

			- list containers and copy candybot_vr id:

				sudo docker container ls

			- commit changes:

				sudo docker commit <candybot_id> <your_image_name>

					(you can save source container locally with any name)


3. Open new terminal in running candybot_vr docker container:

	in new window (for example, in new browser tab with dataplicity.com):

		sudo docker exec -ti candybot_vr /bin/bash


4. Run tests (in running docker container candybot_vr):

	0. in the first terminal run roscore

	in other terminals:

	1. to run tests:

		1.1.сommon way to run test:

				rosrun candybot_v2 <test_file_name>

		1.2. some tests require the tested module to be started

			in this case:

			1. run the test module (for example, motion_<part>_controller.py)

			2. in another terminal (see 3.) do 4.1 - 4.3.1
