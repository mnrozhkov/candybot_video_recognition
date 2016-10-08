#!/usr/bin/env python3
'''Meke decision by recieved data'''

import rospy
from std_msgs.msg import String
from candybot_vr.msg import VisionMessage
from candybot_vr.network.encyclopedia import Encyclopedia

import subprocess

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

def run_sensors():
    '''Resumes viewing and listening'''
    
    rospy.set_param('listening', True)
    rospy.set_param('viewing', True)

    
def callback_listen(data):
    '''Listening callback function.
    Args:
        data: listen data, ROS String type
    '''
    
    phrase = data.data.lower()
    
    if phrase.find('привет') > -1:
        say('привет')
          
    elif phrase.find('росси') > -1:
        encyclopedia = Encyclopedia('россия')
        say(encyclopedia.get_summary())

    else:
        encyclopedia = Encyclopedia(phrase)
        say(encyclopedia.get_summary())
        
    run_sensors()

    
def callback_view(data):
    '''Listening callback function.
    Args:
        data: listen data, VisionMessage type, see msg/VisionMessage.msg
    '''
    face_count = data.face_count
    smile_exists = data.smile

    if face_count > 6:
        say('Как вас много!')

    if smile_exists:
        say('Улыбка!')

    run_sensors()
    

def recieve():
    print('I ready to recieve messages')
    rospy.init_node('decision_maker', anonymous=True)
    rospy.Subscriber('audio_decision', String, callback_listen)
    rospy.Subscriber('vision_decision', VisionMessage, callback_view)
    rospy.spin()

def main():

    recieve()


if __name__ == '__main__':
    main()
