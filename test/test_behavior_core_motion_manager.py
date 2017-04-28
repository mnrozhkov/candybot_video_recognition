#!/usr/bin/env python3
'''
test for core_motion_manager
'''

import rospy
from coffebot.msg import EyebrowsMotion, HeadMotion

import sys
from pathlib import Path
top = Path(__file__).resolve().parents[1].as_posix()
sys.path.append(top)

from scripts.core_motion_manager import MotionMaker

import unittest

import time

BEHAVIOR_REACTION_TIMEOUT = 4 #seconds

class TestBehaviorCoreMotionManager(unittest.TestCase):

    def test_set_neutral(self):

        motion_maker = MotionMaker()

        self.eyebrows_motion =  None
        self.eyebrows_data_recieved = False

        def callback_eyebrows(data: EyebrowsMotion):
            self.eyebrows_motion = data
            self.eyebrows_data_recieved = True

        eyebrows_sub = rospy.Subscriber('/motion_eyebrows_controller/eyebrows_motion', EyebrowsMotion, callback_eyebrows)

        start = time.time()

        while time.time() - start < BEHAVIOR_REACTION_TIMEOUT and self.eyebrows_data_recieved is False:
            motion_maker._set_neutral()

        start = time.time()

        while time.time() - start < BEHAVIOR_REACTION_TIMEOUT and self.eyebrows_data_recieved is False:
            time.sleep(0.1)

        self.assertEqual(self.eyebrows_motion, EyebrowsMotion(l_angle=30.0, r_angle=30.0, emotion='neutral'))

        eyebrows_sub.unregister()
        del(self.eyebrows_motion, self.eyebrows_data_recieved)

    def test_set_happy(self):

        motion_maker = MotionMaker()

        self.eyebrows_motion =  None
        self.head_motion = None
        self.eyebrows_data_recieved = False
        self.head_data_recieved = False

        def all_data_recieved():
            return self.eyebrows_data_recieved and self.head_data_recieved

        def callback_eyebrows(data: EyebrowsMotion):
            self.eyebrows_motion = data
            self.eyebrows_data_recieved = True

        def callback_head(data: HeadMotion):
            self.head_motion = data
            self.head_data_recieved = True

        eyebrows_sub = rospy.Subscriber('/motion_eyebrows_controller/eyebrows_motion', EyebrowsMotion, callback_eyebrows)
        head_sub = rospy.Subscriber('/motion_head_controller/head_motion', HeadMotion, callback_head)

        start = time.time()

        while time.time() - start < BEHAVIOR_REACTION_TIMEOUT and all_data_recieved() is False:
            motion_maker._set_happy()

        start = time.time()

        while time.time() - start < BEHAVIOR_REACTION_TIMEOUT and all_data_recieved() is False:
            time.sleep(0.1)

        self.assertEqual(self.eyebrows_motion, EyebrowsMotion(l_angle=-30.0, r_angle=-30.0, emotion='neutral'))
        self.assertEqual(self.head_motion, HeadMotion(v_angle=150.0, emotion='neutral'))

        eyebrows_sub.unregister()
        head_sub.unregister()
        del(self.eyebrows_motion, self.eyebrows_data_recieved, self.head_motion, self.head_data_recieved)

    def test_set_sad(self):
        motion_maker = MotionMaker()

        self.eyebrows_motion =  None
        self.head_motion = None
        self.eyebrows_data_recieved = False
        self.head_data_recieved = False

        def all_data_recieved():
            return self.eyebrows_data_recieved and self.head_data_recieved

        def callback_eyebrows(data: EyebrowsMotion):
            self.eyebrows_motion = data
            self.eyebrows_data_recieved = True

        def callback_head(data: HeadMotion):
            self.head_motion = data
            self.head_data_recieved = True

        eyebrows_sub = rospy.Subscriber('/motion_eyebrows_controller/eyebrows_motion', EyebrowsMotion, callback_eyebrows)
        head_sub = rospy.Subscriber('/motion_head_controller/head_motion', HeadMotion, callback_head)

        start = time.time()

        while time.time() - start < BEHAVIOR_REACTION_TIMEOUT and all_data_recieved() is False:
            motion_maker._set_sad()

        start = time.time()

        while time.time() - start < BEHAVIOR_REACTION_TIMEOUT and all_data_recieved() is False:
            time.sleep(0.1)

        self.assertEqual(self.eyebrows_motion, EyebrowsMotion(l_angle=30.0, r_angle=30.0, emotion='neutral'))
        self.assertEqual(self.head_motion, HeadMotion(h_angle=45.0, v_angle=45.0, emotion='neutral'))

        eyebrows_sub.unregister()
        head_sub.unregister()
        del(self.eyebrows_motion, self.eyebrows_data_recieved, self.head_motion, self.head_data_recieved)

    def test_set_fear(self):
        motion_maker = MotionMaker()

        self.head_motion = None
        self.head_data_recieved = False

        def callback_head(data: HeadMotion):
            self.head_motion = data
            self.head_data_recieved = True

        head_sub = rospy.Subscriber('/motion_head_controller/head_motion', HeadMotion, callback_head)

        start = time.time()

        while time.time() - start < BEHAVIOR_REACTION_TIMEOUT and self.head_data_recieved is False:
            motion_maker._set_fear()

        start = time.time()

        while time.time() - start < BEHAVIOR_REACTION_TIMEOUT and self.head_data_recieved is False:
            time.sleep(0.1)

        self.assertEqual(self.head_motion, HeadMotion(v_angle=45.0, emotion='neutral'))

        head_sub.unregister()
        del(self.head_motion, self.head_data_recieved)

    def test_set_surprise(self):

        motion_maker = MotionMaker()

        self.eyebrows_motion =  None
        self.head_motion = None
        self.eyebrows_data_recieved = False
        self.head_data_recieved = False

        def all_data_recieved():
            return self.eyebrows_data_recieved and self.head_data_recieved

        def callback_eyebrows(data: EyebrowsMotion):
            self.eyebrows_motion = data
            self.eyebrows_data_recieved = True

        def callback_head(data: HeadMotion):
            self.head_motion = data
            self.head_data_recieved = True

        eyebrows_sub = rospy.Subscriber('/motion_eyebrows_controller/eyebrows_motion', EyebrowsMotion, callback_eyebrows)
        head_sub = rospy.Subscriber('/motion_head_controller/head_motion', HeadMotion, callback_head)

        start = time.time()

        while time.time() - start < BEHAVIOR_REACTION_TIMEOUT and all_data_recieved() is False:
            motion_maker._set_surprise()

        start = time.time()

        while time.time() - start < BEHAVIOR_REACTION_TIMEOUT and all_data_recieved() is False:
            time.sleep(0.1)

        self.assertEqual(self.eyebrows_motion, EyebrowsMotion(l_angle=30.0, r_angle=30.0, emotion='neutral'))
        self.assertEqual(self.head_motion, HeadMotion(v_angle=150.0, emotion='neutral'))

        eyebrows_sub.unregister()
        head_sub.unregister()
        del(self.eyebrows_motion, self.eyebrows_data_recieved, self.head_motion, self.head_data_recieved)

    def test_set_angry(self):

        motion_maker = MotionMaker()

        self.eyebrows_motion =  None
        self.head_motion = None
        self.eyebrows_data_recieved = False
        self.head_data_recieved = False

        def all_data_recieved():
            return self.eyebrows_data_recieved and self.head_data_recieved

        def callback_eyebrows(data: EyebrowsMotion):
            self.eyebrows_motion = data
            self.eyebrows_data_recieved = True

        def callback_head(data: HeadMotion):
            self.head_motion = data
            self.head_data_recieved = True

        eyebrows_sub = rospy.Subscriber('/motion_eyebrows_controller/eyebrows_motion', EyebrowsMotion, callback_eyebrows)
        head_sub = rospy.Subscriber('/motion_head_controller/head_motion', HeadMotion, callback_head)

        start = time.time()

        while time.time() - start < BEHAVIOR_REACTION_TIMEOUT and all_data_recieved() is False:
            motion_maker._set_angry()

        start = time.time()

        while time.time() - start < BEHAVIOR_REACTION_TIMEOUT and all_data_recieved() is False:
            time.sleep(0.1)

        self.assertEqual(self.eyebrows_motion, EyebrowsMotion(l_angle=-30.0, r_angle=-30.0, emotion='neutral'))
        self.assertEqual(self.head_motion, HeadMotion(v_angle=45.0, emotion='neutral'))

        eyebrows_sub.unregister()
        head_sub.unregister()
        del(self.eyebrows_motion, self.eyebrows_data_recieved, self.head_motion, self.head_data_recieved)

    def test_set_emotion(self):
        pass

    def test_make_motion(self):
        pass

if __name__ == '__main__':
    rospy.init_node('test_core_motion_manager')
    unittest.main()
