#!/usr/bin/env python3
import math

class Head:

    def __init__(self):
        self.coords = {'x': 0, 'y': 0}

    def turn_left(self, angle: float=math.pi / 4):
        print('head turn left:', angle)

    def turn_right(self, angle: float=math.pi / 4):
        pritn('head turn right:', angle)

    def turn_up(self, angle: float=math.pi / 4):
        print('head turn up:', angle)

    def turn_down(self, angle: float=math.pi / 4):
        print('head turn down:', angle)

    def nod_to_agree(self):
        print('head nod to agree')

    def nod_to_disagree(self):
        print('head nod to disagree')

    def move_to_coords(self, coords: dict={'x': 0, 'y': 0}):
        print('head move to:', coords)
        self.coords = coords



class Eyebrows:

    def __init__(self):
        self.backlight_color = None

    def move_up(self, angle: float=math.pi / 4):
        print('eyebrows move up:', angle)

    def move_down(self, angle: float=math.pi / 4):
        print('eyebrows move down:', angle)

    def turn_on_backlight(self):
        print('eyebrows backlight')

    def set_backlight_color(self, color):
        print('backlight:', color)
        self.backlight_color = color


class Eyes:

    def __init__(self):
        self.coords = {'x': 0, 'y': 0}

    def set_pupil_position(self, coords: dict={'x': 0, 'y': 0}):
        print('eyes pupil position:', coords)
        self.coords = coords

    def get_pupil_position(self) -> dict:
        return self.coords
