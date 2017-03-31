#!/usr/bin/env python3


class Body:

    def __init__(self):
        self.backlight_color = None

    def blink_backlight(self):
        print('body backlight')

    def turn_on_backlight(self):
        print('body turn on backlight')

    def set_backlight_color(self, color):
        print('body backlight color:', color)
        self.backlight_color = color
