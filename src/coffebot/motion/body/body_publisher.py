#!/usr/bin/env python3
'''
publish message for body motions
'''

import rospy
from coffebot.msg import BodyMotion


class BodyPublisher:
    '''
    relesase body motion message creation
    '''

    def __init__(self):
        '''
        constructer
        create ROS publisher
        '''

        self.publisher = rospy.Publisher('/motion_body_controller/body_motion', BodyMotion, queue_size=1)

    def form_message(self, angle: float=0.0, emotion: str=str()) -> BodyMotion:
        '''
        form BodyMotion message
        '''

        msg = BodyMotion()
        msg.angle = h_angle
        msg.emotion = emotion

        return msg

    def send_message(self, msg: BodyMotion) -> None:
        self.publisher.publish(msg)

    def turn_left():
        self.send_message(self.form_message(angle=45.0))

    def turn_right():
        self.send_message(self.form_message(h_angle=135.0))
