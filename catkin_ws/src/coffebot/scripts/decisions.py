#!/usr/bin/env python3
'''Meke decision by recieved data'''

import rospy
import os
import sys
from BotClient import APIAIBot

from urllib import request, parse
#from gtts import gTTS
import io
import pyaudio
import wave

from std_msgs.msg import String

import subprocess

import logging

logging.basicConfig(filename='desicions.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.ERROR)

from typing import List, Dict
import json


class Talker:

    def __init__(self):

        self.TTSs = {'rhvoice': self._sayrhvoice,
                     'yandex': self._sayyandex,
                     'google': self._saygoogle
                     }

    def _play_wav(self, wav_src: bytes):

        #define stream chunk   
        chunk = 1024  

        #open a wav format music  
        f = wave.Wave_read(wav_src) 
        #instantiate PyAudio  
        p = pyaudio.PyAudio()  
        #open stream  
        stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                        channels = f.getnchannels(),  
                        rate = f.getframerate(),  
                        output = True)  
        #read data  
        data = f.readframes(chunk)  

        #play stream  
        while data:  
            stream.write(data)  
            data = f.readframes(chunk)  

        #stop stream  
        stream.stop_stream()  
        stream.close()  

        #close PyAudio  
        p.terminate()

    
    def _sayrhvoice(self, text: str):
        '''Says text
        Args:
            text: text to say
        '''
        try:
            echo_proc = subprocess.Popen(['echo', text],
                                                 stdout=subprocess.PIPE)
            rhvoice_proc = subprocess.call(['spd-say', '-w', '-o', 'rhvoice',
                                            '-l', 'ru', '-e', '-t', 'male1'],
                                           stdin=echo_proc.stdout)

        except Exception as e:
            logging.error(str(e))


    def _sayyandex(self, text: str):
        try:
            url = 'https://tts.voicetech.yandex.net/generate?text='
            url += parse.quote(text)
            url += '&format=wav&lang=ru&speaker=ermil&key=49d9bb75-7419-45cc-9988-76052abc6c44'
            req = request.urlopen(url)

            self._play_wav(req)
            print('yandex!')
        except Exception as e:
            logging.error(str(e))
            print(str(e))
        

    def _saygoogle(self, text: str):
        pass

    def say(self, tts_name: str, text: str):
        print('--say--')
        self.TTSs[tts_name](text)

    def tts_names() -> List[str]:
        return list(self.TTSs.keys())

bot = APIAIBot(client_key=json.load(open('coffebot.config', 'r'))['client_key'])


def run_processes(*args):
    '''Resumes viewing and listening'''
    for arg in args:
    	rospy.set_param(arg, True)


def stop_processes(*args):
    '''Stops viewing and listening'''

    for arg in args:
    	rospy.set_param(arg, False)


def make_command(command: str, parameters: Dict):
	
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
	

def callback_listen(data):
    '''Listening callback function.
    Args:
        data: listen data, ROS String type
    '''
    global bot
    
    if rospy.get_param('listening'):
        stop_processes('listening')
        d = data.data
        print('listened: ', d)
        answer = bot.request(d)
        text = answer['text']
        print('bot answer: ', text)
        if len(text) > 0:
            talker = Talker()
            talker.say('yandex',text)
        if 'action' in answer.keys():
        	make_command(answer['action']['name'], answer['action']['parameters'])
    run_processes('listening')

    if not rospy.get_param('listening'):
        run_processes('listening')


def recieve():
	'''Recieves messages from listener and viewer
	'''
	
	rospy.init_node('decision_maker', anonymous=True)
	rospy.Subscriber('audio_decision', String, callback_listen)
	print('I ready to recieve messages')
	rospy.spin()

def main():
    
    recieve()


if __name__ == '__main__':
    main()
