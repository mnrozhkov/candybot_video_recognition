#!/usr/bin/env python3
'''Meke decision by recieved data'''

import rospy
import aiml
import os
import sys

from std_msgs.msg import String
#from candybot_vr.util import rus_ascii_filter

import subprocess

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
    

bot = Bot('aiml')


def say(text):
    '''Says text
    Args:
        text: text to say
    '''
    
    echo_proc = subprocess.Popen(['echo', text],
                                         stdout=subprocess.PIPE)
    rhvoice_proc = subprocess.call(['spd-say', '-w', '-o', 'rhvoice',
                                    '-l', 'ru', '-e', '-t', 'male1'],
                                   stdin=echo_proc.stdout)

    
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
        say(text)
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
