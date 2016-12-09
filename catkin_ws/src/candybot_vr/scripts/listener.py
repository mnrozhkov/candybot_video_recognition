#!/usr/bin/env python3
'''Allows to listen and recognize speech'''


from candybot_vr.audio import speech_recognizer as sr

import rospy
from std_msgs.msg import String

import argparse

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


def main(keyword=None):
    '''Main function. Listens all time. If text detected it is sended to
    audio decision module
    Args:
       min_rms: minimal rms value that is not silence
       keyword: keyword which must be detected to make decision
    
    '''
    #set listening parameter 
    rospy.set_param('listening', True)
    
    
    #min_rms=2000

    if keyword is None:
        keyword='владимир'
        
    #min_rms = min_rms
    #keyword = keyword
    
    if not sr.init('ru-ru','rualt.dic','ru.lm.bin') is None:
        
        publisher = rospy.Publisher('audio_decision', String, queue_size=1)
        rospy.init_node('listener', anonymous=True)
        
        print('start listen')
        while True:
            if rospy.get_param('listening'):
               
                #if sound detected record raw data until silence
                min_rms = rospy.get_param('min_rms')
                if min_rms == 0:
                    min_rms = 1500
                sr.min_rms = min_rms
                text = sr.listen()
                if not text is None and text.find(keyword) > -1:
                    print(text)
                    keyword_pos = recognized_phrase.index(keyword)
                    task_sentence = recognized_phrase[index + len(keyword):len(recognized_phrase)]
                    send_task_sentense(task_sentence, publisher=publisher)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--keyword', dest='keyword')
    args = parser.parse_args()
    
    main(keyword=args.keyword)
