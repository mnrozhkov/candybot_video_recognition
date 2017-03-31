#!/usr/bin/env python3

import rospy
import std_msgs

import json

import time


class Decision:

    def __init__(self):

        self.bot_text_answer = None
        self.bot_action_answer = str()
        self.bot_action_parameter_answer = dict()
        self.smile_exists = False
        self.user_emotion = str()

        self._create_subscribers()
        self._create_publishers()



    def _create_subscribers(self):

        def callback_face_info(data: std_msgs.msg.String) -> None:
            pass


        def callback_face_coord(data: std_msgs.msg.String) -> None:
            pass


        def callback_smile(data: std_msgs.msg.Bool) -> None:
            pass


        def callback_bot_dialog(data: std_msgs.msg.String) -> None:
            pass


        rospy.Subscriber('face_info', std_msgs.msg.String, callback_face_info)
        rospy.Subscriber('face_coord', std_msgs.msg.String, callback_face_coord)
        rospy.Subscriber('smile', std_msgs.msg.Bool, callback_smile)
        rospy.Subscriber('bot_dialog', std_msgs.msg.String, callback_bot_dialog)

    def _create_publishers(sefl):
        self.pattern_publisher = rospy.Publisher('pattern', std_msgs.msg.String, queue_size=1)
        self.emotion_publisher = rospy.Publisher('emotion', std_msgs.msg.String, queue_size=1)
        self.make_video_publisher = rospy.Publisher('make_video', std_msgs.msg.String, queue_size=1)
        self.make_photo_publisher = rospy.Publisher('make_photo', std_msgs.msg.String, queue_size=1)
        self.user_speech_text_publisher = rospy.Publisher('user_speech_text', std_msgs.msg.String, queue_size=1)
        self.bot_speech_text_publisher = rospy.Publisher('bot_speech_text', std_msgs.msg.String, queue_size=1)

    def make_decision(self) -> None:
        '''
        1. takes inputs
        2. makes decisions
        '''

        if len(bot_text_answer) > 0:
            decision['say_text'] = bot_text_answer
            if bot_action_answer is not None:
                if bot_action_answer == 'action.hello.sayHello':
                    dict['motion_pattern'] = 'sayHello'

        else:
            if bot_action_answer is None:
                if smile_exists is True:
                    dialog_bot_publisher = rospy.Publisher('user_speech_text', std_msgs.std.String, queue_size=1)
                    dialog_bot_publisher.publish('привет')


if __name__ == '__main__':

    rospy.init_node('core_decision_manager')

    decision = Decision()
    while True:
        decision.make_decision()
        time.sleep(0.1)
