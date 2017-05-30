#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2017 FunRobots Lab

# Project: Candybot: candybot_v2
# Summary: Test for motion_eyes_controller
# version: v1


import os
import sys
from pathlib import Path
import random
import pytest

top = Path(__file__).resolve().parents[1]
sys.path.append(str(top))

from eyebrows_controller import Eyebrows

# set general params
L_ANGLE_DEFAULT = 90,
R_ANGLE_DEFAULT = 90,
L_SERVO_CHANNEL = 1,
R_SERVO_CHANNEL = 0,
LED_ON = True,
LED_COLOR = '#ffffff',
EMOTION = 'happy'


### Define fixtures
#______________________

@pytest.fixture(scope="function")
def dummy_eyebrows():
    eyebrows = Eyebrows(
        _l_angle = L_ANGLE_DEFAULT,
        _r_angle = R_ANGLE_DEFAULT,
        _l_SERVO_CHANNEL = L_SERVO_CHANNEL,
        _r_SERVO_CHANNEL = R_SERVO_CHANNEL,
        _led_on = LED_ON,
        _led_color = LED_COLOR,
        _emotion = EMOTION
    )
    yield eyebrows



### Tests for  softwareEMOTION
#______________________

def test_eyebrows_init(dummy_eyebrows):
    assert dummy_eyebrows._l_angle == L_ANGLE_DEFAULT
    assert dummy_eyebrows._r_angle == R_ANGLE_DEFAULT
    assert dummy_eyebrows._l_SERVO_CHANNEL == L_SERVO_CHANNEL
    assert dummy_eyebrows._r_SERVO_CHANNEL == R_SERVO_CHANNEL
    assert dummy_eyebrows._led_on == LED_ON
    assert dummy_eyebrows._led_color == LED_COLOR
    assert dummy_eyebrows._emotion == EMOTION


# Tests for servo 1: horizontal
@pytest.mark.parametrize(("angle", "pos_expected"),
                         [(0, 90),
                          (5, 95),
                          (-60, 35),
                          (1, 36),
                          (None, 36),
                          (143.5, 179.5),
                          (-89.5, 90),])
def test_set_left_servo_position_normal(angle, pos_expected):
    dummy_eyebrows.set_left_servo_position(angle)
    assert dummy_eyebrows.set_left_servo_position == pos_expected

@pytest.mark.parametrize(("angle"),
                         [("10"),
                          ([16, 30]),
                          ({}),
                          (''),])
def test_set_left_servo_position_raise_type_error(angle):
    with pytest.raises(TypeError, message="Expecting TypeError exception"):
        dummy_eyebrows.set_left_servo_position(angle)


# Tests for servo 2: vertical
@pytest.mark.parametrize(("angle", "pos_expected"),
                         [(0, 90),
                          (5, 95),
                          (-60, 35),
                          (1, 36),
                          (None, 36),
                          (143.5, 179.5),
                          (-89.5, 90),])
def test_set_right_servo_position_normal(angle, pos_expected):
    dummy_eyebrows.set_right_servo_position(angle)
    assert dummy_eyebrows.set_right_servo_position == pos_expected

@pytest.mark.parametrize(("angle"),
                         [("10"),
                          ([16, 30]),
                          ({}),
                          (''),])
def test_set_right_servo_position_raise_type_error(angle):
    with pytest.raises(TypeError, message="Expecting TypeError exception"):
        dummy_eyebrows.set_right_servo_position(angle)


# Tests position return type
def test_get_eyebrows_position_type(dummy_eyebrows):
    """
    eyebrows position should be a tuple of two numbers
    :param dummy_eyebrows:
    :return:
    """
    eyebrows_position = dummy_eyebrows.get_eyebrows_position()
    assert isinstance(eyebrows_position, tuple)
    assert isinstance(eyebrows_position[0], (int, float))
    assert isinstance(eyebrows_position[1], (int, float))


# Tests emtions
@pytest.mark.parametrize(("emotion, expected"),
                         [("happy", "happy"),
                          ("neutral", "neutral"),])
def test_set_get_emotion(emotion, expected, dummy_eyebrows):
    dummy_eyebrows.set_emotion = 'happy'
    assert dummy_eyebrows.get_emotion == expected



# TODO: Add tests for LEDs and backlights methods
