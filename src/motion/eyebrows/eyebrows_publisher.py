#!/usr/bin/env python3
'''
publish message for eyebrows motions
'''

import rospy
from candybot_v2.msg import EyebrowsMotion


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

    def form_message(self, l_angle: float=0.0, r_angle: float=0.0, emotion: str='neutral') -> EyebrowsMotion:
        '''
        form EyebrowsMotion message
        '''

        msg = EyebrowsMotion(l_angle=l_angle, r_angle=r_angle, emotion=emotion)
        return msg

    def send_message(self, msg: EyebrowsMotion) -> None:
        self.publisher.publish(msg)

    def move_up(self):
        self.send_message(self.form_message(l_angle=88, r_angle=85))

    def move_down(self):
        self.send_message(self.form_message(l_angle=108, r_angle=65))

    def set_center(self):
        self.send_message(self.form_message(l_angle=98, r_angle=75))
