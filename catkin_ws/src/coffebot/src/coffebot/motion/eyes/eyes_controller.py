#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 FunRobots Lab
# See LICENSE.rst for details.

"""
Candybot eyes module 

"""
from eyes_lib import convert_params_to_coord, draw_eye, zip_wrapper


class Eyes(object):
    def __init__(self, width, height, background_color, eye_radius, eye_color, pupil_radius, pupil_color):
        #LCD base settings
        self._w = width
        self._h = height
        self._color = background_color
        self._eye_radius = eye_radius
        self._eye_color = eye_color
        
        #Eyes base settings 
        self._x_center = int(self._w / 2)
        self._y_center = int(self._h / 2)
        self._x_pos = self._x_center
        self._y_pos = self._y_center
        self._pupil_radius = pupil_radius 
        self._pupil_orbit_radius = self._eye_radius - self._pupil_radius
        self._pupil_color = pupil_color
        
        #speed settings
        self._x_speed = 5
        self._y_speed = 5

        #other settings
        self._emotion = 'happy'



    def set_eyes_position(self, x_step = None, y_step = None):
        if x_step is None:
            x_step = 0
        if y_step is None:
            y_step = 0

        self._x_pos += x_step
        self._y_pos += y_step


    #eyes control methods
    def get_eyes_position(self):
        return (self._x_pos, self._y_pos)


    def set_path_to_move_eyes(self, x, y):
        '''
            Calculate a path to set a position for eyes to move.
        '''

        #define steps to set eyes into new position (x,y)
        def get_path_to_point(self, goal, self_pos, speed):

            path=[]
            steps = int(abs((goal - self_pos) / speed))
            # print(steps)
            if steps == 0:
                step_speed = 0
            else:
                step_speed = int((goal - self_pos) / steps)
            [path.append(step_speed) for step in range(0, steps)]
            if path==[]:
                path.append(0)

            return path
        
        x_path = get_path_to_point(self, x, self._x_pos,  self._x_speed)
        y_path = get_path_to_point(self, y, self._y_pos,  self._y_speed)

        return zip_wrapper(x_path, y_path, fillvalue=0)


    def set_emotion(self, emotion=None):
        if emotion is None:
            self._emotion = 'happy'
        else:
            self._emotion = emotion


    def get_emotion(self):
        return self._emotion



    def move_eyes(self, canvas, angle=None, distance_from_center_percent=None):

        # set default position
        if canvas is None:
            raise Exception('Error: canvas is None')

        # get new coords for eye pupil
        x_shift, y_shift = convert_params_to_coord(angle, distance_from_center_percent,
                                                   self._pupil_orbit_radius)
        x = x_shift + self._x_center
        y = y_shift + self._y_center

        #get path to move eyes
        path = self.set_path_to_move_eyes(x, y)



        # move eyes
        for x_step, y_step in path:
            # update eyes position
            self.set_eyes_position(x_step, y_step)

            # draw default eye (clear previous step)
            draw_eye(eyes_canvas=canvas,
                     emotion=self._emotion,
                     x0=0,
                     y0=0,
                     x1=self._x_center + self._eye_radius,
                     y1=self._y_center + self._eye_radius,
                     fill=self._eye_color,
                     outline=self._eye_color)

            # draw pupil
            draw_eye(eyes_canvas = canvas,
                     emotion = self._emotion,
                     x0 = self._x_pos - self._pupil_radius,
                     y0 = self._y_pos - self._pupil_radius,
                     x1 = self._x_pos + self._pupil_radius,
                     y1 = self._y_pos + self._pupil_radius,
                     fill=self._pupil_color,
                     outline=self._pupil_color)


# if __name__ == "__main__":
#     try:
#         main()
#     except KeyboardInterrupt:
#         pass
