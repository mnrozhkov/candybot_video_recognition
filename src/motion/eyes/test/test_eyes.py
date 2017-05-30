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

from eyes_controller import Eyes
from eyes_lib import get_device, draw_eye, set_display_frame_rate, create_canvas, convert_params_to_coord
#

### Define fixtures
#______________________

@pytest.fixture
def dummy_eyes_params():
    dummy_eyes_params = {
        '_w': 128,
        '_h': 128,
        '_color': '#ffffff',
        '_eye_radius': 64,
        '_eye_color': '#ffffff',
        '_x_center': 64,
        '_y_center': 64,
        '_x_pos': 64,
        '_y_pos': 64,
        '_pupil_radius': 25,
        '_pupil_orbit_radius': 39,
        '_pupil_color': '#1c86ee',
        '_x_speed': 5,
        '_y_speed': 5,
        '_emotion': 'happy'
    }
    return dummy_eyes_params

@pytest.fixture
def dummy_eyes_class(dummy_eyes_params):
    eyes = Eyes(width=dummy_eyes_params['_w'],
                height=dummy_eyes_params['_h'],
                background_color=dummy_eyes_params['#ffffff'],
                eye_radius=dummy_eyes_params['_eye_radius'],
                eye_color=dummy_eyes_params['#ffffff'],
                pupil_radius=dummy_eyes_params['_pupil_radius'],
                pupil_color=dummy_eyes_params['#1c86ee']
                )
    return eyes



### Tests for  software
#______________________

class TestEyesLibFunctions:                      # unit-tests for a class methods
    @pytest.mark.parametrize(('angle', 'distance_from_center_percent', 'outer_radius', "x_expected", "y_expected"), [
        (None, None, dummy_eyes_params['_pupil_orbit_radius'], 0, 0),
    ])
    def test_convert_params_to_coord(self, eyes, angle, distance_from_center_percent, outer_radius, x_expected, y_expected):
        _x_pos, _y_pos = convert_params_to_coord(angle, distance_from_center_percent, outer_radius)
        assert (_x_pos == x_expected) & (_y_pos == y_expected)



class TestEyesMethods:                      # unit-tests for a class methods
    @pytest.mark.parametrize(("x", "y", "x_expected", "y_expected"), [
        (None, None, dummy_eyes_params['_w'], dummy_eyes_params['_h']),
    ])
    def test_set_eyes_position(self, eyes, x, y, x_expected, y_expected):
        _x_pos, _y_pos = eyes.set_eyes_position(x, y)
        assert (_x_pos == x_expected) & (_y_pos == y_expected)

    def test_set_path_to_move_eyes(self):
        pass

    def test_get_set_emotion(self):
        pass
