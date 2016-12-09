#!/usr/bin/env python3
'''Allows to listen and recognize speech'''


import os
from pocketsphinx import get_model_path, Decoder
import pyaudio
import time
import audioop
import logging

logging.basicConfig(filename='speech_recognizer.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.ERROR)

decoder = None
stream = None
min_rms = 100

def init(model_prefix,dictionary, lang_model):
    '''Initialize Pocketsphinx Decoder and acoustic model path, audio stream

    Returns:
    [decoder, stream]: list 
    '''
    global decoder
    global stream
    
    try:
        
        model_path = get_model_path()

        #set up decoder configuration
        config = Decoder.default_config()
        config.set_string('-hmm', os.path.join(model_path, model_prefix))
        config.set_string('-dict', os.path.join(model_path, dictionary))
        config.set_string('-lm', os.path.join(model_path, lang_model))
        
        decoder = Decoder(config)

        #initialize recognition
        decoder.start_utt()

        #set up pyaudio configuration and start audio stream
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
        stream.start_stream()

        return True
    except Exception as e:
        logging.error(str(e))
        return False


def record(last_chunk):
    '''Records speech until silence
    Args:
        last_chunk: last chunk before record starting
        stream: audio stream
        min_rms: minimal rms value that is not silence
    Returns:
        buf: contains recorded audio data, bytes type
    '''

    global stream
    global min_rms
    
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


def recognize(buf):
    '''Recognizes speech
    Args:
        buf: audio data, bytes type
        decoder: object of Decoder class, Pocketsphinx
    Returns:
        task_sentence: phrase to make decision if keyword detected
    '''

    global decoder
    
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


def listen():
    global decoder
    global stream
    global min_rms
    
    while True:
        chunk = stream.read(1024)
        #if sound detected record raw data until silence
        if audioop.rms(chunk, 2) >=  min_rms:
            buf = record(last_chunk=chunk)
            text = recognize(buf=buf)
            return text
