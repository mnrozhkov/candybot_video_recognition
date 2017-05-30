#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2017 FunRobots Lab

# Project: Candybot: candybot_v2
# Summary: Test for motion_eyes_controller
# version: v1
# Test marks and interpretations
#     1) Серьезность (Severity) Наиболее распространена пятиуровневая система градации серьезности дефекта:
#         • S1 Блокирующий (Blocker)
#         • S2 Критический (Critical)
#         • S3 Значительный (Major)
#         • S4 Незначительный (Minor)
#         • S5 Тривиальный (Trivial)
#     2) Приоритет (Priority) Приоритет дефекта:
#         • P1 Высокий (High)
#         • P2 Средний (Medium)
#         • P3 Низкий (Low)


import pytest


@pytest.fixture
def dummy_eyes_class_params():
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





class TestEyesROSIntegration:               # integration tests for a class
    def test_one(self):
        pass

    def test_two(self):
        pass


class TestMotionEyesControllerScript:       # integration methods for a script (node)
    def test_one(self):
        pass
