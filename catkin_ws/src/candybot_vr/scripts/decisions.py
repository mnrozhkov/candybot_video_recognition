#!/usr/bin/env python3
'''Meke decision by recieved data'''

import rospy
import aiml
import os
import sys

from urllib import request, parse
#from gtts import gTTS
import io
import pyaudio
import wave


from std_msgs.msg import String
#from candybot_vr.util import rus_ascii_filter

import subprocess

import logging

logging.basicConfig(filename='desicions.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.ERROR)

class Bot:

    def __init__(self, aiml_folder):
        self.kernel = aiml.Kernel()
        self.base_path = sys.path[0]
        self._aiml_folder = aiml_folder
        self._learn()

    def _learn(self):
        files = os.listdir('/'.join([self.base_path, self._aiml_folder]))
        for file in files:
            if file[-4:] == 'aiml':
                print(file)
                self.kernel.learn('/'.join([self.base_path,self._aiml_folder,file]))

    def respond(self,qst=''):
        return self.kernel.respond(qst)


class Talker:

    def __init__(self):

        self.TTSs = {'rhvoice': self._sayrhvoice,
                     'yandex': self._sayyandex,
                     'google': self._saygoogle
                     }

    def _play_wav(self, wav_src):

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

    
    def _sayrhvoice(self, text):
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


    def _sayyandex(self, text):
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
        

    def _saygoogle(self, text):
        pass

    def say(self, tts_name, text):
        print('--say--')
        self.TTSs[tts_name](text)

    def tts_names():
        return list(self.TTSs.keys())

bot = Bot('aiml')


def run_processes(*args):
    '''Resumes viewing and listening'''
    for arg in args:
    	rospy.set_param(arg, True)


def stop_processes(*args):
    '''Stops viewing and listening'''

    for arg in args:
    	rospy.set_param(arg, False)

    
def callback_listen(data):
    '''Listening callback function.
    Args:
        data: listen data, ROS String type
    '''
    global bot
    
    if rospy.get_param('listening'):
        stop_processes('listening', 'viewing')
        d = data.data
        print('listened: ', d)
        text = bot.respond(d)
        print('bot answer: ', text)
        if len(text) > 0:
            talker = Talker()
            talker.say('yandex',text)
    run_processes('listening', 'viewing')

    if not (rospy.get_param('listening') or rospy.get_param('viewing')):
        run_processes('listening', 'viewing')

    
def callback_view(data):
    '''Listening callback function.
    Args:
        data: listen data, VisionMessage type, see msg/VisionMessage.msg
    '''
    global bot
    
    if rospy.get_param('viewing'):
        stop_processes('listening', 'viewing')
        d = data.data
        print(d)
        text = bot.respond(d)
        run_processes('listening', 'viewing')

    if not (rospy.get_param('listening') or rospy.get_param('viewing')):
        run_processes('listening', 'viewing')

def recieve():
	'''Recieves messages from listener and viewer
	'''
	
	rospy.init_node('decision_maker', anonymous=True)
	rospy.Subscriber('audio_decision', String, callback_listen)
	rospy.Subscriber('vision_decision', String, callback_view)
	print('I ready to recieve messages')
	rospy.spin()

def main():
    
    recieve()


if __name__ == '__main__':
    main()
