#!/usr/bin/env python3

# -*- coding: utf-8 -*-
# Copyright (c) 2014-17 Richard Hull and contributors
# See LICENSE.rst for details.

import sys
from luma.core import cmdline, error
from luma.core.render import canvas
from luma.core.sprite_system import framerate_regulator
from luma.lcd.device import st7735

from pathlib import Path
top = Path(__file__).resolve().parents[1].as_posix()
sys.path.append(top)


EYES_LCD_CONFIG_FILE = top + "/conf/eyes.conf"

def load_config(path_to_config):
    """
    Load device configuration from file path and return list with parsed lines.

    :param path: Location of configuration file.
    :type path: str
    :rtype: list
    """
    args = []
    with open(path_to_config, 'r') as fp:
        for line in fp.readlines():
            if line.strip() and not line.startswith("#"):
                args.append(line.replace("\n", ""))

    return args


def get_device():
    """
    Create device from command-line arguments and return it.
    """
    config = load_config(EYES_LCD_CONFIG_FILE)
    parser = cmdline.create_parser(description='ST7735 128*128 configuration')
    args = parser.parse_args(config)

    # create device
    try:
        device = cmdline.create_device(args)
    except error.Error as e:
        parser.error(e)

    return device


def create_canvas(device):
    return canvas(device)


def set_display_frame_rate(fps):
    return framerate_regulator(fps)


def convert_params_to_coord(angle, distance_from_center_percent, outer_radius):
    import math

    if angle is None:
        angle = 0
    if distance_from_center_percent is None:
        distance_from_center_percent = 0

    angle_rad = math.radians(360 - angle)
    distance = distance_from_center_percent * outer_radius
    x = math.ceil(distance * math.cos(angle_rad))
    y = math.ceil(distance * math.sin(angle_rad))

    return x, y


def draw_eye(eyes_canvas, emotion, x0, y0, x1, y1, fill='#14F6FA', outline='#14F6FA'):
    eyes_canvas.ellipse((x0, y0, x1, y1), fill=fill, outline=outline)


def zip_wrapper(x_path, y_path, fillvalue=0):
    req_version = 3.5
    cur_version = float(str(sys.version_info.major) + '.' + str(sys.version_info.minor))

    if cur_version >= req_version:
        from itertools import zip_longest
        return zip_longest(x_path, y_path, fillvalue=0)
    else:
        from itertools import izip
        return izip(x_path, y_path, fillvalue=0)
