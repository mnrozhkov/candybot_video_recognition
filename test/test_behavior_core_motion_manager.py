#!/usr/bin/env python3
'''
test for core_motion_manager
'''

import rospy
from coffebot.msg import EyebrowsMotion, HeadMotion, MotionPattern, Emotion

import sys
from pathlib import Path
top = Path(__file__).resolve().parents[1].as_posix()
sys.path.append(top)

from scripts.core_motion_manager import MotionMaker

import unittest

import time

BEHAVIOR_REACTION_TIMEOUT = 2 #seconds

class TestBehaviorCoreMotionManager(unittest.TestCase):

    def setUp(self):
        def all_data_recieved():
            return self.eyebrows_data_recieved and self.head_data_recieved

        self.all_data_recieved = all_data_recieved

        self.motion_maker = MotionMaker()

        self.eyebrows_motion =  None
        self.eyebrows_data_recieved = False
        self.head_motion = None
        self.head_data_recieved = False

        def callback_eyebrows(data: EyebrowsMotion):
            self.eyebrows_motion = data
            self.eyebrows_data_recieved = True

        def callback_head(data: HeadMotion):
            self.head_motion = data
            self.head_data_recieved = True

        self.eyebrows_sub = rospy.Subscriber('/motion_eyebrows_controller/eyebrows_motion', EyebrowsMotion, callback_eyebrows)
        self.head_sub = rospy.Subscriber('/motion_head_controller/head_motion', HeadMotion, callback_head)

    def tearDown(self):
        self.eyebrows_sub.unregister()
        self.head_sub.unregister()
        del(self.eyebrows_motion, self.eyebrows_data_recieved, self.head_motion, self.head_data_recieved, self.all_data_recieved)

    def test_set_neutral(self):
        start = time.time()
        while time.time() - start < BEHAVIOR_REACTION_TIMEOUT and self.eyebrows_data_recieved is False:
            self.motion_maker._set_neutral()

        start = time.time()
        while time.time() - start < BEHAVIOR_REACTION_TIMEOUT and self.eyebrows_data_recieved is False:
            time.sleep(0.1)

        self.assertEqual(self.eyebrows_motion, EyebrowsMotion(l_angle=30.0, r_angle=30.0, emotion='neutral'))

    def test_set_happy(self):
        start = time.time()
        while time.time() - start < BEHAVIOR_REACTION_TIMEOUT and self.all_data_recieved() is False:
            self.motion_maker._set_happy()

        start = time.time()
        while time.time() - start < BEHAVIOR_REACTION_TIMEOUT and self.all_data_recieved() is False:
            time.sleep(0.1)

        self.assertEqual(self.eyebrows_motion, EyebrowsMotion(l_angle=-30.0, r_angle=-30.0, emotion='neutral'))
        self.assertEqual(self.head_motion, HeadMotion(v_angle=150.0, emotion='neutral'))

    def test_set_sad(self):
        start = time.time()
        while time.time() - start < BEHAVIOR_REACTION_TIMEOUT and self.all_data_recieved() is False:
            self.motion_maker._set_sad()

        start = time.time()
        while time.time() - start < BEHAVIOR_REACTION_TIMEOUT and self.all_data_recieved() is False:
            time.sleep(0.1)

        self.assertEqual(self.eyebrows_motion, EyebrowsMotion(l_angle=30.0, r_angle=30.0, emotion='neutral'))
        self.assertEqual(self.head_motion, HeadMotion(h_angle=45.0, v_angle=45.0, emotion='neutral'))

    def test_set_fear(self):
        start = time.time()
        while time.time() - start < BEHAVIOR_REACTION_TIMEOUT and self.head_data_recieved is False:
            self.motion_maker._set_fear()

        start = time.time()
        while time.time() - start < BEHAVIOR_REACTION_TIMEOUT and self.head_data_recieved is False:
            time.sleep(0.1)

        self.assertEqual(self.head_motion, HeadMotion(v_angle=45.0, emotion='neutral'))

    def test_set_surprise(self):
        start = time.time()
        while time.time() - start < BEHAVIOR_REACTION_TIMEOUT and self.all_data_recieved() is False:
            self.motion_maker._set_surprise()

        start = time.time()
        while time.time() - start < BEHAVIOR_REACTION_TIMEOUT and self.all_data_recieved() is False:
            time.sleep(0.1)

        self.assertEqual(self.eyebrows_motion, EyebrowsMotion(l_angle=30.0, r_angle=30.0, emotion='neutral'))
        self.assertEqual(self.head_motion, HeadMotion(v_angle=150.0, emotion='neutral'))

    def test_set_angry(self):
        start = time.time()
        while time.time() - start < BEHAVIOR_REACTION_TIMEOUT and self.all_data_recieved() is False:
            self.motion_maker._set_angry()

        start = time.time()
        while time.time() - start < BEHAVIOR_REACTION_TIMEOUT and self.all_data_recieved() is False:
            time.sleep(0.1)

        self.assertEqual(self.eyebrows_motion, EyebrowsMotion(l_angle=-30.0, r_angle=-30.0, emotion='neutral'))
        self.assertEqual(self.head_motion, HeadMotion(v_angle=45.0, emotion='neutral'))

    def test_make_motions(self):
        self.pattern_pub = rospy.Publisher('/core_decision_manager/pattern', MotionPattern, queue_size=1)
        self.pattern_msg = MotionPattern(name='sayHello')
        self.emotion_pub = rospy.Publisher('/core_decision_manager/emotion', Emotion, queue_size=1)
        self.emotion_msg = Emotion(name='happy')

        start = time.time()
        while time.time() - start < BEHAVIOR_REACTION_TIMEOUT and self.all_data_recieved() is False:
            self.emotion_pub.publish(self.emotion_msg)
            self.pattern_pub.publish(self.pattern_msg)
            self.motion_maker.make_motions()

        start = time.time()
        while time.time() - start < BEHAVIOR_REACTION_TIMEOUT and self.all_data_recieved() is False:
            time.sleep(0.1)

        self.assertEqual(self.eyebrows_motion, EyebrowsMotion(l_angle=30.0, r_angle=30.0, emotion='neutral'))
        self.assertEqual(self.head_motion, HeadMotion(v_angle=150.0, emotion='neutral'))

        self.pattern_pub.unregister()
        self.emotion_pub.unregister()

        del(self.pattern_msg, self.emotion_msg)

if __name__ == '__main__':
    rospy.init_node('test_core_motion_manager')
    unittest.main()
