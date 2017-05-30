#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from pathlib import Path

top = Path(__file__).resolve().parents[1]
sys.path.append(str(top))

from body_controller import Body, \
    ANGLE_OPEN_DISPENSER, \
    ANGLE_CLOSE_DISPENSER
import time

# Initialise the PCA9685 using the default channel (0x40)
pwm = Adafruit_PCA9685.PCA9685()

# Uncomment to enable debug output.
import logging
logging.basicConfig(level=logging.DEBUG)


angles = [30, 90, 180, 360]
body = Body(_d_SERVO_CHANNEL=3,
            _d_servo_angle=0,
            _led_on=True,
            _backlight_color='#ffffff',
            _emotion='happy',
            )

def test_dispenser_servo():
    """
    Turns servo back and forth 10 times
    """

    # Set frequency to 60hz, good for servos.
    for angle in angles:
        # Move servo on channel O between extremes.
        body.set_dispenser_servo_position(angle)
        time.sleep(1)
        body.set_dispenser_servo_position(-angle)
        time.sleep(1)


if __name__ == "__main__":
    try:
        test_dispenser_servo()
    except KeyboardInterrupt:
        pass
