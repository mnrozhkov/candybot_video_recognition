#!/usr/bin/env python3

import rospy
import std_msgs

import json
from coffebot.motion.head_control import Head

if __name__ == '__main__':

    rospy.init_node('motion_head_controller')
    head = Head()

    def callback_head_motion(data: std_msgs.msg.String, queue_size=1):
        head_motion = json.loads(data.data)
        head.turn_left(head_motion['turn_left'])
        head.turn_right(head_motion['turn_right'])
        head.turn_up(head_motion['turn_up'])
        head.turn_down(head_motion['turn_down'])
        head.turn_left(head_motion['turn_left'])
        if head_motion['nod_to_agree'] is True:
            head.nod_to_agree()
        if head_motion['nod_to_disagree'] is True:
            head.nod_to_diagree()
        head.move_to_coords(head_motion['move_to_coords'])

    rospy.Subscriber('head_motion', std_msgs.msg.String, callback_head_motion)
