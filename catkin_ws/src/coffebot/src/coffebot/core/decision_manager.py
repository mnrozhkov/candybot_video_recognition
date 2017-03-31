#!/usr/bin/env python3

class Decision:

    def __init__(self):

        self.bot_text_answer = None
        self.bot_action_answer = None
        self.bot_action_parameter_answer = None
        self.smile_exists = False
        self.user_emotion = None


    def make_decision(bot_text_answer: str='',
                      bot_action_answer: str or None=None,
                      bot_action_parameter_answer: dict={},
                      smile_exists: bool=False,
                      user_emotion: str='neutral') -> dict or None:
        '''
        1. takes inputs
        2. returns pattern info
        '''
        decision = dict()

        if len(bot_text_answer) > 0:
            decision['say_text'] = bot_text_answer
            if bot_action_answer is not None:
                if bot_action_answer == 'action.hello.sayHello':
                    dict['motion_pattern'] = 'sayHello'

        else:
            if bot_action_answer is None:
                if smile_exists is True:
                    dialog_bot_publisher = rospy.Publisher('user_speech_text', std_msgs.std.String, queue_size=1)
                    dialog_bot_publisher.publish('привет')
