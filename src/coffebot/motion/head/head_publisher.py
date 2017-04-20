#!/usr/bin/env python3

import rospy
from coffebot.msg import HeadMotion

class Head:

    def __init__(self):
        self.publisher = rospy.Publisher('/motion_head_controller/head_motion_msg', HeadMotion, queue_size=1)

    def form_message(self, h_angle: float=0.0, v_angle: float=0.0, emotion: str=str()) -> HeadMotion:
        msg = HeadMotion()
        msg.h_angle = h_angle
        msg.v_angle = v_angle
        msg.emotion = emotion

        return msg

    def send_message(self, msg: HeadMotion) -> None:
        self.publisher.publish(msg)

    def move_up():
        self.send_message(self.form_message(v_angle=150.0))

    def move_down():
        self.send_message(self.form_message(v_angle=45.0))

    def turn_left():
        self.send_message(self.form_message(h_angle=45.0))

    def turn_left():
        self.send_message(self.form_message(h_angle=135.0))
