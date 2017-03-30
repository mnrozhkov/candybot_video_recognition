#!/usr/bin/env python3

import rospy
import std_msgs

from coffebot.motion import joint_control, head_control, body_control
from coffebot.core import emotion_manager

import json


if __name__ == '__main__':

    rospy.init_node('core_motion_manager')

    motion_publisher = rospy.Publisher('motion', std_msgs.msg.String, queue_size=1)


    def callback_pattern(data: std_msgs.msg.String) -> None:
        pass


    def callback_emotion(data: std_msgs.msg.String) -> None:
        pass

    
    def callback_position(data: std_msgs.msg.String) -> None:
        pass


    rospy.Subscriber('pattern', std_msgs.msg.String, callback_pattern)
    rospy.Subscriber('emotion', std_msgs.msg.String, callback_emotion)
    rospy.Subscriber('position', std_msgs.msg.String, callback_position)

    rospy.spin()
