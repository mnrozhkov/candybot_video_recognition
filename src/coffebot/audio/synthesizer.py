from urllib import request, parse

import sys
from pathlib import Path
top = Path(__file__).resolve().parents[0].as_posix()
sys.path.append(top)

from player import Player

import logging
import os
LOG_FOLDER = 'logs'
if os.path.exists(LOG_FOLDER) is False:
    os.mkdir(LOG_FOLDER)

logging.basicConfig(filename=LOG_FOLDER + '/' + __name__ + '.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.DEBUG)

class Talker:
    '''
    Text-to-speech class
    '''

    def __init__(self, yandex_voice_key: str):
        '''
        Constructor
        yandex_voice_key: access key for Yandex SpeechKit
        '''

        self.yandex_voice_key = yandex_voice_key
        self._player = Player()

    def text_to_speech(self, text: str) -> bytes or None:
        '''
        Translate text to speech
        Args:
            text: text to translate
        Returns:
            wave format audio bytes : if translated
            None : if failed
        '''

        try:
            url = 'https://tts.voicetech.yandex.net/generate?text='
            url += parse.quote(text)
            url += '&format=wav&lang=ru&speaker=ermil&key=' + self.yandex_voice_key
            req = request.urlopen(url)

            print('yandex!')
            return req.read()
        except Exception as e:
            logging.error(str(e))
            return None
