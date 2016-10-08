#!/bin/bash
#1.remove this script to <catkin_workspace>
#2.in new terminal run roscore
#3.in old terminal run this script: $chmod +x run.sh
#				    $./run.sh

source devel/setup.bash
export PYTHONPATH=/usr/local/lib/python3.5/dist-packages:$PYTHONPATH

rosrun candybot_vr decision_maker.py & rosrun candybot_vr listener.py & rosrun candybot_vr viewer.py
