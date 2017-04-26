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
    '''
    test reaction on different events
    '''

    def test_publish_smile_exists(self):
        '''
        test reaction on smile
        '''

        decision = Decision()
        smile_publisher = rospy.Publisher('/vision_face_tracking/smile_detected', SmileDetected, queue_size=1)

        self.user_speech_text = str()
        self.data_recieved = False

        def callback(data: UserSpeechText):
            self.user_speech_text = data.text
            self.data_recieved = True

        user_speech_text_sub = rospy.Subscriber('/speech_recognition/user_speech_text', UserSpeechText, callback)

        start = time.time()
        while time.time() - start < 1:
            smile_publisher.publish(True)
            decision.make_decision()
            time.sleep(0.1)

        start = time.time()
        while (time.time() - start < 1) and (self.data_recieved is False):
            time.sleep(0.1)

        try:
            self.assertEqual(self.user_speech_text, 'привет')
        except:
            raise
        finally:
            decision._delete_subscribers()
            decision._delete_publishers()

            smile_publisher.unregister()
            user_speech_text_sub.unregister()

        del(self.user_speech_text)
        del(self.data_recieved)

    def test_publish_bot_answer(self):
        '''
        reaction on bot answer
        '''

        decision = Decision()
        bot_answer_publisher = rospy.Publisher('/dialog_bot_manager/bot_dialog', APIAIBotAnswer, queue_size=1)

        bot_answer = APIAIBotAnswer(text='привет', action_name='action.hello', action_parameters_in_json=json.dumps(dict()))

        self.bot_speech_text = str()
        self.pattern_name = str()
        self.bot_speech_text_data_recieved = False
        self.pattern_name_recieved = False

        def callback_bot_speech_text(data: BotSpeechText):
            self.bot_speech_text = data.text
            self.bot_speech_text_data_recieved = True

        bot_speech_text_sub = rospy.Subscriber('/core_decision_manager/bot_speech_text', BotSpeechText, callback_bot_speech_text)

        def callback_pattern(data: MotionPattern):
            self.pattern_name = data.name
            self.pattern_name_recieved = True

        pattern_sub = rospy.Subscriber('/core_decision_manager/pattern', MotionPattern, callback_pattern)

        start = time.time()
        while time.time() - start < 1:
            bot_answer_publisher.publish(bot_answer)
            decision.make_decision()
            time.sleep(0.1)

        def all_data_recieved():
            return self.bot_speech_text_data_recieved and self.pattern_name_recieved

        start = time.time()

        while (time.time() - start < 1) and all_data_recieved() is False:
            time.sleep(0.1)

        try:
            self.assertEqual(self.bot_speech_text, 'привет')
            self.assertEqual(self.pattern_name, 'sayHello')
        except:
            raise
        finally:
            decision._delete_subscribers()
            decision._delete_publishers()

            bot_answer_publisher.unregister()
            bot_speech_text_sub.unregister()
            pattern_sub.unregister()

        del(self.bot_speech_text)
        del(self.pattern_name)
        del(self.bot_speech_text_data_recieved)
        del(self.pattern_name_recieved)


if __name__ == '__main__':
    rospy.init_node('test_core_decision_manager')
    unittest.main()
