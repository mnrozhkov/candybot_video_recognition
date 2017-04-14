#!/usr/bin/env python3


class Body:

    def __init__(self):
        self.backlight_color = None

    def blink_backlight(self, times: int):
        print('body backlight blink:', times)

    def set_backlight_color(self, color):
        print('body backlight color:', color)
        self.backlight_color = color

    def turn_backlight_on(self):
        print('body backlight on')

    def turn_backlight_off(self):
        print('body backlight off')

    def turn_backlight_dim(self):
        print('body backlight dim')