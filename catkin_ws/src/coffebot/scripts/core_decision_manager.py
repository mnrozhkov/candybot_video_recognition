#!/usr/bin/env python3

import rospy
from coffebot.msg import MotionPattern, Emotion, MakeVideo, MakePhoto
from coffebot.msg import UserSpeechText, BotSpeechText, APIAIBotAnswer
from coffebot.msg import FaceCoordinates, SmileDetected, FaceFeatures
import json

import time


class Decision:

    def __init__(self):
        self.bot_text_answer = None
        self.bot_action_answer = None
        self.bot_action_parameter_answer = dict()
        self.smile_exists = False
        self.face_coords = dict()
        self.face_info = dict()
        self.user_emotion = str()

        self._create_subscribers()
        self._create_publishers()

    def _create_subscribers(self):
        '''
        create Subscribers with theirs callbacks
        '''

        def callback_face_info(data: FaceFeatures) -> None:
            '''
            1. recieve face features information
            2. extract user emotion from it
            '''

            self.face_info = dict()
            self.face_info['emotions'] = json.loads(data.emotions)
            self.face_info['celebrities_similarity'] = json.loads(data.celebrities_similarity)
            self.face_info['gender'] = json.loads(data.gender)
            self.face_info['age'] = json.loads(data.age)

            emotions = self.face_info['emotions']
            emotion_confidence = 0.0
            self.user_emotion = None
            for emotion_name in emotions.keys():
                if emotions[emotion_name] > emotion_confidence:
                    emotion_confidence = emotions[emotion_name]
                    self.user_emotion = emotion_name


        def callback_face_coords(data: FaceCoordinates) -> None:
            '''
            recieve closest face coordinates
            '''

            self.face_coords = dict({'x': int(data.x), 'y': int(data.y), 'w': int(data.w), 'h': int(data.h)})


        def callback_smile(data: SmileDetected) -> None:
            '''
            recieve information about smile at closest face existance
            '''
            print('callback_smile:', data.detected)
            if data.detected is True:
                self.smile_exists = True


        def callback_bot_dialog(data: APIAIBotAnswer) -> None:
            '''
            1. recieve api.ai bot answer
            2. extract from the answer speech text, action name and action parameters
            '''

            self.bot_text_answer = data.text
            if len(data.action_name) > 0:
                self.bot_action_answer = data.action_name
            if len(data.action_parameters_in_json) > 0:
                self.bot_action_parameter_answer = json.loads(data.action_parameters_in_json)


        rospy.Subscriber('face_info', FaceFeatures, callback_face_info)
        rospy.Subscriber('face_coord', FaceCoordinates, callback_face_coords)
        rospy.Subscriber('smile_detected', SmileDetected, callback_smile)
        rospy.Subscriber('bot_dialog', APIAIBotAnswer, callback_bot_dialog)

    def _create_publishers(self):
        self.pattern_publisher = rospy.Publisher('pattern', MotionPattern, queue_size=1)
        self.emotion_publisher = rospy.Publisher('emotion', Emotion, queue_size=1)
        self.make_video_publisher = rospy.Publisher('make_video', MakeVideo, queue_size=1)
        self.make_photo_publisher = rospy.Publisher('make_photo', MakePhoto, queue_size=1)
        self.dialog_bot_publisher = rospy.Publisher('user_speech_text', UserSpeechText, queue_size=1)
        self.speech_synthesis_publisher = rospy.Publisher('bot_speech_text', BotSpeechText, queue_size=1)

    def make_decision(self) -> None:
        '''
        1. takes inputs
        2. makes decisions
        '''
        bot_text_answer = self.bot_text_answer
        bot_action_answer = self.bot_action_answer
        smile_exists = self.smile_exists

        if bot_text_answer is not None and len(bot_text_answer) > 0:
            bot_speech_text_msg = BotSpeechText()
            bot_speech_text_msg.text = self.bot_text_answer
            self.speech_synthesis_publisher.publish(bot_speech_text_msg)
            if bot_action_answer is not None:
                print('bot_action_answer', bot_action_answer)
                pattern_msg = MotionPattern()
                if bot_action_answer == 'action.hello':
                    pattern_msg.name = 'sayHello'
                elif bot_action_answer == 'action.hello.doIntroduction':
                    pattern_msg.name = 'dointroduction'
                elif bot_action_answer == 'action.service.coffeOrder':
                    pattern_msg.name = 'coffeOrder'
                elif bot_action_answer == 'action.service.promo.feedback':
                    pattern_msg.name = 'feedback'
                elif bot_action_answer == 'action.service.goodbye':
                    pattern_msg.name = 'goodbye'

                self.pattern_publisher.publish(pattern_msg)

        else:
            if bot_action_answer is None:
                if smile_exists is True:
                    user_speech_text_msg = UserSpeechText()
                    user_speech_text_msg.text = 'привет'
                    self.dialog_bot_publisher.publish(user_speech_text_msg)

        if self.bot_text_answer == bot_text_answer:
            self.bot_text_answer = None
        if self.bot_action_answer == bot_action_answer:
            self.bot_action_answer = None
        if self.smile_exists == smile_exists:
            self.smile_exists = False


if __name__ == '__main__':

    rospy.init_node('core_decision_manager')

    decision = Decision()
    while True:
        try:
            rospy.get_master().getPid()
        except:
            break

        decision.make_decision()
        time.sleep(0.1)
