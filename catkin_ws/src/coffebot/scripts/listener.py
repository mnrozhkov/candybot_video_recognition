#!/usr/bin/env python3
'''Allows to listen and recognize speech'''

import sys

from coffebot.audio.recorder import Recorder

import rospy
from std_msgs.msg import String
import base64
import logging

logging.basicConfig(filename='listener.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.ERROR)


def send_task_sentense(data: str, publisher: rospy.Publisher):
    '''Send sentence with task
    Args:
        data: data to send
        publisher: Publisher object
    '''
    try:
        publisher.publish(data)
    except Exception as e:
        logging.error(str(e))


def main():
    '''Main function. Listens all time. If text detected it is sended to
    audio decision module       
    '''
    #set listening parameter 
    min_rms=500
    audio_recorder = Recorder(min_rms=min_rms, pyaudio_config=rospy.get_param('pyaudio'))
        
    publisher = rospy.Publisher('audio_capture', String, queue_size=1)
    rospy.init_node('listener')
    
    print('start listen')
    while True:
        
        #if sound detected record raw data until silence
        if rospy.has_param('min_rms'):
            min_rms = rospy.get_param('min_rms')
            audio_recorder.set_min_rms(min_rms)
        raw_audio = audio_recorder.listen()
        str_raw_audio = base64.b64encode(raw_audio).decode('utf-8')
        send_task_sentense(str_raw_audio, publisher=publisher)


if __name__ == '__main__':
    main()
