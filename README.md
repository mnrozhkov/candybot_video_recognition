# candybot_video_recognition
Module for CandyBot to help recognise people and objects via web-cam


Libraries list and intallation instruction:

I. Python libraries:
	
	1. rospkg, catkin_pkg - ros libraries for Python 3.5:
	
		sudo pip3 install rospkg, catkin_pkg
		
	2. pocketsphinx - speech recognition library:
	
		sudo pip3 install pocketsphinx
		
	3. pyaudio - audio record library, depends on avbin package https://github.com/downloads/AVbin/AVbin/install-avbin-linux-x86-64-v10:
		
		sudo pip3 install pyaudio
		
	4. wikipedia - Python API Wiki library:
		
		sudo pip3 install wikipedia
		
	
II. Non-Python libraries:

	1. ROS Kinetic (official recommended way):
		
		1.1. follow link http://wiki.ros.org/Installation
		
		1.2. choose your OS
		
		1.3. follow instructions
		
	2. OpenCV:
		
		You can use two links:
		
			- instruction from official site http://docs.opencv.org/3.1.0/d7/d9f/tutorial_linux_install.html
			
			- short instruction from askubuntu http://askubuntu.com/questions/783956/how-to-install-opencv-3-1-for-python-3-5-on-ubuntu-16-04-lts
			
			WARNING! : you can use both links following your intuition... and knowledge, of course 
			WARNING! : if Python 3.5 already installed in your system pass Python-installation steps
			ACHTUNG!! : DO NOT USE OPENCV INSTALLATION INSTRUCTION FOR PYTHON VERSION LESS THAN 3.5
		
	3. RHVoice - speech synthesis library:
	
		https://launchpad.net/~linvinus/+archive/ubuntu/rhvoice
		
	
		
-------------------------------------------------------------------------------------------------------
