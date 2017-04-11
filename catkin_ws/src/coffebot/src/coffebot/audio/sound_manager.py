#!/usr/bin/env python3
'''
contain class SoundManager
'''

from coffebot.audio.player import Player
import io


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

        self._player = Player()

    def play_action_sound(self, action_name: str or None=None) -> None:
        if action_name is not None:
            f = io.BytesIO(self._action_sounds[action_name])
            f.seek(0)
            self._player.play_audio(f)

    def play_emotion_sound(self, emotion_name: str or None=None) -> None:
        if emotion_name is not None:
            f = io.BytesIO(self._emotion_sounds[emotion_name])
            f.seek(0)
            self._player.play_audio(f)

    def play_warning_sound(self, warning_type: str or None=None) -> None:
        if warning_type is not None:
            f = io.BytesIO(self._warning_sounds[warning_type])
            f.seek(0)
            self._player.play_audio(f)
