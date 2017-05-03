#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2017 FunRobots Lab
# See LICENSE.rst for details.

"""
Candybot eyes module

"""

import math
from itertools import zip_longest #use zip_longest for Python3
import rospy
from coffebot.msg import EyesMotion, EyesState
from coffebot.motion.eyes.eyes_controller import Eyes
from coffebot.motion.eyes.eyes_lib import get_device, create_canvas, get_device, convert_params_to_coord, draw_eye, \
    set_display_frame_rate, create_canvas, zip_wrapper
from coffebot.topic_controller import Lock

import sys

import time


def main(num_iterations=sys.maxsize):

    rospy.init_node('motion_eyes_controller')

    eyes_motion_lock = Lock()
    rospy.Subscriber('/motion_eyes_controller/eyes_motion', EyesMotion, eyes_motion_lock.callback)
    eyes_position_publisher = rospy.Publisher('eyes_state', EyesState, queue_size=1)

    eyes = Eyes(width=128,
                height=128,
                background_color='#ffffff',
                eye_radius=64,
                eye_color='#ffffff',
                pupil_radius=25,
                pupil_color='#1c86ee')

    # display settings
    # display settings
    device = get_device()
    frame_count = 0
    fps = ""
    regulator = set_display_frame_rate(fps=10)
    print('motion_eyes_controller start')
    while num_iterations > 0:
        with regulator:
            num_iterations -= 1

            frame_count += 1

            #read EyesMotion message
            eyes_motion_msg =  eyes_motion_lock.message

            # some subscribers code here


            #extract patameters from EyesMotion
            if isinstance(eyes_motion_msg, EyesMotion):
                angle = eyes_motion_msg.angle
                distance_from_center_percent = eyes_motion_msg.distance_from_center_percent
                emotion = eyes_motion_msg.emotion
            else:
                angle = None
                distance_from_center_percent = None
                emotion = None

            with create_canvas(device) as canvas:

                # check params
                if angle is None:
                    eyes.move_eyes(canvas)
                elif distance_from_center_percent is None:
                    # set default params to draw eyes in center position
                    eyes.move_eyes(canvas)

                # main instructions for eyes
                else:
                    # set eyes working mode
                    eyes.set_emotion(emotion)
                    eyes.move_eyes(canvas, angle, distance_from_center_percent)

                eyes_state_msg = EyesState()
                eyes_state_msg.x, eyes_state_msg.y = eyes.get_eyes_position()
                eyes_state_msg.emotion = eyes.get_emotion()

                eyes_position_publisher.publish(eyes_state_msg)
                
                #if new EyesMotion message is equal to the old one clear field message of Lock class object
                if eyes_motion_lock.message == eyes_motion_msg:
                    eyes_motion_lock.message = None
                    # additional code here (i.e. publish eyes state)

        time.sleep(0.5)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
