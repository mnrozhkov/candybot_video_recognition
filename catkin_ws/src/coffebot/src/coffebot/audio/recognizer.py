#!/usr/bin/env python3
'''
speech recognition
'''

import pyaudio
import wave
import io
import requests
import random
import xml.etree.ElementTree as ET

import logging
import os
LOG_FOLDER = 'logs'
if os.path.exists(LOG_FOLDER) is False:
    os.mkdir(LOG_FOLDER)

logging.basicConfig(filename=LOG_FOLDER + '/' + __name__ + '.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.DEBUG)

class SpeechRecognizer:


    def __init__(self, yandex_voice_key):
        self.yandex_voice_key = yandex_voice_key

    def _make_uuid(self):

        symbols = '0123456789abcdef'
        uuid = ''
        for i in range(32):
            uuid += symbols[random.randint(0, len(symbols) - 1)]
        return uuid

    def recognize_speech(self, wav_data: bytes) -> str:

        try:
            url = 'https://asr.yandex.net/asr_xml?uuid=' + self._make_uuid()
            url += '&key=' + self.yandex_voice_key + '&topic=queries'


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
