#!/usr/bin/env python3
import math

class Head:

    def __init__(self):
        self.cartesian_coords = {'x': 0, 'y': 0}
        self.vertical_angle = 0
        self.horizontal_angle = 0

        self.led_on = None
        self.color = None
        self.mode = None
        self.frequency = None

    def turn_left(self, angle: float=math.pi / 4):
        print('head turn left:', angle)
        self.horizontal_angle = angle

    def turn_right(self, angle: float=math.pi / 4):
        pritn('head turn right:', angle)
        self.horizontal_angle = -angle

    def move_up(self, angle: float=math.pi / 4):
        print('head move up:', angle)
        self.vertical_angle = angle

    def move_down(self, angle: float=math.pi / 4):
        print('head move down:', angle)
        self.vertical_angle = -angle

    def nod_to_agree(self):
        print('head nod to agree')

    def nod_to_disagree(self):
        print('head nod to disagree')

    def move_to_coords(self, coords: dict={'x': 0, 'y': 0}):
        print('head move to:', coords)
        self.cartesian_coords = coords
        self.horizontal_angle = math.atan(x)
        self.vertical_angle = math.atan(y)

    def shake_left_right(self, times: int=1):
        print('head shake left-right')



