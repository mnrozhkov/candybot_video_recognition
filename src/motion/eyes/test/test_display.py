#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2017 FunRobots Lab

# Project: Candybot: candybot_v2
# Summary: Test for motion_eyes_controller
# version: v1

import os
import sys
from pathlib import Path

top = Path(__file__).resolve().parents[1]
sys.path.append(str(top))

from eyes_lib import get_device, draw_eye, set_display_frame_rate, create_canvas, convert_params_to_coord


### Tests for hardware
# ______________________

def test_display_st7735():
    num_iterations = sys.maxsize
    device = get_device()
    frame_count = 0
    fps = ""
    regulator = set_display_frame_rate(fps=10)

    while num_iterations > 0:
        with regulator:
            num_iterations -= 1
            frame_count += 1
            with create_canvas(device) as canvas:
                draw_eye(canvas, "test", 50, 50, 82, 82, fill='#1c86ee', outline='#000000')


if __name__ == "__main__":
    try:
        test_display_st7735()
    except KeyboardInterrupt:
        pass
