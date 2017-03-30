#!/usr/bin/env python3

class Decision:

    def __init__(self):

        self.bot_text_answer = None
        self.bot_action_answer = None
        self.bot_action_parameter_answer = None
        self.smile_exists = False
        self.user_emotion = None


    def make_decision(bot_text_answer: str or None,
                      bot_action_answer: str='',
                      bot_action_parameter_answer: dict={},
                      smile_exists: bool=False,
                      user_emotion: str='neutral') -> dict or None:
        '''
        1. takes inputs
        2. returns pattern info
        '''
        pattern = dict()
        pattern['name'] = bot_action_answer
        pattern['speech_text'] = bot_text_answer
        pattern['action_parameters'] = bot_action_parameter_answer

        #decision making
        if bot_text_answer is None:
            if smile_exists is True:
                pattern['name'] = 'sayHelloFirst'

        return pattern
