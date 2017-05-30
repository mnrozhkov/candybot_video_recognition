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
head = Head(_h_angle=90,
            _v_angle=90,
            _emotion='happy',
            _h_SERVO_CHANNEL=3,
            _v_SERVO_CHANNEL=2)


def test_horizontal_servo():
    """
    Turns servo back and forth 10 times
    """

    # Set frequency to 60hz, good for servos.
    turns = 0
    for angle in angles:
        # Move servo on channel O between extremes.
        head.set_horizontal_servo_position(angle)
        time.sleep(1)
        head.set_horizontal_servo_position(-angle)
        time.sleep(1)


def test_verticical_servo():
    """
    Turns servo back and forth 10 times
    """

    # Set frequency to 60hz, good for servos.
    turns = 0
    for angle in angles:
        # Move servo on channel O between extremes.
        head.set_verticical_servo_position(angle)
        time.sleep(1)
        head.set_verticical_servo_position(-angle)
        time.sleep(1)


if __name__ == "__main__":
    try:
        test_horizontal_servo()
        test_verticical_servo()
    except KeyboardInterrupt:
        pass
