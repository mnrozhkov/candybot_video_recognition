#!/usr/bin/env python3
'''
publish message for eyebrows motions
'''

import rospy
from coffebot.msg import EyesMotion


class EyesPublisher:
    '''
    relesase eyebrows motion message creation
    '''

    def __init__(self):
        '''
        constructer
        create ROS publisher
        '''

        self.publisher = rospy.Publisher('/motion_eyes_controller/eyes_motion', EyesMotion, queue_size=1)

    def form_message(self, angle: float=0.0, distance_from_center_percent: float=0.0, emotion: str=str()) -> EyebrowsMotion:
        '''
        form EyesMotion message
        '''

        msg = EyesMotion()
        msg.angle = angle
        msg.distance_from_center_percent = distance_from_center_percent
        msg.emotion = emotion

        return msg

    def send_message(self, msg: EyesMotion) -> None:
        self.publisher.publish(msg)

    def move_up():
        self.send_message(self.form_message(angle=90.0, distance_from_center_percent=90.0))

    def move_down():
        self.send_message(self.form_message(angle=270.0, distance_from_center_percent=90.0))

    def move_left():
        self.send_message(self.form_message(angle=180.0, distance_from_center_percent=90.0))

    def move_right():
        self.send_message(self.form_message(angle=0.0, distance_from_center_percent=90.0))
