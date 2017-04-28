#!/usr/bin/env python3
'''
publish message for head motions
'''

import rospy
from coffebot.msg import HeadMotion


class HeadPublisher:
    '''
    relesase head motion message creation
    '''

    def __init__(self):
        '''
        constructer
        create ROS publisher
        '''

        self.publisher = rospy.Publisher('/motion_head_controller/head_motion', HeadMotion, queue_size=1)

    def form_message(self, h_angle: float=0.0, v_angle: float=0.0, emotion: str='neutral') -> HeadMotion:
        '''
        form HeadMotion message
        '''

        msg = HeadMotion()
        msg.h_angle = h_angle
        msg.v_angle = v_angle
        msg.emotion = emotion

        return msg

    def send_message(self, msg: HeadMotion) -> None:
        self.publisher.publish(msg)

    def move_up(self):
        self.send_message(self.form_message(v_angle=150.0))

    def move_down(self):
        self.send_message(self.form_message(v_angle=45.0))

    def turn_left(self):
        self.send_message(self.form_message(h_angle=45.0))

    def turn_right(self):
        self.send_message(self.form_message(h_angle=135.0))

    def move_up_left(self):
        self.send_message(self.form_message(h_angle=45.0, v_angle=150.0))

    def move_up_rigth(self):
        self.send_message(self.form_message(h_angle=135.0, v_angle=150.0))

    def move_down_left(self):
        self.send_message(self.form_message(h_angle=45.0, v_angle=45.0))

    def move_down_right(self):
        self.send_message(self.form_message(h_angle=135.0, v_angle=45.0))
