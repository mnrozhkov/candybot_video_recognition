#!/usr/bin/env python3

import rospy
from coffebot.motion.body.body_controller import Body
from coffebot.msg import BodyMotion, BodyState
from coffebot.topic_controller import Lock

import time


if __name__ == '__main__':
    rospy.init_node('motion_body_controller')

    body = Body(_d_SERVO_ADDRESS=3, _emotion='neutral')
    body_motion_lock = Lock()
    rospy.Subscriber('/motion_body_controller/body_motion', BodyMotion, body_motion_lock.callback)
    body_state_publisher = rospy.Publisher('/motion_body_controller/body_state', BodyState, queue_size=1)
    while True:
        try:
            rospy.get_master().getPid()
        except:
            break

        body_msg = body_motion_lock.message
        if isinstance(body_msg, BodyMotion):
            body.set_dispenser_servo_position(angle=body_msg.angle)
            body.set_emotion(emotion=body_msg.emotion)

            body_state_msg = BodyState()
            body_state_msg.angle = body.get_dispenser_servo_position()
            body_state_msg.emotion = body.get_emotion()
            body_state_publisher.publish(body_state_msg)

        if body_motion_lock.message == body_msg:
            body_motion_lock.message = None

        time.sleep(0.5)
