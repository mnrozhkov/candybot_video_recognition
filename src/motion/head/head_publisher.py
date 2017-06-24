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

        self.mid_angle = 90

        self.min_h_angle = 45
        self.max_h_angle = 135
        self.min_v_angle = 70
        self.max_v_angle = 110

        self.image_width = 640
        self.image_heigth = 480

        #self.step = 10

    def _get_h_angle_by_x_coord(self, x: int) -> int:
        return self.min_h_angle + (self.max_h_angle - self.min_h_angle) * x // self.image_width

    def _get_v_angle_by_y_coord(self, y: int) -> float:
        return self.min_v_angle + (self.max_v_angle - self.max_v_angle) * y // self.image_heigth

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

    def move_down(self):
        self.send_message(self.form_message(v_angle=40.0))

    def move_up(self):
        self.send_message(self.form_message(v_angle=0.0))

    def turn_right(self):
        self.send_message(self.form_message(h_angle=0.0))

    def turn_left(self):
        self.send_message(self.form_message(h_angle=90.0))

    def move_down_right(self):
        self.send_message(self.form_message(h_angle=40.0, v_angle=0.0))

    def move_down_left(self):
        self.send_message(self.form_message(h_angle=40.0, v_angle=90.0))

    def move_up_right(self):
        self.send_message(self.form_message(h_angle=0.0, v_angle=0.0))

    def move_up_left(self):
        self.send_message(self.form_message(h_angle=0.0, v_angle=90.0))

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
            self.send_message(self.form_message(h_angle=self._get_h_angle_by_x_coord(self.x), v_angle=self._get_v_angle_by_y_coord(self.y)))

    def set_h_angle(self, h_angle=0.0):
        if rospy.has_param('/head/v_angle'):
            self.send_message(self.form_message(h_angle=h_angle, v_angle=rospy.get_param('/head/v_angle')))

    def set_v_angle(self, v_angle=0.0):
        if rospy.has_param('/head/h_angle'):
            self.send_message(self.form_message(h_angle=rospy.get_param('/head/h_angle'), v_angle=v_angle))

    def move_h_angle(self, h_angle=0.0):
        if rospy.has_param('/head/h_angle') and rospy.has_param('/head/v_angle'):
            future_h_angle = rospy.get_param('/head/h_angle') + h_angle
            if future_h_angle >= self.min_h_angle and future_h_angle <= self.max_h_angle:
                self.send_message(self.form_message(h_angle=future_h_angle, v_angle=rospy.get_param('/head/v_angle')))

    def move_v_angle(self, v_angle=0.0):
        if rospy.has_param('/head/h_angle') and rospy.has_param('/head/v_angle'):
            future_v_angle = rospy.get_param('/head/v_angle') + v_angle
            if future_v_angle >= self.min_v_angle and future_v_angle <= self.max_v_angle:
                self.send_message(self.form_message(h_angle=rospy.get_param('/head/h_angle'), v_angle=future_v_angle))
