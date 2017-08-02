#!/usr/bin/env python3
import sys
sys.path.insert(1, '/usr/local/lib/python3.5/dist-packages')

import rospy
import smach

from candybot_v2.msg import *
from core.decision_state_machine import *

import unittest


class TestBotTextAnswerState(unittest.TestCase):

    def setUp(self):
        self.sm = smach.StateMachine(outcomes=['text_exists', 'text_does_not_exist'])

        with self.sm:
            smach.StateMachine.add('BotTextAnswerState', BotTextAnswerState(),
                                    transitions={'outcome1':'text_exists',
                                                 'outcome2':'text_does_not_exist'
                                                },
                                    remapping={'bot_text_answer':'bot_text_answer'})

    def test_text_exists(self):
        self.sm.userdata.bot_text_answer = 'привет'
        outcome = self.sm.execute()

        self.assertEqual(outcome, 'text_exists')

    def test_text_does_not_exist(self):
        self.sm.userdata.bot_text_answer = ''
        outcome = self.sm.execute()

        self.assertEqual(outcome, 'text_does_not_exist')

    def test_not_text_data(self):
        self.sm.userdata.bot_text_answer = 0
        outcome = self.sm.execute()

        self.assertEqual(outcome, 'text_does_not_exist')


class TestBotActionNameAnswerState(unittest.TestCase):

    def setUp(self):
        self.sm = smach.StateMachine(outcomes=['end'])

        with self.sm:
            smach.StateMachine.add('BotActionNameAnswerState', BotActionNameAnswerState(),
                                    transitions={'outcome1':'end'},
                                    remapping={'bot_action_answer':'bot_action_answer'})

    def test_action_name_exists(self):
        self.sm.userdata.bot_action_answer = 'hello.sayHello'
        outcome = self.sm.execute()

        self.assertEqual(outcome, 'end')

    def test_action_name_does_not_exist(self):
        self.sm.userdata.bot_action_answer = ''
        outcome = self.sm.execute()

        self.assertEqual(outcome, 'end')

    def test_action_name_is_not_string(self):
        self.sm.userdata.bot_action_answer = 0
        outcome = self.sm.execute()

        self.assertEqual(outcome, 'end')


class TestSmileExistsState(unittest.TestCase):

    def setUp(self):
        self.sm = smach.StateMachine(outcomes=['end'])

        with self.sm:
            smach.StateMachine.add('SmileExistsState', SmileExistsState(),
                                    transitions={'outcome1':'end'},
                                    remapping={'smile_exists':'smile_exists'})

    def test_smile_exists(self):
        self.sm.userdata.smile_exists = True
        outcome = self.sm.execute()

        self.assertEqual(outcome, 'end')

    def test_smile_does_not_exist(self):
        self.sm.userdata.smile_exists = False
        outcome = self.sm.execute()

        self.assertEqual(outcome, 'end')

    def test_smile_is_not_bool(self):
        self.sm.userdata.smile_exists = 0
        outcome = self.sm.execute()

        self.assertEqual(outcome, 'end')

if __name__ == '__main__':
    rospy.init_node('test_decision_state_machine')
    unittest.main()
