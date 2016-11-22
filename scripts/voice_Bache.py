#!/usr/bin/env python3
'''Allows to listen and recognize speech'''


import os
from pocketsphinx import get_model_path, Decoder
import pyaudio
import time
import audioop
import argparse
import random
import logging

logging.basicConfig(filename='Bache.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.ERROR)

def init():
    '''Initialize Pocketsphinx Decoder and acoustic model path, audio stream

    Returns:
    [decoder, stream]: list 
    '''
    #create ROS Publisher
    try:
        
        model_path = get_model_path()

        #set up decoder configuration
        config = Decoder.default_config()
        config.set_string('-hmm', os.path.join(model_path, 'ru-ru'))
        config.set_string('-dict', os.path.join(model_path, 'Bache.dic'))
        config.set_string('-lm', os.path.join(model_path, 'Bache.lm.bin'))
        
        decoder = Decoder(config)

        #initialize recognition
        decoder.start_utt()

        #set up pyaudio configuration and start audio stream
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
        stream.start_stream()

        return [decoder, stream]
    except Exception as e:
        logging.error(str(e))
        return None


def record(last_chunk, stream, min_rms):
    '''Records speech until silence
    Args:
        last_chunk: last chunk before record starting
        stream: audio stream
        min_rms: minimal rms value that is not silence
    Returns:
        buf: contains recorded audio data, bytes type
    '''
    try:
        buf = last_chunk
        silence_start = time.time()
        while (time.time() - silence_start) < 2:
            chunk = stream.read(1024)
            if audioop.rms(chunk, 2) >= min_rms / 3 :
                buf += chunk
            if audioop.rms(chunk, 2) >= min_rms:
                silence_start = time.time()
        return buf
    except Exception as e:
        logging.error(str(e))


def recognize(buf, decoder):
    '''Recognizes speech
    Args:
        buf: audio data, bytes type
        decoder: object of Decoder class, Pocketsphinx
    Returns:
        task_sentence: phrase to make decision if keyword detected
    '''
    try:
        decoder.process_raw(buf, False, False)
        if not decoder.hyp() is None:
            recognized_phrase = decoder.hyp().hypstr
            decoder.end_utt()
            decoder.start_utt()
            return recognized_phrase
                
        decoder.end_utt()
        decoder.start_utt()
    except Exception as e:
        logging.error(str(e))
    return None


init_list = init()
if init_list is None:
    exit()
decoder, stream = init_list
min_rms=500

def listen():
    global stream
    global decoder
    global min_rms
    
    while True:
        chunk = stream.read(1024)
        #if sound detected record raw data until silence
        if audioop.rms(chunk, 2) >=  min_rms:
            buf = record(last_chunk=chunk, stream=stream, min_rms=min_rms)
            text = recognize(buf=buf, decoder=decoder)
            if not text is None:
                return text


#----------------------Bache------------------------

objects = 15
max_at_step = 3


def print_objects():
    '''Print string objects representation
    '''
    
    global objects
    
    obj_str = ''
    obj_str += str(objects) + ':'
    for i in range(0,objects):
        obj_str += '|'
    print(obj_str)


def computer_step():
    '''Computer does step
    '''
    
    global objects
    print('Ходит компьютер...')
    if objects > 1:
        comp_step = random.randint(1,min(max_at_step,objects-1))
        objects -= comp_step
        print_objects()
    else:
        if objects == 1:
            print('Человек победил')
        elif objects <= 0:
            print('Компьютер победил')
        return
    
    human_step()


number = {'один': 1, 'два': 2, 'три': 3}


def human_step():
    '''Human does step
    '''
    
    global objects
    print('Ходит человек...')
    if objects > 1:
        step = listen()
        if number[step] < 1 or number[step] > 3:
            human_step()
            return
        objects -= number[step]
        print_objects()
    else:
        print("Компьютер победил")
        return

    computer_step()
    
#----------------------Bache------------------------


def choose_player():
    '''Chooses first player
    '''
    
    print('Назовите первого игрока (я - человек, компьютер - компьютер): ')
    fst_player = listen()
    if fst_player == 'компьютер':
        computer_step()
    elif fst_player == 'я':
        human_step()
    else:
        choose_player()
    
def main(objs=15):
    global objects
    objects = objs
    
    print_objects()
    choose_player()

if __name__ == '__main__':
   main()
