#!/usr/bin/env python3

import rospy
from coffebot.msg import MotionPattern, Emotion

import json
import yaml

import time

import sys

BASE_PATH = sys.path[0]

import logging
import os
LOG_FOLDER = 'logs'
if os.path.exists(LOG_FOLDER) is False:
    os.mkdir(LOG_FOLDER)

logging.basicConfig(filename=LOG_FOLDER + '/' + __name__ + '.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.DEBUG)


class MotionMaker:
    '''
    1. recieves robot emotion name and motion pattern name
    2. makes motions
    '''

    def __init__(self):

        #emotions-motions dictionary
        self.emotion_actions = {
            'neutral' : self._set_neutral,
            'happy'   : self._set_happy,
            'sad'     : self._set_sad,
            'fear'    : self._set_fear,
            'surprise': self._set_surprise,
            'angry'   : self._set_angry,
            'thinking': self._set_thinking
        }

        self.pattern_name = None
        self.emotion = None


        def callback_pattern(data: MotionPattern) -> None:
            '''
            recieve pattern name
            '''

            self.pattern_name = data.name


        def callback_emotion(data: Emotion) -> None:
            '''
            recieve emotion name
            '''

            self.emotion = data.name
            print(self.emotion)

        self.pattern_sub = rospy.Subscriber('pattern', MotionPattern, callback_pattern)
        self.emotion_sub = rospy.Subscriber('emotion', Emotion, callback_emotion)


    def _reset_fields(self):
        '''
        create or reset class fields
        '''

        self.pattern_name = None
        self.emotion = None

    def _set_neutral(self) -> None:
        self.eyebrows.move_up(0)
        self.eyebrows.turn_backlight_dim()
        self.eyebrows.set_backlight_color(color='orange')

        self.body.turn_backlight_on()
        self.body.set_backlight_color(color='orange')

    def _set_happy(self) -> None:
        self.head.move_up()
        self.head.shake_left_right(5)

        self.eyebrows.move_down()
        self.eyebrows.turn_backlight_dim()
        self.eyebrows.set_backlight_color(color='orange')

        self.body.turn_backlight_dim()
        self.body.set_backlight_color(color='orange')

    def _set_sad(self) -> None:
        self.head.turn_left()
        self.head.move_down()

        self.eyebrows.move_up()
        self.eyebrows.turn_backlight_off()

        self.body.turn_backlight_off()


    def _set_fear(self) -> None:
        self.head.move_down()

        self.eyebrows.blink_backlight(30)
        self.eyebrows.set_backlight_color(color='orange')

        self.body.blink_backlight(30)
        self.body.set_backlight_color(color='orange')

    def _set_surprise(self) -> None:
        self.head.move_up()

        self.eyebrows.move_up()
        self.eyebrows.turn_backlight_on()
        self.eyebrows.set_backlight_color(color='blue')

        self.body.turn_backlight_on()
        self.body.set_backlight_color(color='blue')

    def _set_angry(self) -> None:
        self.head.move_down()
        self.head.shake_left_right(30)

        self.eyebrows.move_down()
        self.eyebrows.turn_backlight_dim()
        self.eyebrows.set_backlight_color(color='red')

        self.body.turn_backlight_dim()
        self.body.set_backlight_color(color='red')

    def _set_thinking(self) -> None:
        pass

    def get_emotion(self) -> str:
        return self.emotion

    def set_emotion(self, emotion: str) -> None:
        '''
        set new robot emotion
        '''

        self.emotion_actions[emotion]()
        self.emotion = emotion

    def _make_head_motions(self, head_motions: dict or None):
        print('head motion')

    def _make_eyes_motions(self, eyes_motions: dict or None):
        print('eyes motion')

    def _make_eyebrows_motions(self, eyebrows_motions: dict or None):
        print('eyebrows motion')

    def _make_body_motions(self, body_motions: dict or None):
        print('body motion')

    def make_motions(self):
        '''
        make motions by robot emotion and pattern content
        '''

        emotion = self.emotion
        pattern_name = self.pattern_name

        try:
            if emotion is not None:
                self.set_emotion(emotion)

            if pattern_name is not None:
                pattern_path = BASE_PATH + '/motion_patterns/' + pattern_name + '.yaml'
                pattern = yaml.load(open(pattern_path,'r'))
                pattern_steps = pattern['steps']
                print(pattern_steps)
                step_count = len(pattern_steps)
                i = 0
                while i < step_count:

                    step = pattern_steps[i]['step']
                    print(step)
                    step_emotion = step.get('emotion')
                    if step_emotion is not None:
                        self.set_emotion(step_emotion)

                    motions = step.get('motions')
                    if motions is not None:

                        head_motions = motions.get('head')
                        self._make_head_motions(head_motions)

                        eyes_motions = motions.get('eyes')
                        self._make_eyes_motions(eyes_motions)

                        eyebrows_motions = motions.get('eyebrows')
                        self._make_eyebrows_motions(eyebrows_motions)

                        body_motions = motions.get('body')
                        self._make_body_motions(body_motions)

                    i += 1

        except Exception as e:
            logging.error(str(e))
        finally:
            if self.emotion == emotion:
                self.emotion = None
            if self.pattern_name == pattern_name:
                self.pattern_name = None


if __name__ == '__main__':

    rospy.init_node('core_motion_manager')

    motion_maker = MotionMaker()
    print('motion making start')
    while True:
        try:
            rospy.get_master().getPid()
        except:
            break

        motion_maker.make_motions()
        time.sleep(0.5)
