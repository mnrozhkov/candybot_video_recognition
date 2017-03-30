#!/usr/bin/env python3


class Emotion:

    def __init__(self):

        self.emotion_actions = {
            'neutral' : None,
            'happy'   : None,
            'sad'     : None,
            'fear'    : None,
            'surprise': None,
            'angry'   : None,
            'thinking': None
        }

        self.emotion = None

    def get_emotion() -> str or None:
        return self.emotion

    def set_emotion(emotion: str):

        emotion_action = self.emotion_actions[emotion]
        if callable(emotion_action) is True:
            emotion_action()
        
        self.emotion = emotion
