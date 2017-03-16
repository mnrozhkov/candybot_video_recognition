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
format coffebot import convert
import pyaudio
import numpy as np
import logging

logging.basicConfig(filename='desicions.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.ERROR)


class DecisionMaker:
    
    def __init__(self):
    	
        self._parse_config()
        self.bot = APIAIBot(self._bot_client_key) #create object bot for using api.ai API
        self.talker = Talker(self._yandex_voice_key) #create object talker for TTS
        self.sr = SpeechRecognizer(self._yandex_voice_key)
        self.tracker = SimpleTracker(face_cascade_file='haarcascade_frontalface_default.xml')
        self._set_topics()
        
    def _set_topics(self):
    	self._listen_decision = None
    	self._view_decision = None
    	
        rospy.Subscriber('audio_capture', std_msgs.msg.String, self.callback_listen)
        rospy.Subscriber('image_capture', std_msgs.msg.String, self.callback_view)
        
    def _parse_config(self) -> None:
        config = json.load(open('coffebot.config', 'r'))
        self._bot_client_key = config['bot_client_key']
        self._yandex_voice_key = config['yandex_voice_key']

    def callback_listen(self, data: std_msgs.msg.String) -> None:
        '''Listening callback function.
        Args:
            data: listen data, ROS String type
        '''
        print(type(data))
        
        raw_audio = base64.b64decode(data.data)
        wav = convert.raw_audio2wav(raw_audio=raw_audio, pyaudio_config=rospy.get_param('pyaudio'))
        phrase = self.sr.asr_yandex(wav_data=wav)
        print('listened: ', phrase)
        answer = self.bot.request(phrase)
        
        self._listen_decision = dict()
        self._listen_decision['text'] = answer['text']
        self._listen_decision['command_info'] = None
        
        print('bot answer: ', answer['text'])
        if 'action' in answer.keys():
        	self._listen_decision['command_info'] = dict()
            self._listen_decision['command_info']['name'] = answer['action']['name']
            self._listen_decision['command_info']['parameters'] = answer['action']['parameters'])
    
    def callback_view(self, data: std_msgs.msg.String):
    	image = convert.str2ndarray(data.data)
    	faces = self.tracker.find_faces(image)
    	closest_face = faces.sort()[0]
    	
    	self._view_decision = closest_face
    
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
    	if self._listen_decision is not None:
    		say_text = self._listen_decision['text']
    		command_info = self._listen_decision['command_info']
    		if len(say_text) > 0:
    			self.talker.sayyandex(say_text)
    		if command_info is not None:
    			self.make_command(command_info['name'], command_info['parameters'])
    		
    		self._listen_decision = None
    	
    	if self._view_decision is not None:
    		print(self._view_decision)


def main():
    rospy.init_node('decision_maker', anonymous=True)
    decision_maker = DecisionMaker()
    


if __name__ == '__main__':
    main()
