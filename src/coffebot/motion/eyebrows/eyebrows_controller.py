#!/usr/bin/env python3
import os
import sys
from pathlib import Path
import warnings

top = Path(__file__).resolve().parents[1]
sys.path.append(str(top))

from servo.servo_pca9685 import Servo


class Eyebrows(object):
    def __init__(self, _l_angle, _r_angle, _l_SERVO_ADDRESS, _r_SERVO_ADDRESS, _led_on, _led_color, _emotion):
        # Eyebrows position (servos) params
        self._l_angle = _l_angle
        self._r_angle = _r_angle
        self._l_SERVO_ADDRESS = _l_SERVO_ADDRESS
        self._r_SERVO_ADDRESS = _r_SERVO_ADDRESS
        self.l_servo = Servo(address=_l_SERVO_ADDRESS)
        self.r_servo = Servo(address=_r_SERVO_ADDRESS)

        # move Eyebrows into default position
        self.set_left_servo_position(_l_angle)
        self.set_right_servo_position(_r_angle)

        # Eyebrows led params
        self._led_on = _led_on
        self._led_color = _led_color

        # other settings
        self._emotion = _emotion

    def set_left_servo_position(self, angle):
        """
        Turn servo on specified angle in degrees
        Params:
            angle: angle to turn servo, in degrees
        """
        if isinstance(angle, (int, float)):
            self.l_servo.set_angle(self._l_SERVO_ADDRESS, angle)
            self._l_angle = angle
        else:
            warnings.warn("'angle' param is not a number. Servo has not moved")

    def set_right_servo_position(self, angle):
        """
        Turn servo on specified angle in degrees
        Params:
            angles: angle to turn servo, in degrees
        """
        if isinstance(angle, (int, float)):
            self.r_servo.set_angle(self._r_SERVO_ADDRESS, angle)
            self._r_angle = angle
        else:
            warnings.warn("'angle' param is not a number. Servo has not moved")

    def get_eyebrows_position(self):
        return (self._l_angle, self._r_angle)

    # def move_up(self, angle=30):
    #     self.set_left_servo_position(angle)
    #     self.set_left_servo_position(-angle)
    #
    # def move_down(self, angle=-30):
    #     self.set_left_servo_position(angle)
    #     self.set_left_servo_position(-angle)

    def set_emotion(self, emotion=None):
        if emotion is None:
            self._emotion = 'neutral'
        else:
            self._emotion = emotion

    def get_emotion(self):
        return self._emotion



    # TODO: Add implementation for methods below
    def set_led_mode(led_on=False, color=(255, 255, 255), mode='light', frequency=None):
        print('body: led_on={0},color={1}, mode={2}, frequency={3}'.format(led_on, color, mode, frequency))

    def turn_backlight_on(self):
        print('eyebrows backlight on')

    def turn_backlight_off(self):
        print('eyebrows backlight off')

    def turn_backlight_dim(self):
        print('eyebrows backlight dim')

    def set_backlight_color(self, color):
        print('backlight:', color)
        self.backlight_color = color

    def blink_backlight(self, times: int = 1):
        print('eyebrows backlight blink:', times)
