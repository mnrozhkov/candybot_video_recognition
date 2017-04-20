#!/usr/bin/env python3
'''
publish message for eyebrows motions
'''

import rospy
from coffebot.msg import EyebrowsMotion


class EyebrowsPublisher:
    '''
    relesase eyebrows motion message creation
    '''

    def __init__(self):
        '''
        constructer
        create ROS publisher
        '''

        self.publisher = rospy.Publisher('/motion_eyebrows_controller/eyebrows_motion', EyebrowsMotion, queue_size=1)

    def form_message(self, l_angle: float=0.0, r_angle: float=0.0, emotion: str=str()) -> EyebrowsMotion:
        '''
        form EyebrowsMotion message
        '''

        msg = EyebrowsMotion()
        msg.l_angle = l_angle
        msg.r_angle = r_angle
        msg.emotion = emotion

        return msg

    def send_message(self, msg: EyebrowsMotion) -> None:
        self.publisher.publish(msg)

    def move_up():
        self.send_message(self.form_message(l_angle=30.0, r_angle=30.0))

    def move_down():
        self.send_message(self.form_message(l_angle=-30.0, r_angle=-30.0))
