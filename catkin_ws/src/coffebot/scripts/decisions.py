#!/usr/bin/env python3
'''Meke decision by recieved data'''

import rospy
import std_msgs

from BotClient import APIAIBot
from typing import Dict
import json

from coffebot.audio.synthesizer import Talker
from coffebot.audio.recognizer import SpeechRecognizer
from coffebot.vision.opencv.simple_tracker import SimpleTracker
from coffebot.vision.algorithmia import facial

from coffebot import convert
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
            self._bot_decision['command_info'] = None

            print('bot answer: ', answer['text'])
            if 'action' in answer.keys():
                self._bot_decision['command_info'] = dict()
                self._bot_decision['command_info']['name'] = answer['action']['name']
                self._bot_decision['command_info']['parameters'] = answer['action']['parameters']


    def callback_listen(self, data: std_msgs.msg.String) -> None:
        '''Listening callback function.
        Args:
            data: listen data, ROS String type
        '''
        print(type(data))

        raw_audio = base64.b64decode(data.data.encode('utf-8'))
        wav = convert.raw_audio2wav(raw_audio=raw_audio, pyaudio_config=rospy.get_param('pyaudio'))
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
        image = convert.str2ndarray(data.data)
        if image is not None:
            png_image = convert.ndarray2format(image)
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

    def make_command(self, command: str, parameters: Dict) -> None:

        print('command: ', command, 'parameters: ', parameters)
        try:
            #split command into parts
            command_parts = command.split('.')
            #get command group
            command_group = command_parts[len(command_parts) - 2]
            #get command name
            command_name = command_parts[len(command_parts) - 1]
            #import command group module from command_modules folder
            command_module = __import__('command_modules.' + command_group)
            #call function with command name and parameters as arguments
            getattr(command_module, command_name)(parameters)
        except Exception as e:
            print(str(e))

    def make_decision(self):
        if self._bot_decision is not None:
            say_text = self._bot_decision['text']
            command_info = self._bot_decision['command_info']
            if len(say_text) > 0:
                self.talker.sayyandex(say_text)
            if command_info is not None:
                self.make_command(command_info['name'], command_info['parameters'])

            if self._bot_decision is None:
                if self._smile_exists is True:
                    self._request_bot('привет')

            #walk on decision tabel
            for row in self._decision_table:
                action, smile_exists, emotion = row['local_decision']
                if( (action == 'none' or action == self._bot_decision['command_info']['name']) and
                    (smile_exists == 'any' or (smile_exists == 'yes' and self._smile_exists is True) or (smile_exists == 'no' and self._smile_exists is False) ) and
                    (emotion == 'any' or emotion == self._emotion)
                  ):
                  robot_emotion = row['decision']['robot_emotion']
                  robot_action = row['decision']['robot_action']

                  #set emotion
                  command_module = __import__('command_modules.command')
                  getattr(command_module, showEmotion)(robot_emotion)

                  #make command
                  self._make_command({robot_action, command_info['parameters']})
                  break

            self._reset_local_decisions()

        if self._view_decision is not None:
            self._view_decision.printface()
            self._view_decision = None


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
