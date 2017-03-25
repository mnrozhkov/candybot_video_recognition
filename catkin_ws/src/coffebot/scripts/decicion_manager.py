#!/usr/bin/env python3
'''
    1. recieve strings from 2 topic - audio_capture and image_capture
    2. convert strings to adudio and image data
    3. process theese data - analyze data and extract features:
        2.1 by adudio - with audio recognition and api.ai bot
        2.2 by image - with face emotions, position recognition and smile detection

    4. make decision by processing information
    5. publish decision to decision_publication topic
'''

import rospy
import std_msgs

from coffebot.BotClient import APIAIBot
from typing import Dict
import json

from coffebot.audio.synthesizer import Talker
from coffebot.audio.recognizer import SpeechRecognizer
from coffebot.vision.opencv.simple_tracker import SimpleTracker
from coffebot.vision.algorithmia import facial

from coffebot.vision import convert as vision_convert
from coffebot.audio import convert as audio_convert
import pyaudio
import numpy as np
import base64
import time
import logging

logging.basicConfig(filename='desicions.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.ERROR)


class DecisionMaker:
    '''
    Class DecisionMaker. Makes decisions.
    '''

    def __init__(self, bot_client_key, yandex_voice_key, algorithmia_api_key, decision_table):

        self._bot_client_key = bot_client_key
        self._yandex_voice_key = yandex_voice_key
        self._algorithmia_api_key = algorithmia_api_key
        self._decision_table = decision_table

        self.bot = APIAIBot(self._bot_client_key) #create object bot for using api.ai API
        self.talker = Talker(self._yandex_voice_key) #create object talker for TTS
        self.sr = SpeechRecognizer(self._yandex_voice_key)
        self.tracker = SimpleTracker(face_cascade_file='haarcascade_frontalface_default.xml', smile_cascade_file='haarcascade_smile.xml')
        facial.api_key = self._algorithmia_api_key

        self._set_topics()

        self.faces_log = 'faces.log'

    def _set_topics(self):
        self._bot_decision = None
        #self._view_decision = None
        self._emotion = 'neutral'
        self._smile_exists = False

        rospy.Subscriber('audio_capture', std_msgs.msg.String, self.callback_listen)
        rospy.Subscriber('image_capture', std_msgs.msg.String, self.callback_view)

        self._decision_publisher = rospy.Publisher('decision_publication', std_msgs.msg.String, queue_size=1)

    def _reset_local_decisions():
        self._bot_decision = None
        self._emotion = 'neutral'
        self._smile_exists = False

    def _request_bot(phrase):
        answer = self.bot.request(phrase)
        if answer is not None:
            print('answer:', answer)
            self._bot_decision = dict()
            self._bot_decision['text'] = answer['text']
            self._bot_decision['action'] = None

            print('bot answer: ', answer['text'])
            if 'action' in answer.keys():
                self._bot_decision['action'] = dict()
                self._bot_decision['action']['name'] = answer['action']['name']
                self._bot_decision['action']['parameters'] = answer['action']['parameters']


    def callback_listen(self, data: std_msgs.msg.String) -> None:
        '''Listening callback function.
        Args:
            data: listen data, ROS String type
        '''
        print(type(data))

        raw_audio = base64.b64decode(data.data.encode('utf-8'))
        wav = audio_convert.raw_audio2wav(raw_audio=raw_audio, pyaudio_config=rospy.get_param('pyaudio'))
        if wav is not None:
            print(wav[:10])
            phrase = self.sr.asr_yandex(wav_data=wav)
            if phrase is not None and len(phrase) > 0:
                print('listened: ', phrase)
                self._request_bot(phrase)

    def _all_image_info(self, image: bytes) -> dict:
        info = dict()
        info['emotions'] = facial.get_emotions(image)
        info['celebrities_similarity'] = facial.celebrities_similarity(image)
        info['gender'] = facial.gender(image)
        info['age'] = facial.age(image)
        return info

    def callback_view(self, data: std_msgs.msg.String):
        image = vision_convert.str2ndarray(data.data)
        if image is not None:
            png_image = vision_convert.ndarray2format(image)
            if png_image is not None:
                with open(self.faces_log, 'a') as faces_log_file:
                    face_info = self._all_image_info(png_image)
                    faces_log_file.write(str(face_info) + '\n')

            faces = self.tracker.find_faces(image)
            if faces is not None and len(faces) > 0:
                faces.sort()
                closest_face = faces[0]
                self._view_decision = closest_face
                self._smile_exists = closest_face.smile_exists



    def make_decision(self):
        decision = dict()

        if self._bot_decision is not None:
            decision['say_text'] = self._bot_decision['text']
            action = self._bot_decision['action']['name']

            if action == 'action.hello.sayHello':
                decision['hardware_actions'] = [
                    {
                        'name': 'headMoveToUser',
                        'parameters': {}
                    },
                    {
                        'name': 'eyebrowsMoveUpDown',
                        'parameters': {'direction': 'up'}
                    },
                    {
                        'name': 'bodyBacklightBlink',
                        'parameters': {'times': 3}
                    }
                ]

                decision['robot_emotion'] = 'surprise'
                string_decision = json.dumps(decision)
                self._decision_publisher.publish(string_decision)

                self._reset_local_decisions()


        elif self._smile_exists is True:
            self._request_bot('привет')


def main():
    rospy.init_node('decision_maker', anonymous=True)
    try:
        decision_maker = DecisionMaker(bot_client_key=rospy.get_param('bot_client_key'),
                                        yandex_voice_key=rospy.get_param('yandex_voice_key'),
                                        algorithmia_api_key=rospy.get_param('algorithmia_api_key'),
                                        decision_table=rospy.get_param('decision_table'))
    except Exception as e:
        logging.error(str(e))
        print(str(e))
        return

    print('I ready to recieve!')
    while True:
        decision_maker.make_decision()
        time.sleep(0.1)



if __name__ == '__main__':
    main()
