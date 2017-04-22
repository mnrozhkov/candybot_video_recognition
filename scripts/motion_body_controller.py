#!/usr/bin/env python3

import rospy
from coffebot.motion.body.body_controller import Body
from coffebot.msg import BodyMotion
from coffebot.topic_controller import Lock

import time


if __name__ == '__main__':
    rospy.init_node('motion_body_controller')

    body = Body()
    body_motion_lock = Lock()
    rospy.Subscriber('/motion_body_controller/body_motion', BodyMotion, body_motion_lock.callback)

    while True:
        try:
            rospy.get_master().getPid()
        except:
            break

        body_msg = body_motion_lock.message
        if isinstance(body_msg, BodyMotion):
            body.set_dispenser_servo_position(angle=body_msg.angle)
            body.set_emotion(emotion=body_msg.emotion)

        if body_motion_lock.message == body_msg:
            body_motion_lock.message = None

        time.sleep(0.5)
