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

import json

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
            face_coords_dict = decision.face_coords
            if len(face_coords_dict.keys()) > 0:
                break
            time.sleep(0.1)
        self.assertEqual(decision.face_info, dict())

        decision._delete_subscribers()
        pub.unregister()


class TestCallbackFaceCoords(unittest.TestCase):
    '''
    Test for callback_face_coords function in core_decision_manager node
    '''

    def test_valid_data_publish(self):
        '''
        test valid data publishing
        '''

        decision = Decision()
        pub = rospy.Publisher('/vision_face_tracking/face_coord', FaceCoordinates, queue_size=1)
        face_coords_msg = FaceCoordinates(x=0, y=0, h=200, w=200)
        start = time.time()
        while time.time() - start < 1:
            pub.publish(face_coords_msg)
            face_coords_dict = decision.face_coords
            if len(face_coords_dict.keys()) > 0:
                break
            time.sleep(0.1)

        face_coords_dict = decision.face_coords
        self.assertEqual(face_coords_dict['x'], 0)
        self.assertEqual(face_coords_dict['y'], 0)
        self.assertEqual(face_coords_dict['h'], 200)
        self.assertEqual(face_coords_dict['w'], 200)

        decision._delete_subscribers()
        pub.unregister()

    def test_invalid_data_publish(self):
        '''
        test invalid data publish - wrong typo of one of message fields
        '''

        decision = Decision()

        pub = rospy.Publisher('/vision_face_tracking/face_coord', FaceCoordinates, queue_size=1)
        face_coords_msg = FaceCoordinates(x='hello', y=0, h=200, w=200)
        start = time.time()
        while time.time() - start < 1:
            try:
                pub.publish(face_coords_msg)
            except Exception as e:
                break
            face_coords_dict = decision.face_info
            if len(face_coords_dict.keys()) > 0:
                break
            time.sleep(0.1)
        face_coords_dict = decision.face_info
        self.assertEqual(face_coords_dict, dict())

        decision._delete_subscribers()
        pub.unregister()

    def test_invalid_data_publish2(self):
        '''
        test invalid data publish - wrong typo of one of message fields
        '''

        decision = Decision()

        pub = rospy.Publisher('/vision_face_tracking/face_coord', FaceCoordinates, queue_size=1)
        face_coords_msg = FaceCoordinates(x=1.5, y=0, h=200, w=200)
        start = time.time()
        while time.time() - start < 1:
            try:
                pub.publish(face_coords_msg)
            except Exception as e:
                break
            face_coords_dict = decision.face_info
            if len(face_coords_dict.keys()) > 0:
                break
            time.sleep(0.1)
        face_coords_dict = decision.face_info
        self.assertEqual(face_coords_dict, dict())

        decision._delete_subscribers()
        pub.unregister()

    def test_wrong_type_data_publish(self):
        '''
        test wrong type data publishing - try publish message with one type
        in topic with other type
        '''

        decision = Decision()
        pub = rospy.Publisher('/vision_face_tracking/face_coord', SmileDetected, queue_size=1)
        smile_detected = SmileDetected(detected=True)
        pub.publish(smile_detected)
        start = time.time()
        while time.time() - start < 1:
            pub.publish(smile_detected)
            smile = decision.smile_exists
            time.sleep(0.1)
        self.assertEqual(decision.face_coords, dict())

        decision._delete_subscribers()
        pub.unregister()



