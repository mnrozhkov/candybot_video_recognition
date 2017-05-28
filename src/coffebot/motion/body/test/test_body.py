#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2017 FunRobots Lab

# Project: Candybot: Coffebot
# Summary: Test for motion_eyes_controller
# version: v1


import os
import sys
from pathlib import Path
import random
import pytest
import warnings

top = Path(__file__).resolve().parents[1]
sys.path.append(str(top))


from body_controller import Body, \
    ANGLE_OPEN_DISPENSER, \
    ANGLE_CLOSE_DISPENSER

### Define fixtures
#______________________

@pytest.fixture(scope="function")
def dummy_body():
    body = Body(_d_SERVO_CHANNEL = 3,
                _d_servo_angle = 0,
                _led_on = True,
                _backlight_color = '#ffffff',
                _emotion = 'happy',
                )
    yield body



### Tests for  software
#______________________

def test_body_init(dummy_body):
    assert dummy_body._d_SERVO_CHANNEL== 3
    assert dummy_body._d_servo_angle == 0
    assert dummy_body._led_on == True
    assert dummy_body._backlight_color == '#ffffff'
    assert dummy_body._emotion == 'happy'


# Tests for servo 1: candy dispenser
@pytest.mark.parametrize(("angle", "pos_expected"),
                         [(0, 90),
                          (5, 95),
                          (-60, 35),
                          (1, 36),
                          (None, 36),
                          (143.5, 179.5),
                          (-89.5, 90),])
def test_set_dispenser_servo_position_normal(angle, pos_expected):
    dummy_body.set_dispenser_servo_position(angle)
    assert dummy_body.set_dispenser_servo_position == pos_expected

    @pytest.mark.parametrize(("angle"),
                             [("10"),
                              ([16, 30]),
                              ({}),
                              (''), ])
    def test_set_dispenser_servo_position_raise_type_error(angle):
        with pytest.raises(TypeError, message="Expecting TypeError exception"):
            dummy_body.set_dispenser_servo_position(angle)
            
# Tests position return type
def test_get_body_position_type(dummy_body):
    """
    body position should be a tuple of two numbers 
    :param dummy_body: 
    :return: 
    """
    body_position = dummy_body.get_body_position()
    assert isinstance(body_position, tuple)
    assert isinstance(body_position[0], (int, float))
    assert isinstance(body_position[0], (int, float))


def test_open_dispenser(ANGLE_OPEN_DISPENSER):
    dummy_body.open_dispenser()
    assert dummy_body.get_body_position() == ANGLE_OPEN_DISPENSER

def test_close_dispenser(ANGLE_CLOSE_DISPENSER):
    dummy_body.close_dispenser()
    assert dummy_body.get_body_position() == ANGLE_CLOSE_DISPENSER

def test_give_candy():
    assert dummy_body.give_candy()



# Tests emotions
@pytest.mark.parametrize(("emotion, expected"),
                         [("happy", "happy"),
                          ("neutral", "neutral"),])
def test_set_get_emotion(emotion, expected, dummy_body):
    dummy_body.set_emotion = 'happy'
    assert dummy_body.get_emotion == expected




# TODO: Add tests for LEDs and backlights methods
