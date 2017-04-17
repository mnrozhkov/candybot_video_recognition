#!/usr/bin/env python3
import os
import sys
from pathlib import Path

top = Path(__file__).resolve().parents[1]
sys.path.append(str(top))

from servo import servo


class Head(object):
    def __init__(self, _h_angle, _v_angle, _led_on, _color, _emotion, _h_SERVO_PIN, _v_SERVO_PIN, _PWM_DIVISOR, _PWM_RANGE,):
        # head position (servos) params
        self._h_angle = _h_angle
        self._v_angle = _v_angle

        # head led params
        self._led_on = _led_on
        self._color = _color

        # other settings
        self._emotion = _emotion

        # pin settings
        self._h_SERVO_PIN = _h_SERVO_PIN
        self._v_SERVO_PIN = _v_SERVO_PIN
        self._PWM_DIVISOR = _PWM_DIVISOR  # clock at 50kHz (20us tick)
        self._PWM_RANGE = _PWM_RANGE  # range at 1000 ticks (20ms)

        # move Head into default position
        self.set_horizontal_servo_position(90)
        self.set_vertical_servo_position(90)


    def setup_rpi_pins(self, _h_SERVO_PIN, _v_SERVO_PIN, _PWM_DIVISOR, _PWM_RANGE):
        servo.setup_rpi_pins([_h_SERVO_PIN, _v_SERVO_PIN], _PWM_DIVISOR, _PWM_RANGE)


    def set_horizontal_servo_position(self, angle):
        """
        Turn servo on specified angle in degrees
        Params:
            pos: angle to turn servo, in degrees
        """
        servo.set_servo_position(angle, self._h_SERVO_PIN)


    def set_vertical_servo_position(self, angle):
        """
        Turn servo on specified angle in degrees
        Params:
            pos: angle to turn servo, in degrees
        """
        servo.set_servo_position(angle, self._v_SERVO_PIN)


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

