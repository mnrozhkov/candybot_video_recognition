#!/usr/bin/env python3

import rospy
import std_msgs
from coffebot.msg import MotionPattern, Emotion

from coffebot.motion import head_control, body_control

import json
import yaml

import time

import sys

BASE_PATH = sys.path[0]


class MotionMaker:
    '''
    1. recieves robot emotion name and motion pattern name
    2. makes motions
    '''

    def __init__(self):
        #create objects of robot`s parts classes
        self.head = head_control.Head()
        self.eyes = head_control.Eyes()
        self.eyebrows = head_control.Eyebrows()
        self.body = body_control.Body()

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

        self.motion_publisher = rospy.Publisher('motion', std_msgs.msg.String, queue_size=1)


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

        self.pattern_sub = rospy.Subscriber('pattern', std_msgs.msg.String, callback_pattern)
        self.emotion_sub = rospy.Subscriber('emotion', std_msgs.msg.String, callback_emotion)


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
        '''
        parse head motions (from motion pattern)
        '''

        if head_motions is not None:

            head_turn_left = head_motions.get('turn_left')
            if head_turn_left is not None:
                if head_turn_left == 'default':
                    self.turn_left()
                else:
                    self.head.turn_left(head_turn_left)

            head_turn_right = head_motions.get('turn_right')
            if head_turn_right is not None:
                if head_turn_right == 'default':
                    sefl.head.turn_right()
                else:
                    self.head.turn_right(head_turn_right)

            head_move_up = head_motions.get('move_up')
            if head_move_up is not None:
                if head_move_up == 'default':
                    sefl.head.move_up()
                else:
                    self.head.move_up(head_move_up)

            head_move_down = head_motions.get('move_down')
            if head_move_down is not None:
                if head_move_down == 'default':
                    sefl.head.move_down()
                else:
                    self.head.move_down(head_move_down)

            head_nod_to_agree = head_motions.get('node_to_agree')
            if head_nod_to_agree is not None:
                if head_nod_to_agree is True:
                    sefl.head.node_to_agree()

            head_nod_to_disagree = head_motions.get('node_to_disagree')
            if head_nod_to_disagree is not None:
                if head_nod_to_disagree is True:
                    sefl.head.node_to_disagree()

            head_move_to_coords = head_motions.get('move_to_coords')
            if head_move_to_coords is not None:
                if head_move_to_coords == 'default':
                    sefl.head.move_to_coords()
                else:
                    self.head.move_to_coords(head_move_to_coords)

            head_shake_left_right = head_motions.get('shake_left_right')
            if head_shake_left_right is not None:
                if head_shake_left_right == 'default':
                    sefl.head.shake_left_right()
                else:
                    self.head.shake_left_right(head_shake_left_right)

    def _make_eyes_motions(self, eyes_motions: dict or None):
        '''
        parse eyes motions (from motion pattern)
        '''

        if eyes_motions is not None:

            eyes_pupil_position = eyes_motions.get('pupil_position')
            if eyes_pupil_position is not None:
                if eyes_pupil_position == 'default':
                    self.eyes.set_pupil_position()
                else:
                    self.eyes.set_pupil_position(eyes_pupil_position)

    def _make_eyebrows_motions(self, eyebrows_motions: dict or None):
        '''
        parse eyebrows motions (from motion pattern)
        '''

        if eyebrows_motions is not None:

            eyebrows_move_up = eyebrows_motions.get('move_up')
            if eyebrows_move_up is not None:
                if eyebrows_move_up == 'default':
                    self.eyebrows.move_up()
                else:
                    self.eyebrows.move_up(eyebrows_move_up)

            eyebrows_move_down = eyebrows_motions.get('move_down')
            if eyebrows_move_down is not None:
                if eyebrows_move_down == 'default':
                    self.eyebrows.move_down()
                else:
                    self.eyebrows.move_down(eyebrows_move_down)

            eyebrows_turn_backlight_on = eyebrows_motions.get('turn_backlight_on')
            if eyebrows_turn_backlight_on is not None:
                if eyebrows_turn_backlight_on is True:
                    self.eyebrows.turn_backlight_on()

            eyebrows_turn_backlight_off = eyebrows_motions.get('turn_backlight_off')
            if eyebrows_turn_backlight_off is not None:
                if eyebrows_turn_backlight_off is True:
                    self.eyebrows.turn_backlight_off()

            eyebrows_turn_backlight_dim = eyebrows_motions.get('turn_backlight_dim')
            if eyebrows_turn_backlight_dim is not None:
                if eyebrows_turn_backlight_dim is True:
                    self.eyebrows.turn_backlight_dim()

            eyebrows_backlight_color = eyebrows_motions.get('backlight_color')
            if eyebrows_backlight_color is not None:
                self.eyebrows.set_backlight_color(color = eyebrows_backlight_color)

            eyebrows_blink_backlight = eyebrows_motions.get('blink_backlight')
            if eyebrows_blink_backlight is not None:
                if eyebrows_blink_backlight == 'default':
                    self.eyebrows.blink_backlight()
                else:
                    self.eyebrows.blink_backlight(eyebrows_blink_backlight)

    def _make_body_motions(self, body_motions: dict or None):
        '''
        parse body motions (from motion pattern)
        '''

        if body_motions is not None:

            body_blink_backlight = body_motions.get('blink_backlight')
            if body_blink_backlight is not None:
                if body_blink_backlight == 'default':
                    self.body.blink_backlight()
                else:
                    self.body.blink_backlight(body_blink_backlight)

            body_turn_backlight_on = body_motions.get('turn_backlight_on')
            if body_turn_backlight_on is not None:
                if body_turn_backlight_on is True:
                    self.body.turn_backlight_on()

            body_turn_backlight_off = body_motions.get('turn_backlight_off')
            if body_turn_backlight_off is not None:
                if body_turn_backlight_off is True:
                    self.body.turn_backlight_off()

            body_turn_backlight_dim = body_motions.get('turn_backlight_dim')
            if body_turn_backlight_dim is not None:
                if body_turn_backlight_dim is True:
                    self.body.turn_backlight_dim()

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
            print(str(e))
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
