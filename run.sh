#!/bin/bash

source devel/setup.bash
export PYTHONPATH=/usr/local/lib/python3.5/dist-packages:$PYTHONPATH
echo $PYTHONPATH

rosrun candybot_vr rms.py & rosrun candybot_vr decision_maker.py & rosrun candybot_vr listener.py & rosrun candybot_vr viewer.py
