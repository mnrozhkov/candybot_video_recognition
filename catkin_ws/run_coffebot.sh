#!/bin/bash

source devel/setup.bash
export PYTHONPATH=/usr/local/lib/python3.5/dist-packages:$PYTHONPATH
echo $PYTHONPATH

rosrun coffebot decisions.py & rosrun coffebot viewer.py & rosrun coffebot rms.py & rosrun coffebot listener.py
