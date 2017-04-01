#!/usr/bin/env python3

import rospy
import std_msgs

import json

import time


class Decision:

    def __init__(self):
        self._reset_fields()

        self._create_subscribers()
        self._create_publishers()

    def _reset_fields(self):
        self.bot_text_answer = None
        self.bot_action_answer = str()
        self.bot_action_parameter_answer = dict()
        self.smile_exists = False
        self.face_coords = dict()
        self.face_info = dict()
        self.user_emotion = str()

    def _create_subscribers(self):

        def callback_face_info(data: std_msgs.msg.String) -> None:
            self.face_info = json.loads(data.data)
            emotions = self.face_info['emotions']
            emotion_confidence = 0.0
            self.user_emotion = None
            for emotion_name in emotions.keys():
                if emotions[emotion_name] > emotion_confidence:
                    emotion_confidence = emotions[emotion_name]
                    self.user_emotion = emotion_name


        def callback_face_coords(data: std_msgs.msg.String) -> None:
            self.face_coords = json.loads(data.data)


        def callback_smile(data: std_msgs.msg.Bool) -> None:
            if data.data is True:
                self.smile_exists = True


        def callback_bot_dialog(data: std_msgs.msg.String) -> None:
            bot_answer = json.loads(data.data)
            self.bot_text_answer = bot_answer['text']
            if 'action' in bot_answer.keys():
                self.bot_action_answer = bot_answer['action']['name']
                self.bot_action_parameter_answer = bot_answer['action']['parameters']


        rospy.Subscriber('face_info', std_msgs.msg.String, callback_face_info)
        rospy.Subscriber('face_coord', std_msgs.msg.String, callback_face_coords)
        rospy.Subscriber('smile', std_msgs.msg.Bool, callback_smile)
        rospy.Subscriber('bot_dialog', std_msgs.msg.String, callback_bot_dialog)

    def _create_publishers(sefl):
        self.pattern_publisher = rospy.Publisher('pattern', std_msgs.msg.String, queue_size=1)
        self.emotion_publisher = rospy.Publisher('emotion', std_msgs.msg.String, queue_size=1)
        self.make_video_publisher = rospy.Publisher('make_video', std_msgs.msg.String, queue_size=1)
        self.make_photo_publisher = rospy.Publisher('make_photo', std_msgs.msg.String, queue_size=1)
        self.dialog_bot_publisher = rospy.Publisher('user_speech_text', std_msgs.msg.String, queue_size=1)
        self.speech_synthesis_publisher = rospy.Publisher('bot_speech_text', std_msgs.msg.String, queue_size=1)

    def make_decision(self) -> None:
        '''
        1. takes inputs
        2. makes decisions
        '''

        if len(bot_text_answer) > 0:
            self.speech_synthesis_publisher.publish(bot_text_answer)
            if bot_action_answer is not None:
                if bot_action_answer == 'action.hello.sayHello':
                    self.pattern_publisher.publish('sayHello')

        else:
            if bot_action_answer is None:
                if smile_exists is True:
                    self.dialog_bot_publisher.publish('привет')

        self._reset_fields()


if __name__ == '__main__':

    rospy.init_node('core_decision_manager')

    decision = Decision()
    while True:
        decision.make_decision()
        time.sleep(0.1)
