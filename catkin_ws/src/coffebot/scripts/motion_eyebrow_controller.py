#!/usr/bin/env python3

import rospy
import std_msgs

import json
from coffebot.motion.head_control import Eyebrows

if __name__ == '__main__':

    rospy.init_node('motion_head_controller')
    eyebrows = Eyebrows()

    def callback_eyebrows_motion(data: std_msgs.msg.String, queue_size=1):
        eyebrows_motion = json.loads(data.data)
        eyebrows.move_up(eyebrows_motion['move_up'])
        eyebrows.move_down(eyebrows_motion['move_down'])

        if eyebrows_motion['turn_on_backlight'] is True:
            eyebrows.turn_on_backlight()

        eyebrows.set_backlight_color(eyebrows_motion['set_backlight_color'])

    rospy.Subscriber('eyebrows_motion', std_msgs.msg.String, callback_eyebrows_motion)
