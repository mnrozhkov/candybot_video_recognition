#!/usr/bin/env python3

import rospy
from coffebot.motion.eyebrows.eyebrows_controller import Eyebrows
from coffebot.msg import EyebrowsMotion
from coffebot.topic_controller import Lock

import time


if __name__ == '__main__':
    rospy.init_node('motion_eyebrows_controller')

    eyebrows = Eyebrows()
    eyebrows_motion_lock = Lock()
    rospy.Subscriber('/motion_eyebrows_controller/eyebrows_motion', EyebrowsMotion, eyebrows_motion_lock.callback)

    while True:
        try:
            rospy.get_master().getPid()
        except:
            break

        eyebrows_msg = eyebrows_motion_lock.message
        if isinstance(yebrows_msg, EyebrowsMotion):
            eyebrows.set_left_servo_position(angle=eyebrows_msg.l_angle)
            eyebrows.set_right_servo_position(angle=eyebrows_msg.r_angle)
            eyebrows.set_emotion(emotion=eyebrows_msg.emotion)

        if eyebrows_motion_lock.message == eyebrows_msg:
            eyebrows_motion_lock.message = None

        time.sleep(0.5)
