#!/usr/bin/env python3

import os
from pocketsphinx import get_model_path, Decoder
import subprocess
import pyaudio
import time
import audioop


def main():
    '''Listens all time. If text detected it is sended to
    audio decision module
    '''
    
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

    min_amplitude = 2000

    keyword = 'владимир'
    keyword_len = len(keyword)

    buf = b''
    print('start')
    while True:
        chunk = stream.read(1024)
        #if sound detected record raw data until silence
        if audioop.rms(chunk, 2) >=  min_amplitude:
            buf += chunk
            silence_start = time.time()
            while (time.time() - silence_start) < 2:
                chunk = stream.read(1024)
                buf += chunk
                if audioop.rms(chunk, 2) >= min_amplitude:
                    silence_start = time.time()
        #recognize recorded data
        decoder.process_raw(buf, False, False)
        if not decoder.hyp() is None:
            recognized_phrase = decoder.hyp().hypstr
            if len(recognized_phrase) >= keyword_len:
                #if keyword detected
                if recognized_phrase.find(keyword) > -1:
                    #form sentence (substring) for sending to audio_analyzer
                    index = recognized_phrase.index(keyword)
                    task_sentence = recognized_phrase[index + keyword_len:len(recognized_phrase)]

                    subprocess.call([os.getcwd() + '/audio_analyzer.py', task_sentence])
                    
                buf = b''            
                decoder.end_utt()
                decoder.start_utt()    
        


if __name__ == '__main__':
    main()
