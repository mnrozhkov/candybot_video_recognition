#!/usr/bin/env python3
'''Allows to listen and recognize speech'''


import os
from pocketsphinx import get_model_path, Decoder
import pyaudio
import time
import audioop

import rospy
from std_msgs.msg import String

import argparse


def init():
    '''Initialize ROS Publisher, Pocketsphinx Desoder and acoustic
    model path, audio stream

    Returns:
    [decoder, stream, publisher]: list 
    '''
    #create ROS Publisher
    publisher = rospy.Publisher('listening', String, queue_size=10)
    rospy.init_node('audio', anonymous=True)
    
    model_path = get_model_path()

    #set up decoder configuration
    config = Decoder.default_config()
    config.set_string('-hmm', os.path.join(model_path, 'ru-ru'))
    config.set_string('-dict', os.path.join(model_path, 'ru.dict'))
    config.set_string('-lm', os.path.join(model_path, 'ru.lm.bin'))
    
    decoder = Decoder(config)

    #initialize recognition
    decoder.start_utt()

    #set up pyaudio configuration and start audio stream
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
    stream.start_stream()

    return [decoder, stream, publisher]    


def record(last_chunk, stream, min_rms):
    '''Records speech until silence
    Args:
        last_chunk: last chunk before record starting
        stream: audio stream
        min_rms: minimal rms value that is not silence
    Returns:
        buf: contains recorded audio data, bytes type
    '''
    
    buf = last_chunk
    silence_start = time.time()
    while (time.time() - silence_start) < 2:
        chunk = stream.read(1024)
        buf += chunk
        if audioop.rms(chunk, 2) >= min_rms:
            silence_start = time.time()
    print(0)
    return buf


def recognize(buf, decoder, keyword):
    '''Recognizes speech
    Args:
        buf: audio data, bytes type
        decoder: object of Decoder class, Pocketsphinx
        keyword: keyword which must be detected to make decision
    Returns:
        task_sentence: phrase to make decision if keyword detected
        '': if keyword not detected
    '''
    
    decoder.process_raw(buf, False, False)
    if not decoder.hyp() is None:
        recognized_phrase = decoder.hyp().hypstr
        if len(recognized_phrase) >= len(keyword):
            #if keyword detected
            print(recognized_phrase)
            if recognized_phrase.find(keyword) > -1:
                #form sentence (substring) for sending to audio_analyzer
                index = recognized_phrase.index(keyword)
                task_sentence = recognized_phrase[index + len(keyword):len(recognized_phrase)]

                decoder.end_utt()
                decoder.start_utt()
                return task_sentence
            
            else:
                decoder.end_utt()
                decoder.start_utt()
                return ''
        else:
            decoder.end_utt()
            decoder.start_utt()
            return ''
    else:
        decoder.end_utt()
        decoder.start_utt()
        return ''


def send_task_sentense(data, publisher):
    '''Send sentence with task
    Args:
        data: data to send
        publisher: Publisher object
    '''
    
    publisher.publish(data)

    
    
def main(min_rms=None, keyword=None):
    '''Main function. Listens all time. If text detected it is sended to
    audio decision module
    Args:
       min_rms: minimal rms value that is not silence
       keyword: keyword which must be detected to make decision
    
    '''

    if min_rms is None:
        min_rms=2000

    if keyword is None:
        keyword='владимир'
        
    min_rms = min_rms
    keyword = keyword
    
    decoder, stream, publisher = init()
    
    print('start')
    while True:
        chunk = stream.read(1024)
        #if sound detected record raw data until silence
        if audioop.rms(chunk, 2) >=  min_rms:
            buf = record(last_chunk=chunk, stream=stream, min_rms=min_rms)
            text = recognize(buf=buf, decoder=decoder, keyword=keyword)
            if not text is None:
                send_task_sentense(text, publisher=publisher)
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--min_rms', dest='min_rms')
    parser.add_argument('--keyword', dest='keyword')
    args = parser.parse_args()
    
    main(min_rms=args.min_rms, keyword=args.keyword)
