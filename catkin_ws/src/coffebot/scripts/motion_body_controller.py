#!/usr/bin/env python3

import rospy
import std_msgs

import json
from coffebot.motion.body_control import Body

if __name__ == '__main__':

    rospy.init_node('motion_head_controller')
    body = body()

    def callback_body_motion(data: std_msgs.msg.String, queue_size=1):

        if body_motion['turn_on_backlight'] is True:
            body.turn_on_backlight()

        if body_motion['blink_backlight'] is True:
            body.blink_backlight()

        body.set_backlight_color(body_motion['set_backlight_color'])

    rospy.Subscriber('body_motion', std_msgs.msg.String, callback_body_motion)
