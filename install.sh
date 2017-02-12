apt-get python3-pip

#install ROS
sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116

apt-get update

apt-get install ros-kinetic-ros-base

pip3 install rospkg catkin_ws
#end-ROS-installation------------------------------------

#install OpenCV
apt-get install build-essential cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev python3.5-dev python3-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev

git clone https://github.com/Itseez/opencv.git

mv opencv opencv-3

cd opencv-3

mkdir build; cd build

cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local ..

make

make install
#end-OpenCV-installation --------------------------------

#install libraries for audio and speech
apt-get install python3-pyaudio swig libpulse-dev

add-apt-repository ppa:linvinus/rhvoice
apt-get update
apt-get install speech-dispatcher-rhvoice rhvoice-russian rhvoice-english

./install-avbin-linux-x86-64-v10

pip3 install pocketsphinx pyaudio

#end-audio-libraries-installation------------------------

#WIKI API library install
pip3 install wikipedia
#end-WIKI-API-library------------------------------------
