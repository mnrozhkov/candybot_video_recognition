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

from head_controller import Head

#

### Define fixtures
### Define fixtures
#______________________

@pytest.fixture(scope="function")
def dummy_head():
    head = Head(_h_angle=90,
                _v_angle=90,
                _emotion='happy',
                _h_SERVO_CHANNEL=3,
                _v_SERVO_CHANNEL=2)
    yield head



### Tests for  software
#______________________

def test_head_init(dummy_head):
    assert dummy_head._h_angle == 90
    assert dummy_head._v_angle == 90
    assert dummy_head._emotion == 'neutral'
    assert dummy_head._h_SERVO_CHANNEL==3
    assert dummy_head._v_SERVO_CHANNEL==2


# Tests for servo 1: horizontal
@pytest.mark.parametrize(("angle", "pos_expected"),
                         [(0, 90),
                          (5, 95),
                          (-60, 35),
                          (1, 36),
                          (None, 36),
                          (143.5, 179.5),
                          (-89.5, 90),])
def test_set_horizontal_servo_position_normal(angle, pos_expected):
    dummy_head.set_horizontal_servo_position(angle)
    assert dummy_head.set_horizontal_servo_position == pos_expected

@pytest.mark.parametrize(("angle"),
                         [("10"),
                          ([16, 30]),
                          ({}),
                          (''),])
def test_set_horizontal_servo_position_raise_type_error(angle):
    with pytest.raises(TypeError, message="Expecting TypeError exception"):
        dummy_head.set_horizontal_servo_position(angle)


# Tests for servo 2: vertical
@pytest.mark.parametrize(("angle", "pos_expected"),
                         [(0, 90),
                          (5, 95),
                          (-60, 35),
                          (1, 36),
                          (None, 36),
                          (143.5, 179.5),
                          (-89.5, 90),])
def test_set_vertical_servo_position_normal(angle, pos_expected):
    dummy_head.set_vertical_servo_position(angle)
    assert dummy_head.set_vertical_servo_position == pos_expected

@pytest.mark.parametrize(("angle"),
                         [("10"),
                          ([16, 30]),
                          ({}),
                          (''),])
def test_set_vertical_servo_position_raise_type_error(angle):
    with pytest.raises(TypeError, message="Expecting TypeError exception"):
        dummy_head.set_vertical_servo_position(angle)


# Tests position return type
def test_get_head_position_type(dummy_head):
    """
    Head position should be a tuple of two numbers
    :param dummy_head:
    :return:
    """
    head_position = dummy_head.get_head_position()
    assert isinstance(head_position, tuple)
    assert isinstance(head_position[0], (int, float))
    assert isinstance(head_position[1], (int, float))


# Tests emtions
@pytest.mark.parametrize(("emotion, expected"),
                         [("happy", "happy"),
                          ("neutral", "neutral"),])
def test_set_get_emotion(emotion, expected, dummy_head):
    dummy_head.set_emotion = 'happy'
    assert dummy_head.get_emotion == expected



#TODO: Add tests behavior patterns below
# Tests behavior patterns
def test_nod_to_agree(dummy_head):
    print('head nod to agree')
    pass


def test_nod_to_disagree(dummy_head):
    print('head nod to disagree')
    pass


def test_move_to_coords(dummy_head):
    print('head move to:')
    pass
