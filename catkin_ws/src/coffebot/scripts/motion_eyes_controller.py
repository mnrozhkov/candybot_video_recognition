#!/usr/bin/env python3

import rospy
import std_msgs

import json
from coffebot.motion.head_control import Eyes

if __name__ == '__main__':

    rospy.init_node('motion_head_controller')
    eyes = Eyes()

    def callback_eyes_motion(data: std_msgs.msg.String, queue_size=1):
        eyes_motion = json.loads(data.data)
        eyes.set_pupil_position(eyes_motion['set_pupil_position'])

    rospy.Subscriber('eyes_motion', std_msgs.msg.String, callback_eyes_motion)
