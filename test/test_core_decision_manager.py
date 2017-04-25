#!/usr/bin/env python3
import rospy
from coffebot.msg import MotionPattern, Emotion, MakeVideo, MakePhoto
from coffebot.msg import UserSpeechText, BotSpeechText, APIAIBotAnswer
from coffebot.msg import FaceCoordinates, SmileDetected, FaceFeatures
from coffebot.msg import MakePhotoAction, MakePhotoActionGoal
from coffebot.msg import MakeVideoAction, MakeVideoActionGoal

import sys
from pathlib import Path
top = Path(__file__).resolve().parents[1].as_posix()
sys.path.append(top)

from scripts.core_decision_manager import Decision

import json

import actionlib

import time

import unittest
import time

class TestCallbackFaceInfo(unittest.TestCase):
    '''
    Test for callback_face_info function in core_decision_manager node
    '''

    def test_valid_data_publish(self):
        '''
        test valid data publishing
        '''

        decision = Decision()
        pub = rospy.Publisher('/vision_face_recognition/face_info', FaceFeatures, queue_size=1)
        face_features = FaceFeatures(emotion='happy', celebrity_name='Jackie Chan', gender='male', min_age=20, max_age=40)
        start = time.time()
        while time.time() - start < 1:
            pub.publish(face_features)
            face_info = decision.face_info
            if len(face_info.keys()) > 0:
                break
            time.sleep(0.1)

        face_info = decision.face_info
        self.assertEqual(face_info['emotion'], 'happy')
        self.assertEqual(face_info['celebrity_name'], 'Jackie Chan')
        self.assertEqual(face_info['gender'], 'male')
        self.assertEqual(face_info['age'], [20, 40])

        decision._delete_subscribers()
        pub.unregister()

    def test_invalid_data_publish(self):
        '''
        test invalid data publish - wrong typo of one of message fields
        '''

        decision = Decision()

        pub = rospy.Publisher('/vision_face_recognition/face_info', FaceFeatures, queue_size=1)
        face_features = FaceFeatures(emotion=1, celebrity_name='Jackie Chan', gender='male', min_age=20, max_age=40)
        start = time.time()
        while time.time() - start < 1:
            try:
                pub.publish(face_features)
            except Exception as e:
                break
            face_info = decision.face_info
            if len(face_info.keys()) > 0:
                break
            time.sleep(0.1)
        face_info = decision.face_info
        self.assertEqual(face_info, dict())

        decision._delete_subscribers()
        pub.unregister()

    def test_wrong_type_data_publish(self):
        '''
        test wrong type data publishing - try publish message with one type
        in topic with other type
        '''

        decision = Decision()
        pub = rospy.Publisher('/vision_face_recognition/face_info', FaceCoordinates, queue_size=1)
        face_coords = FaceCoordinates()
        pub.publish(face_coords)
        start = time.time()
        while time.time() - start < 1:
            pub.publish(face_coords)
            face_coords_d = decision.face_coords
            if len(face_coords_d.keys()) > 0:
                break
            time.sleep(0.1)
        self.assertEqual(decision.face_coords, dict())

        decision._delete_subscribers()
        pub.unregister()

if __name__ == '__main__':
    rospy.init_node('test_core_decision_manager')
    unittest.main()
