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
import math
import warnings


# Initialise the PCA9685 using the default address (0x40)
# SDA -> GPIO00/SDA0
# SCL- > GPIO01/SCL0
pwm = Adafruit_PCA9685.PCA9685()


# Uncomment to enable debug output.
import logging
logging.basicConfig(level=logging.DEBUG)

### Tests for hardware
#______________________

def test_hardware_example():
    # Turns servo back and forth 10 times
    # SDA -> GPIO00/SDA0
    # SCL- > GPIO01/SCL0
    # Ths is a simple hardware test, based on Adafruit_Python_PCA9685 example
    # Source: https://github.com/adafruit/Adafruit_Python_PCA9685/blob/master/examples/simpletest.py

    # Configure min and max servo pulse lengths
    servo_min = 150  # Min pulse length out of 4096
    servo_max = 600  # Max pulse length out of 4096

    # Helper function to make setting a servo pulse width simpler.
    def set_servo_pulse(channel, pulse):
        pulse_length = 1000000    # 1,000,000 us per second
        pulse_length //= 60       # 60 Hz
        print('{0}us per period'.format(pulse_length))
        pulse_length //= 4096     # 12 bits of resolution
        print('{0}us per bit'.format(pulse_length))
        pulse *= 1000
        pulse //= pulse_length
        pwm.set_pwm(channel, 0, pulse)

    # Set frequency to 60hz, good for servos.
    pwm.set_pwm_freq(60)

    print('Moving servo on channel 0, press Ctrl-C to quit...')
    turns = 0
    while turns <= 10:
        # Move servo on channel O between extremes.
        pwm.set_pwm(0, 0, servo_min)
        time.sleep(1)
        pwm.set_pwm(0, 0, servo_max)
        time.sleep(1)
        turns += 1


### Tests for hardware
#______________________

def test_set_angle():
    """
    Turns servo back and forth 10 times
    """

    # Set frequency to 60hz, good for servos.
    turns = 0
    while turns <= 10:
        # Move servo on channel O between extremes.
        set_angle(0, 60)
        time.sleep(1)
        set_angle(0, 120)
        time.sleep(1)
        turns += 1

def test_servo_class():
    """
    Turns servo back and forth 10 times
    """

    servo = Servo()
    # Set frequency to 60hz, good for servos.
    turns = 0
    while turns <= 10:
        # Move servo on channel O between extremes.
        servo.set_angle(0, 60)
        time.sleep(1)
        servo.set_angle(0, 120)
        time.sleep(1)
        turns += 1



if __name__ == "__main__":
    try:
        test_hardware_example()
    except KeyboardInterrupt:
        pass
