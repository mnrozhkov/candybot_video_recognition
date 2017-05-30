#!/usr/bin/env python3
import os
import sys
from pathlib import Path
import warnings

top = Path(__file__).resolve().parents[1]
sys.path.append(str(top))

from servo.servo_pca9685 import Servo


class Head(object):
    def __init__(self, _h_angle, _v_angle, _emotion, _h_SERVO_CHANNEL, _v_SERVO_CHANNEL):
        # head position (servos) params
        self._h_angle = _h_angle
        self._v_angle = _v_angle

        # head led params
        # self._led_on = _led_on
        # self._color = _color

        # other settings
        self._emotion = _emotion

        # pin settings
        self._h_SERVO_CHANNEL = _h_SERVO_CHANNEL
        self._v_SERVO_CHANNEL = _v_SERVO_CHANNEL

        self.h_servo = Servo(channel =_h_SERVO_CHANNEL)
        self.v_servo = Servo(channel =_v_SERVO_CHANNEL)

        # move Head into default position
        self.set_horizontal_servo_position(_h_angle)
        self.set_vertical_servo_position(_v_angle)


    def set_horizontal_servo_position(self, angle):
        """
        Turn servo on specified angle in degrees
        Params:
            angle: angle to turn servo, in degrees
        """
        if isinstance(angle, (int, float)):
            self.h_servo.set_angle(self._h_SERVO_CHANNEL, angle)
            self._h_angle = angle
        else:
            warnings.warn("'angle' param is not a number. Servo has not moved")


    def set_vertical_servo_position(self, angle):
        """
        Turn servo on specified angle in degrees
        Params:
            angles: angle to turn servo, in degrees
        """
        if isinstance(angle, (int, float)):
            self.v_servo.set_angle(self._v_SERVO_CHANNEL, angle)
            self._v_angle = angle
        else:
            warnings.warn("'angle' param is not a number. Servo has not moved")


    def get_head_position(self):
        return (self._h_angle, self._v_angle)


    def set_emotion(self, emotion=None):
        if emotion is None:
            self._emotion = 'neutral'
        else:
            self._emotion = emotion

    def get_emotion(self):
        return self._emotion


    #TODO: Add implementation for methods below
    def set_led_mode(led_on=False, color=(255, 255, 255), mode='light', frequency=None):
        print('body: led_on={0},color={1}, mode={2}, frequency={3}'.format(led_on, color, mode, frequency))


    def nod_to_agree(self):
        print('head nod to agree')


    def nod_to_disagree(self):
        print('head nod to disagree')


    def move_to_coords(self, coords):
        print('head move to:', coords)
