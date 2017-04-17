#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2017 FunRobots Lab

import wiringpi
import math
import warnings


# #use BCM pin numbers
# wiringpi.wiringPiSetupGpio()
#
# # setup WiringPi PWM
# SERVO_PIN = 18
# PWM_DIVISOR = 384 # clock at 50kHz (20us tick)
# PWM_RANGE = 1000  # range at 1000 ticks (20ms)


def servo.setup_rpi_pins(servo_pins, PWM_DIVISOR, PWM_RANGE):
    """
    Setup pin as an output 
    :param dummy_head: 
    :return: 
    """
    for pin in servo_pins:
        try:
            wiringpi.pinMode(pin, 2)
        except:
            warnings.warn("Unable to setup rpi pin mode. Pin number: {}".format(pin))

    wiringpi.pwmSetMode(0)
    wiringpi.pwmSetClock(PWM_DIVISOR)
    wiringpi.pwmSetRange(PWM_RANGE)
    wiringpi.pwmWrite(SERVO_PIN, 0) #theretically 50 (1ms) to 100 (2ms) on my servo 40-200 works ok


def set_servo_position(pos, SERVO_PIN):
    """ 
    Turn servo on specified angle in degrees
    Params:
        pos: angle to turn servo, in degrees
    """

    move = int(40 + math.floor(pos * (200 - 40) / 180))
    if move:
        try:
            wiringpi.pwmWrite(SERVO_PIN, move)
            # time.sleep(0.5)
        except:
            # clean up
            wiringpi.pwmWrite(SERVO_PIN, 0)
            warnings.warn("Servo was not moved. Move in None. Set servo pin to 0")