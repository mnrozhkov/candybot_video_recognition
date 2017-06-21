#!/usr/bin/env python3

from pathlib import Path
top = Path(__file__).resolve().parents[1].as_posix()
import sys
sys.path.append(top)

from servo.servo_pca9685 import Servo360


class Dispenser:

    '''
    candy dispenser
    '''

    def __init__(self, SERVO_CHANNEL):
        self.angle = 0
        self.SERVO_CHANNEL = SERVO_CHANNEL

        self.servo = Servo360(self.SERVO_CHANNEL)
        self.set_angle(self.angle)

    def set_angle(self, angle):
        '''
        rotate servo motor on the angle
        '''
        
        if isinstance(angle, (int, float)):
            self.servo.set_angle(angle)
            self.angle = angle

    def get_position(self):
        return self.angle
