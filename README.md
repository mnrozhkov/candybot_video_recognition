1. Setup

	1. install docker image candybot_gui

		sudo docker pull meisterurian/candybot_gui

	2. install python3 libraries in docker:

		pip3 install luma.core git+https://github.com/adafruit/Adafruit_Python_PCA9685.git


	3. Run candybot_gui image

	sudo docker run -ti -p 11311:11311 --privileged --device /dev:/dev candybot_gui

	4. Install candybot_v2 ROS package (in docker container):

		1. create catkin workspace:

				mkdir -p ~/catkin_ws/src

				cd ~/catkin_ws

				catkin_make

		2. clone candybot_v2 package:

				cd ~/catkin_ws/src

				git clone https://github.com/FunRobots/candybot_v2.git

		3. build candybot_v2 package:

				in ~/catkin_ws/src/candybot_v2/run:

					- rename software_config.scheme.launch to software_config.launch

					- fill parameters values - software configuration


				cd ~/catkin_ws

				catkin_make

				catkin_make install

	5. install (get) script(s) for convinient work with Candybot system, scripts allow to make run commands shorter:

		cd ~

		git clone https://github.com/FunRobots/scripts.git

2. Run candybot_v2 ROS package

	1. Run candybot_v2 ROS package in running docker container (interactive mode) (see 1.3):

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


	2. run candybot_v2 ROS package on candybot_vr docker container startup:

					a) run candybot_v2 package:

						1) use run python script

							sudo docker run -w="/root/catkin_ws" -ti -p 11311:11311 --privileged --device /dev:/dev candybot_gui /bin/bash -c "source /opt/ros/kinetic/setup.bash; rosrun candybot_v2 run.py"

						2) use roslaunch:

							sudo docker run -w="/root/catkin_ws" -ti -p 11311:11311 --privileged --device /dev:/dev candybot_gui /bin/bash -c "source /opt/ros/kinetic/setup.bash; roslaunch candybot_v2 run.launch"

					b) run just one candybot_v2 package node:

						sudo docker run -w="/root/catkin_ws" -ti -p 11311:11311 --privileged --device /dev:/dev candybot_gui /bin/bash -c "source /opt/ros/kinetic/setup.bash; roslaunch candybot_v2 <node_name>.launch"

					c) with run script (for installation see 1.5):

						cd ~/scripts

						- 1st method (allows to run package only):

								./candybot_vr.sh run_package

								as daemon:

									candybot_vr.sh run_package -d

						- 2nd method (allows to run package and work with image filesystem):

								./candybot_vr.sh enter_package
								roslaunch candybot_v2 run.launch

3. save changes in docker image (commit):

			in Raspbian terminal:

				- list containers and copy candybot_gui id:

					sudo docker container ls

				- commit changes:

					sudo docker commit <candybot_id> <your_image_name>

						(you can save source container locally with any name)


4. Open new terminal in running candybot_vr docker container:

	in new window (for example, in new browser tab with dataplicity.com):

		sudo docker exec -ti candybot_vr /bin/bash


5. Run tests (in running docker container candybot_vr):

	0. in the first terminal run roscore

	in other terminals:

	1. to run tests:

		1. сommon way to run test:

				rosrun candybot_v2 <test_file_name>

		2. some tests require the tested module to be started

			in this case:

			1. run the test module (for example, motion_<part>_controller.py)

			2. in another terminal (see 4.) do 5.1.1
