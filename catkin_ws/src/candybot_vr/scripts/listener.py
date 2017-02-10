#!/usr/bin/env python3
'''Allows to listen and recognize speech'''

import sys

from candybot_vr.audio.recognizer import SpeechRecognizer

'''
DO NOT DELETE NEXT 2 LINES PLEASE - IT IS FOR DEBUGGING AND TESTING
sys.path.insert(0, '..')
from src.candybot_vr.audio.recognizer import SpeechRecognizer
'''
import rospy
from std_msgs.msg import String
import logging

logging.basicConfig(filename='listener.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.ERROR)


def send_task_sentense(data, publisher):
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
    Args:
       min_rms: minimal rms value that is not silence
       keyword: keyword which must be detected to make decision
    
    '''
    #set listening parameter 
    rospy.set_param('listening', True)
    min_rms=500
    sr = SpeechRecognizer(min_rms=min_rms)
        
    publisher = rospy.Publisher('audio_decision', String, queue_size=1)
    rospy.init_node('listener', anonymous=True)
    
    print('start listen')
    while True:
        if rospy.get_param('listening'):
           
            #if sound detected record raw data until silence
            if rospy.has_param('min_rms'):
                min_rms = rospy.get_param('min_rms')
                sr.set_min_rms(min_rms)
            text = sr.listen('yandex')
            if not text is None :
                print(text)
                send_task_sentense(text, publisher=publisher)


if __name__ == '__main__':
    main()
