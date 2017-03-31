#!/usr/bin/env python3

from coffebot.motion.head_control import Head, Eyes, Eyebrows
from coffebot.motion.body_control import Body

class Emotion:

    def __init__(self):

        self.head = Head()
        self.eyes = Eyes()
        self.eyebrows = Eyebrows()
        self.body = Body()

        self.emotion_actions = {
            'neutral' : self._set_neutral,
            'happy'   : None,
            'sad'     : None,
            'fear'    : None,
            'surprise': None,
            'angry'   : None,
            'thinking': None
        }

        self.emotion = 'neutral'

    def _set_neutral(self) -> None:
        pass

    def get_emotion() -> str:
        return self.emotion

    def set_emotion(emotion: str) -> None:

        emotion_action = self.emotion_actions[emotion]
        if callable(emotion_action) is True:
            emotion_action()

        self.emotion = emotion
