#!/usr/bin/env python3
'''
contain class SoundManager
'''

from coffebot.audio.player import Player
import io

import os
LOG_FOLDER = 'logs'
if os.path.exists(LOG_FOLDER) is False:
    os.mkdir(LOG_FOLDER)

logging.basicConfig(filename=LOG_FOLDER + '/' + __name__ + '.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.DEBUG)


class SoundManager:
    '''
    release playing sounds by its category name
    '''

    def __init__(self):

        self._action_sounds = {
            'make_photo': None #will be .wav file name
        }

        self._emotion_sounds = {
            'neutral'  : None,
            'happy'    : None,
            'sad'      : None,
            'fear'     : None,
            'surprise' : None,
            'angry'    : None,
            'thinking' : None
        }

        self._warning_sounds = {
            'attention': None,
            'warning'  : None
        }

        self._categories = {
            'actions': self.play_action_sound,
            'emotions': self.play_emotion_sound,
            'warnings': self.play_warning_sound
        }

        self._player = Player()

    def play_action_sound(self, action_name: str or None=None) -> None:
        if action_name is not None:
            try:
                f = io.BytesIO(self._action_sounds[action_name])
                f.seek(0)
                self._player.play_audio(f)
            except Exception as e:
                logging.error(str(e))

    def play_emotion_sound(self, emotion_name: str or None=None) -> None:
        if emotion_name is not None:
            try:
                f = io.BytesIO(self._emotion_sounds[emotion_name])
                f.seek(0)
                self._player.play_audio(f)
            except Exception as e:
                logging.error(str(e))

    def play_warning_sound(self, warning_type: str or None=None) -> None:
        if warning_type is not None:
            try:
                f = io.BytesIO(self._warning_sounds[warning_type])
                f.seek(0)
                self._player.play_audio(f)
            except Exception as e:
                logging.error(str(e))

    def play_sound(category_name: str or None=None, sound_in_category: str or None=None) -> None:
        if category_name is not None and sound_in_category is not None:
            self._categories[category_name](sound_in_category)
