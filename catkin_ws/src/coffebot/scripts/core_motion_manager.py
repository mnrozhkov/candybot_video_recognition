#!/usr/bin/env python3

import rospy
import std_msgs

from coffebot.motion import joint_control, head_control, body_control
from coffebot.core import emotion_manager

import json
import yaml

class MotionMaker:

    def __init__(self):

        self.head = Head()
        self.eyes = Eyes()
        self.eyebrows = Eyebrows()
        self.body = Body()

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
        self.emotion = 'neutral'
        self.position = None #???

        self.motion_publisher = rospy.Publisher('motion', std_msgs.msg.String, queue_size=1)


        def callback_pattern(data: std_msgs.msg.String) -> None:
            self.pattern_name = data.data


        def callback_emotion(data: std_msgs.msg.String) -> None:
            self.emotion = data.data


        def callback_position(data: std_msgs.msg.String) -> None:
            pass


        self.pattern_sub = rospy.Subscriber('pattern', std_msgs.msg.String, callback_pattern)
        self.emotion_sub = rospy.Subscriber('emotion', std_msgs.msg.String, callback_emotion)
        self.position_sub = rospy.Subscriber('position', std_msgs.msg.String, callback_position)


    def _set_neutral(self) -> None:
        self.eyebrows.move_up(0)
        self.eyebrows.turn_backlight_dim()
        self.eyebrows.set_backlight_color(color='orange')

        self.body.turn_backlight_on()
        self.body.set_backlight_color(color='orange')

    def _set_happy(self) -> None:
        self.head.turn_up()
        self.head.shake_left_right(5)

        self.eyebrows.turn_down()
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

    def set_emotion(emotion: str) -> None:

        self.emotion_actions[emotion]()
        self.emotion = emotion

    def load_motion_pattern(self):
        pass

    def make_motions(self):
        pass


if __name__ == '__main__':

    rospy.init_node('core_motion_manager')

    motion_maker = MotionMaker()
    motion_maker.make_motions()
    
    rospy.spin()
