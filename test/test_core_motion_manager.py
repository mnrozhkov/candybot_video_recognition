#!/usr/bin/env python3
'''
test for core_motion_manager
'''

import rospy
from coffebot.msg import MotionPattern, Emotion
from coffebot.msg import BodyMotion, EyebrowsMotion, EyesMotion, HeadMotion

import sys
from pathlib import Path
top = Path(__file__).resolve().parents[1].as_posix()
sys.path.append(top)

from scripts.core_motion_manager import MotionMaker

import unittest

import time

BEHAVIOR_REACTION_TIMEOUT = 2 #seconds

class TestCallbackPattern(unittest.TestCase):

    def test_valid_data_publish(self):

        motion_maker = MotionMaker()

        pattern_publisher = rospy.Publisher('/core_decision_manager/pattern', MotionPattern, queue_size=1)
        pattern_msg = MotionPattern(name='sayHello')

        pattern_name = str()

        start = time.time()

        while time.time() - start < 1:
            pattern_publisher.publish(pattern_msg)
            pattern_name = motion_maker.pattern_name
            if len(pattern_name) > 0:
                break
            time.sleep(0.1)

        self.assertEqual(pattern_name, 'sayHello')

        pattern_publisher.unregister()
        motion_maker.pattern_sub.unregister()
        motion_maker.emotion_sub.unregister()

    def test_invalid_data_publish(self):

        motion_maker = MotionMaker()

        pattern_publisher = rospy.Publisher('/core_decision_manager/pattern', MotionPattern, queue_size=1)
        pattern_msg = MotionPattern(name=1)

        pattern_name = str()

        start = time.time()

        while time.time() - start < 1:
            try:
                pattern_publisher.publish(pattern_msg)
            except:
                break
            pattern_name = motion_maker.pattern_name
            time.sleep(0.1)

        self.assertEqual(pattern_name, str())

        pattern_publisher.unregister()
        motion_maker.pattern_sub.unregister()
        motion_maker.emotion_sub.unregister()

    def test_wrong_type_data_publish(self):

        motion_maker = MotionMaker()

        pattern_publisher = rospy.Publisher('/core_decision_manager/pattern', Emotion, queue_size=1)
        pattern_msg = Emotion(name='happy')

        pattern_name = str()

        start = time.time()

        while time.time() - start < 1:
            pattern_publisher.publish(pattern_msg)
            pattern_name = motion_maker.pattern_name
            if len(pattern_name) > 0:
                break
            time.sleep(0.1)

        self.assertNotEqual(pattern_name, str())

        pattern_publisher.unregister()
        motion_maker.pattern_sub.unregister()
        motion_maker.emotion_sub.unregister()


class TestCallbackEmotion(unittest.TestCase):

    def test_valid_data_publish(self):

        motion_maker = MotionMaker()

        emotion_publisher = rospy.Publisher('/core_decision_manager/emotion', Emotion, queue_size=1)
        emotion_msg = Emotion(name='happy')

        emotion_name = str()

        start = time.time()

        while time.time() - start < 1:
            emotion_publisher.publish(emotion_msg)
            emotion_name = motion_maker.emotion
            if len(emotion_name) > 0:
                break
            time.sleep(0.1)

        self.assertEqual(emotion_name, 'happy')

        emotion_publisher.unregister()
        motion_maker.pattern_sub.unregister()
        motion_maker.emotion_sub.unregister()

    def test_invalid_data_publish(self):

        motion_maker = MotionMaker()

        emotion_publisher = rospy.Publisher('/core_decision_manager/emotion', Emotion, queue_size=1)
        emotion_msg = Emotion(name=1)

        emotion_name = str()

        start = time.time()

        while time.time() - start < 1:
            try:
                emotion_publisher.publish(emotion_msg)
            except:
                break
            emotion_name = motion_maker.emotion
            time.sleep(0.1)

        self.assertEqual(emotion_name, str())

        emotion_publisher.unregister()
        motion_maker.pattern_sub.unregister()
        motion_maker.emotion_sub.unregister()

    def test_wrong_type_data_publish(self):

        motion_maker = MotionMaker()

        emotion_publisher = rospy.Publisher('/core_decision_manager/emotion', MotionPattern, queue_size=1)
        emotion_msg = Emotion(name='happy')

        emotion_name = str()

        start = time.time()

        while time.time() - start < 1:
            emotion_publisher.publish(emotion_msg)
            emotion_name = motion_maker.emotion
            if len(emotion_name) > 0:
                break
            time.sleep(0.1)

        self.assertNotEqual(emotion_name, str())

        emotion_publisher.unregister()
        motion_maker.pattern_sub.unregister()
        motion_maker.emotion_sub.unregister


if __name__ == '__main__':
    rospy.init_node('test_core_motion_manager')
    unittest.main()
