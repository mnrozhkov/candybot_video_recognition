#!/usr/bin/env python3

import sys
sys.path.insert(1, '/usr/local/lib/python3.5/dist-packages')

import rospy
import smach
import smach_ros

from coffebot.msg import BotSpeechText, MotionPattern, Emotion, UserSpeechText


class BotTextAnswerState(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1', 'outcome2'],
                                   input_keys=['bot_text_answer']
                            )
        self.speech_synthesis_publisher = self.speech_synthesis_publisher = rospy.Publisher('/core_decision_manager/bot_speech_text', BotSpeechText, queue_size=1)

    def execute(self, userdata):
        if isinstance(userdata.bot_text_answer, str) and len(userdata.bot_text_answer) > 0:
            bot_speech_text_msg = BotSpeechText(text=self.bot_text_answer)
            self.speech_synthesis_publisher.publish(bot_speech_text_msg)
            return 'outcome1'

        return 'outcome2'


class BotActionNameAnswerState(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1', 'outcome2'],
                                   input_keys=['bot_action_answer']
                            )

        self.pattern_publisher = rospy.Publisher('/core_decision_manager/pattern', MotionPattern, queue_size=1)

    def execute(self, userdata):

        if isinstance(userdata.bot_action_answer, str) and len(userdata.bot_action_answer) > 0:
            print('bot_action_answer', bot_action_answer)
            pattern_msg = MotionPattern()
            if bot_action_answer == 'action.hello':
                pattern_msg.name = 'sayHello'
            elif bot_action_answer == 'action.hello.doIntroduction':
                pattern_msg.name = 'dointroduction'
            elif bot_action_answer == 'action.service.coffeOrder':
                pattern_msg.name = 'coffeOrder'
            elif bot_action_answer == 'action.service.promo.feedback':
                pattern_msg.name = 'feedback'
            elif bot_action_answer == 'action.service.goodbye':
                pattern_msg.name = 'goodbye'

            self.pattern_publisher.publish(pattern_msg)
            return 'outcome1'

        return 'outcome2'

class BotActionParametersAnswerState(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=[])

    def execute(self, userdata):

        return


class BotSmileExists(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1', 'outcome2'],
                                   input_keys=['smile_exists']
                            )
        self.emotion_publisher = rospy.Publisher('/core_decision_manager/emotion', Emotion, queue_size=1)
        self.dialog_bot_publisher = rospy.Publisher('/speech_recognition/user_speech_text', UserSpeechText, queue_size=1)

    def execute(self, userdata):
        if userdata.smile_exists is True:
            #set happy emotion as reaction on human smile
            emotion_msg = Emotion(name='happy')
            emotion_publisher.publish(emotion_msg)

            user_speech_text_msg = UserSpeechText(text='привет')
            self.dialog_bot_publisher.publish(user_speech_text_msg)
            return 'outcome1'

        return 'outcome2'
