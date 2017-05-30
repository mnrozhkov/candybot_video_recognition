#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from pathlib import Path

top = Path(__file__).resolve().parents[1]
sys.path.append(str(top))

from servo_pca9685 import set_angle, Servo
import Adafruit_PCA9685
import time

# Initialise the PCA9685 using the default channel (0x40)
pwm = Adafruit_PCA9685.PCA9685()

# Uncomment to enable debug output.
import logging
logging.basicConfig(level=logging.DEBUG)

angles = [5, 10, 15, 20, 30]
eyebrows = Eyebrows(
    _l_angle=90,
    _r_angle=90,
    _l_SERVO_CHANNEL=1,
    _r_SERVO_CHANNEL=0,
    _led_on=True,
    _led_color='#ffffff',
    _emotion='happy'
)


def test_left_servo():
    """
    Turns servo back and forth 10 times
    """

    # Set frequency to 60hz, good for servos.
    for angle in angles:
        # Move servo on channel O between extremes.
        eyebrows.set_left_servo_position(angle)
        time.sleep(1)
        eyebrows.set_left_servo_position(-angle)
        time.sleep(1)


def test_right_servo():
    """
    Turns servo back and forth 10 times
    """

    # Set frequency to 60hz, good for servos.
    for angle in angles:
        # Move servo on channel O between extremes.
        eyebrows.set_right_servo_position(angle)
        time.sleep(1)
        eyebrows.set_right_servo_position(-angle)
        time.sleep(1)


if __name__ == "__main__":
    try:
        test_left_servo()
        test_right_servo()
    except KeyboardInterrupt:
        pass
