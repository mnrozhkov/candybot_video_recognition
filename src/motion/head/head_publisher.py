#!/usr/bin/env python3
'''
publish message for head motions
'''

import rospy
from candybot_v2.msg import HeadMotion, FaceCoordinates
import time
import math


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

    def move_to_face(self):

        self.face_coords_recieved = False
        self.x, self.y = None, None

        def callback_face_coords(data: FaceCoordinates):
            self.x = data.x
            self.y = data.y
            self.face_coords_recieved = True

        face_coords_sub = rospy.Subscriber('/vision_face_tracking/face_coord', FaceCoordinates, callback_face_coords)

        start = time.time()
        while time.time() - start < 1 and self.face_coords_recieved is False:
            time.sleep(0.1)

        face_coords_sub.unregister()

        if self.x is not None and self.y is not None:
            self.send_message(self.form_message(h_angle= 180 *math.atan(self.x) / math.pi, v_angle= 180 * math.atan(self.y) / math.pi))
