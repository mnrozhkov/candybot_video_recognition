apt-get python3-pip

#install ROS
apt-get install ros-kinetic-ros-base

pip3 install rospkg catkin_ws
#end-ROS-installation------------------------------------

#install OpenCV
apt-get install build-essential cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev python3.5-dev python3-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev

git clone https://github.com/Itseez/opencv.git

mv opencv opencv-3

cd opencv-3

mkdir build; cd build

cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local ../opencv-3

make

make install
#end-OpenCV-installation --------------------------------


#install libraries for audio
apt-get install python3-pyaudio swig libpulse-dev

pip3 install pocketsphinx pyaudio

#end-audio-libraries-installation------------------------

#WIKI API library install
pip3 install wikipedia
#end-WIKI-API-library------------------------------------

#dlib for Python install
git clone https://github.com/davisking/dlib.github

cd dlib

python3 setup.py install

#end-dlib-for-Python-installation------------------------