class TestCallbackSmileDetected(unittest.TestCase):
    '''
    Test for callback_smile function in core_decision_manager node
    '''

    def test_valid_data_publish(self):
        '''
        test valid data publishing
        '''

        decision = Decision()
        pub = rospy.Publisher('/vision_face_tracking/smile_detected', SmileDetected, queue_size=1)
        smile_detected = SmileDetected(detected=True)
        start = time.time()
        while time.time() - start < 0.5:
            pub.publish(smile_detected)
            time.sleep(0.1)

        smile = decision.smile_exists
        self.assertEqual(smile, True)

        decision._delete_subscribers()
        pub.unregister()

    def test_invalid_data_publish(self):
        '''
        test invalid data publish - wrong typo of one of message fields
        '''

        decision = Decision()

        pub = rospy.Publisher('/vision_face_tracking/smile_detected', SmileDetected, queue_size=1)
        smile_detected = SmileDetected(detected='true')
        start = time.time()
        while time.time() - start < 1:
            try:
                pub.publish(smile_detected)
            except Exception as e:
                break
            time.sleep(0.1)
        smile = decision.smile_exists
        self.assertEqual(smile, False)

        decision._delete_subscribers()
        pub.unregister()

    def test_invalid_data_publish2(self):
        '''
        test invalid data publish - wrong typo of one of message fields
        '''

        decision = Decision()

        pub = rospy.Publisher('/vision_face_tracking/smile_detected', SmileDetected, queue_size=1)
        smile_detected = SmileDetected(detected=1)
        start = time.time()
        while time.time() - start < 1:
            try:
                pub.publish(smile_detected)
            except Exception as e:
                break
            time.sleep(0.1)
        smile = decision.smile_exists
        self.assertEqual(smile, True)

        decision._delete_subscribers()
        pub.unregister()

    def test_wrong_type_data_publish(self):
        '''
        test wrong type data publishing - try publish message with one type
        in topic with other type
        '''

        decision = Decision()
        pub = rospy.Publisher('/vision_face_tracking/smile_detected', FaceCoordinates, queue_size=1)
        face_coords = FaceCoordinates()
        pub.publish(face_coords)
        start = time.time()
        while time.time() - start < 1:
            pub.publish(face_coords)
            face_coords_dict = decision.face_coords
            if len(face_coords_dict.keys()) > 0:
                break
            time.sleep(0.1)
        self.assertEqual(decision.smile_exists, False)

        decision._delete_subscribers()
        pub.unregister()



class TestCallbackBotDialog(unittest.TestCase):
    '''
    Test for callback_bot_dialog function in core_decision_manager node
    '''

    def test_valid_data_publish(self):
        '''
        test valid data publishing
        '''

        decision = Decision()
        pub = rospy.Publisher('/dialog_bot_manager/bot_dialog', APIAIBotAnswer, queue_size=1)
        bot_answer = APIAIBotAnswer(text='hello', action_name='action', action_parameters_in_json=json.dumps({'p1': 1, 'p2': 2}))
        start = time.time()
        while time.time() - start < 1:
            pub.publish(bot_answer)
            time.sleep(0.1)

        self.assertEqual(decision.bot_text_answer, 'hello')
        self.assertEqual(decision.bot_action_answer, 'action')
        self.assertEqual(decision.bot_action_parameter_answer, {'p1': 1, 'p2': 2})

        decision._delete_subscribers()
        pub.unregister()

    def test_invalid_data_publish(self):
        '''
        test invalid data publish - wrong typo of one of message fields
        '''

        decision = Decision()

        pub = rospy.Publisher('/dialog_bot_manager/bot_dialog', APIAIBotAnswer, queue_size=1)
        bot_answer = APIAIBotAnswer(text=1, action_name='action', action_parameters_in_json="{'p1': 1, 'p2': 2}")

        start = time.time()
        while time.time() - start < 1:
            try:
                pub.publish(bot_answer)
            except Exception as e:
                break
            time.sleep(0.1)

        self.assertEqual(decision.bot_text_answer, str())
        self.assertEqual(decision.bot_action_answer, str())
        self.assertEqual(decision.bot_action_parameter_answer, dict())

        decision._delete_subscribers()
        pub.unregister()

    def test_wrong_type_data_publish(self):
        '''
        test wrong type data publishing - try publish message with one type
        in topic with other type
        '''

        decision = Decision()
        pub = rospy.Publisher('/dialog_bot_manager/bot_dialog', FaceCoordinates, queue_size=1)
        face_coords = FaceCoordinates()
        pub.publish(face_coords)
        start = time.time()
        while time.time() - start < 1:
            pub.publish(face_coords)
            face_coords_dict = decision.face_coords
            if len(face_coords_dict.keys()) > 0:
                break
            time.sleep(0.1)

        self.assertEqual(decision.bot_text_answer, str())
        self.assertEqual(decision.bot_action_answer, str())
        self.assertEqual(decision.bot_action_parameter_answer, dict())

        decision._delete_subscribers()
        pub.unregister()

class TestBehaviorCoreDecisionManager(unittest.TestCase):

    def test_publish_smile_exists(self):
        pass

    def test_publish_bot_answer(self):
        pass

    
if __name__ == '__main__':
    rospy.init_node('test_core_decision_manager')
    unittest.main()
