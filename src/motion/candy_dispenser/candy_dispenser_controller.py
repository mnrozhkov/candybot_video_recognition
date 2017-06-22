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
        self.servo360 = Servo360(SERVO_CHANNEL)

    def run(self):
        self.servo360.run()

    def stop(self):
        self.servo360.stop()
