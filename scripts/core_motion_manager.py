#!/usr/bin/env python3

import rospy
from std_msgs.msg import Bool
from candybot_v2.msg import MotionPattern, Emotion, SmileDetected
from motion.body.body_publisher import BodyPublisher
from motion.eyebrows.eyebrows_publisher import EyebrowsPublisher
from motion.eyes.eyes_publisher import EyesPublisher
from motion.head.head_publisher import HeadPublisher

import yaml

import time

import sys
from pathlib import Path
top = Path(__file__).resolve().parents[1].as_posix()
sys.path.append(top)

from utils import ErrorLogger

import random

class MotionMaker:
    '''
    1. recieves robot emotion name and motion pattern name
    2. makes motions
    '''

    def __init__(self):

        self._body_publisher = BodyPublisher()
        self._eyebrows_publisher = EyebrowsPublisher()
        self._eyes_publisher = EyesPublisher()
        self._head_publisher = HeadPublisher()

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

        self.pattern_name = str()
        self.emotion = str()

        self.pattern_sub = rospy.Subscriber('/core_decision_manager/pattern', MotionPattern, self.callback_pattern)
        self.emotion_sub = rospy.Subscriber('/core_decision_manager/emotion', Emotion, self.callback_emotion)
        self.smile_sub = rospy.Subscriber('/vision_face_tracking/smile_detected', SmileDetected, self.callback_smile_detected)
        self.ask_for_sub = rospy.Subscriber('/core_motion_manager/speech_to_bot_detected', Bool, self.callback_ask_for_bot)

        self.eyebrows_position = 0
        self.head_h_position = 0
        self.eyebrows_pos_switch_time = time.time()


    def callback_pattern(self, data: MotionPattern) -> None:
        '''
        recieve pattern name
        '''
        if isinstance(data, MotionPattern):
            self.pattern_name = data.name


    def callback_emotion(self, data: Emotion) -> None:
        '''
        recieve emotion name
        '''

        if isinstance(data, Emotion):
            self.emotion = data.name

    def callback_smile_detected(self, data: SmileDetected):
        if isinstance(data, SmileDetected) is True:
            if data.detected is True:
                self._eyebrows_publisher.move_up()
                self.eyebrows_position = 0

    def callback_ask_for_bot(self, data: Bool):
        if isinstance(data, Bool) is True:
            if data.data is True:
                self._eyebrows_publisher.move_up()
                self.eyebrows_position = 0

    def _set_neutral(self) -> None:
        self._head_publisher.move_to_face()

        self._eyebrows_publisher.move_up()
        # self._eyebrows.turn_backlight_dim()
        # self._eyebrows.set_backlight_color(color='orange')
        #
        # self._body.turn_backlight_on()
        # self._body.set_backlight_color(color='orange')

    def _set_happy(self) -> None:

        self._head_publisher.move_to_face()

        self._head_publisher.move_up()
        #self._head.shake_left_right(5)

        self._eyebrows_publisher.move_down()
        # self._eyebrows.turn_backlight_dim()
        # self._eyebrows.set_backlight_color(color='orange')
        #
        # self._body.turn_backlight_dim()
        # self._body.set_backlight_color(color='orange')

    def _set_sad(self) -> None:
        self._head_publisher.move_to_face()

        self._head_publisher.move_down_left()

        self._eyebrows_publisher.move_up()
        # self._eyebrows.turn_backlight_off()
        #
        # self._body.turn_backlight_off()


    def _set_fear(self) -> None:

        self._head_publisher.move_to_face()
        self._head_publisher.move_down()

        # self._eyebrows.blink_backlight(30)
        # self._eyebrows.set_backlight_color(color='orange')
        #
        # self._body.blink_backlight(30)
        # self._body.set_backlight_color(color='orange')

    def _set_surprise(self) -> None:

        self._head_publisher.move_to_face()
        self._head_publisher.move_up()

        self._eyebrows_publisher.move_up()
        # self._eyebrows.turn_backlight_on()
        # self._eyebrows.set_backlight_color(color='blue')
        #
        # self._body.turn_backlight_on()
        # self._body.set_backlight_color(color='blue')

    def _set_angry(self) -> None:
        self._head_publisher.move_to_face()
        self._head_publisher.move_down()
        #self._head.shake_left_right(30)

        self._eyebrows_publisher.move_down()
        # self._eyebrows.turn_backlight_dim()
        # self._eyebrows.set_backlight_color(color='red')
        #
        # self._body.turn_backlight_dim()
        # self._body.set_backlight_color(color='red')

    def _set_thinking(self) -> None:
        pass

    def get_emotion(self) -> str:
        return self.emotion

    def set_emotion(self, emotion: str) -> None:
        '''
        set new robot emotion
        '''

        if emotion in self.emotion_actions.keys():
            self.emotion_actions[emotion]()
            self.emotion = emotion

    def _make_head_motions(self, head_motions: dict or None):
        if isinstance(head_motions, dict):
            for key in head_motions:
                if key in dir(self._head_publisher) and head_motions[key] is True:
                    self._head_publisher.__getattribute__(key)()

    def _make_eyes_motions(self, eyes_motions: dict or None):
        if isinstance(eyes_motions, dict):
            for key in eyes_motions:
                if key in dir(self._eyes_publisher) and eyes_motions[key] is True:
                    self._eyes_publisher.__getattribute__(key)()


    def _make_eyebrows_motions(self, eyebrows_motions: dict or None):
        if isinstance(eyebrows_motions, dict):
            for key in eyebrows_motions:
                if key in dir(self._eyebrows_publisher) and eyebrows_motions[key] is True:
                    self._eyebrows_publisher.__getattribute__(key)()


    def _make_body_motions(self, body_motions: dict or None):
        if isinstance(body_motions, dict):
            for key in body_motions:
                if key in dir(self._body_publisher) and body_motions[key] is True:
                    self._body_publisher.__getattribute__(key)()


    def make_motions(self):
        '''
        make motions by robot emotion and pattern content
        '''
        #self._head_publisher.move_to_face()

        if time.time() - self.eyebrows_pos_switch_time > 10:
            print('eyebrows move!')
            #self.head_h_position = random.randint(60,120)
            #self._head_publisher.set_h_angle(self.head_h_position)

            self.eyebrows_position = random.randint(0,2)
            if self.eyebrows_position == 0:
                self._eyebrows_publisher.move_up()
            elif self.eyebrows_position ==  1:
                self._eyebrows_publisher.set_center()
            else:
                self._eyebrows_publisher.move_down()

            # if self.head_h_position == 0:
            #     self._head_publisher.turn_right()
            # else:
            #     self._head_publisher.turn_left()
            # if self.eyebrows_position == 0:
            #     self._eyebrows_publisher.move_down()
            #     self.eyebrows_position = 1
            # elif self.eyebrows_position == 1:
            #     self._eyebrows_publisher.set_center()
            #     self.eyebrows_position = 2
            # else:
            #     pass
            self.eyebrows_pos_switch_time = time.time()

        '''
        emotion = self.emotion
        pattern_name = self.pattern_name

        try:
            if isinstance(emotion, str) and emotion in self.emotion_actions.keys():
                self.set_emotion(emotion)

            if isinstance(pattern_name, str):
                pattern_path = top + '/motion_patterns/' + pattern_name + '.yaml'
                pattern = yaml.load(open(pattern_path,'r'))
                pattern_steps = pattern['steps']
                step_count = len(pattern_steps)
                i = 0
                while i < step_count:

                    step = pattern_steps[i]['step']
                    print(step)
                    step_emotion = step.get('emotion')
                    if step_emotion is not None and len(emotion) == 0:
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
            ErrorLogger(__file__, e)
        finally:
            if self.emotion == emotion:
                self.emotion = str()
            if self.pattern_name == pattern_name:
                self.pattern_name = str()
        '''

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
