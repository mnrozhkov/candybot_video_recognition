#!/usr/bin/env python3
'''Allows to listen and recognize speech'''


import os
from pocketsphinx import get_model_path, Decoder
import pyaudio
import wave
import io
import requests
import time
import random
import audioop
import xml.etree.ElementTree as ET
import base64
import json

from googleapiclient import discovery
import httplib2
from oauth2client.client import GoogleCredentials

import logging

logging.basicConfig(filename='speech_recognizer.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.ERROR)

class SpeechRecognizer:

    
    def __init__(self, model_prefix='ru-ru',dictionary='rualt.dic', lang_model='ru.lm.bin', min_rms=100):
        '''Initialize Pocketsphinx Decoder and acoustic model path, audio stream

        Returns:
        [decoder, stream]: list 
        '''
        self.ASRs = {'pocketsphinx': self.pocketsphinx,
            'google': self.google,
            'yandex': self.yandex
            }
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'google_credentials.json'
        try:
            self.model_path = get_model_path()
            self.min_rms = min_rms
            #set up decoder configuration
            self.config = Decoder.default_config()
            self.config.set_string('-hmm', os.path.join(self.model_path, model_prefix))
            self.config.set_string('-dict', os.path.join(self.model_path, dictionary))
            self.config.set_string('-lm', os.path.join(self.model_path, lang_model))
            
            self.decoder = Decoder(self.config)

            #initialize recognition
            self.decoder.start_utt()
        except Exception as e:
            logging.error(str(e))
        try:
            #set up pyaudio configuration and start audio stream
            self.audio = pyaudio.PyAudio()
            self.stream = self.audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
            self.stream.start_stream()
        except Exception as e:
            logging.error(str(e))

    def set_min_rms(self, min_rms):
        self.min_rms = min_rms

        
    def record(self, last_chunk):
        print('rec')
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
            while (time.time() - silence_start) < 1.2:
                chunk = self.stream.read(1024)
                if audioop.rms(chunk, 2) >= self.min_rms / 3 :
                    buf += chunk
                if audioop.rms(chunk, 2) >= self.min_rms:
                    silence_start = time.time()
            return (buf, self.audio.get_sample_size(pyaudio.paInt16))
        except Exception as e:
            logging.error(str(e))
            return (None, None)

    def _convert2wav(self, raw_data, samp_size):
        try:
            f = io.BytesIO()
            wave_writer = wave.Wave_write(f)
            wave_writer.setnchannels(1)
            wave_writer.setsampwidth(samp_size)
            wave_writer.setframerate(16000)
            wave_writer.writeframes(raw_data)

            f.seek(0)
            return f.read()
        except Exception as e:
            logging.error(str(e))
            return None

    def pocketsphinx(self, buf, samp_size):
        '''Recognizes speech
        Args:
            buf: audio data, bytes type
            decoder: object of Decoder class, Pocketsphinx
        Returns:
            task_sentence: phrase to make decision if keyword detected
        '''
        try:
            self.decoder.process_raw(buf, False, False)
            if not self.decoder.hyp() is None:
                recognized_phrase = self.decoder.hyp().hypstr
                self.decoder.end_utt()
                self.decoder.start_utt()
                return recognized_phrase
                    
            self.decoder.end_utt()
            self.decoder.start_utt()
        except Exception as e:
            logging.error(str(e))
        return None

    def _make_uuid(self):

        symbols = '0123456789abcdef'
        uuid = ''
        for i in range(32):
            uuid += symbols[random.randint(0, len(symbols) - 1)]
        return uuid

    def google(self, buf, samp_size):

        try:
            wav_data = self._convert2wav(buf, samp_size)

            # [START authenticating]
            DISCOVERY_URL = ('https://{api}.googleapis.com/$discovery/rest?'
                             'version={apiVersion}')


            # Application default credentials provided by env variable
            # GOOGLE_APPLICATION_CREDENTIALS
            def get_speech_service():
                credentials = GoogleCredentials.get_application_default().create_scoped(
                    ['https://www.googleapis.com/auth/cloud-platform'])
                http = httplib2.Http()
                credentials.authorize(http)

                return discovery.build(
                    'speech', 'v1beta1', http=http, discoveryServiceUrl=DISCOVERY_URL)
            # [END authenticating]

            # [START construct_request]
            speech_content = base64.b64encode(wav_data)

            service = get_speech_service()
            service_request = service.speech().syncrecognize(
                body={
                    'config': {
                        # There are a bunch of config options you can specify. See
                        # https://goo.gl/KPZn97 for the full list.
                        'encoding': 'LINEAR16',  # raw 16-bit signed LE samples
                        'sampleRate': 16000,  # 16 khz
                        # See http://g.co/cloud/speech/docs/languages for a list of
                        # supported languages.
                        'languageCode': 'ru-RU',  # a BCP-47 language tag
                    },
                    'audio': {
                        'content': speech_content.decode('UTF-8')
                        }
                    })
            # [END construct_request]
            # [START send_request]
            response = service_request.execute()

            result = ''
            max_conf = 0
            for answer in response.get('results', []):
                for alternative in answer['alternatives']:
                    if float(alternative['confidence'])  > max_conf:
                        max_conf = float(alternative['confidence'])
                        result = alternative['transcript']
            # [END send_request]
            return result
        except Exception as e:
            logging.error(str(e))
        return None


    def yandex(self, buf, samp_size):

        try:
            url = 'https://asr.yandex.net/asr_xml?uuid=' + self._make_uuid()
            url += '&key=49d9bb75-7419-45cc-9988-76052abc6c44&topic=queries'
            wav_data = self._convert2wav(buf, samp_size)
            
            r = requests.post(url, wav_data, headers={
                    'Host': 'asr.yandex.net',
                    'Content-Type': 'audio/x-wav'
            })
            
            root = ET.fromstring(r.text)
            max_conf = 0
            result = None
            for child in root:
                if child.tag == 'variant':
                    conf = float(child.attrib['confidence'])
                    if conf > max_conf:
                        max_conf = conf
                        result = child.text
                        
            return result
        except Exception as e:
            logging.error(str(e))
        return None

    
    def listen(self, asr_name):
               
        while True:
            chunk = self.stream.read(1024)
            #if sound detected record raw data until silence
            if audioop.rms(chunk, 2) >=  self.min_rms:
                (buf, samp_size) = self.record(last_chunk=chunk)
                if (not buf is None) and (not samp_size is None):
                    print('recorded!')
                    text = self.ASRs[asr_name](buf=buf, samp_size=samp_size)
                    return text

