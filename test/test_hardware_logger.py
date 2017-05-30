#!/usr/bin/env python3

import rospy
import unittest

import sys
from pathlib import Path
top = Path(__file__).resolve().parents[1].as_posix()
sys.path.append(top)

from scripts.hardware_logger import *


class TestLogBody(unittest.TestCase):

    def test_param_exists(self):
        rospy.set_param('/body/angle', 100)
        rospy.set_param('/body/emotion', 'happy')

        body_state = log_body()
        
        angle = body_state['angle']
        emotion = body_state['emotion']

        self.assertEqual(angle, 100)
        self.assertEqual(emotion, 'happy')

        rospy.delete_param('/body/angle')
        rospy.delete_param('/body/emotion')

    def test_param_does_not_exist(self):

        body_state = log_body()
        
        angle = body_state['angle']
        emotion = body_state['emotion']

        self.assertEqual(angle, None)
        self.assertEqual(emotion, None)



class TestLogEyebrows(unittest.TestCase):

    def test_param_exists(self):
        rospy.set_param('/eyebrows/l_angle', 100)
        rospy.set_param('/eyebrows/r_angle', 50)
        rospy.set_param('/eyebrows/emotion', 'happy')

        eyebrows_state = log_eyebrows()
        
        l_angle = eyebrows_state['l_angle']
        r_angle = eyebrows_state['r_angle']
        emotion = eyebrows_state['emotion']

        self.assertEqual(l_angle, 100)
        self.assertEqual(r_angle, 50)
        self.assertEqual(emotion, 'happy')

        rospy.delete_param('/eyebrows/l_angle')
        rospy.delete_param('/eyebrows/r_angle')
        rospy.delete_param('/eyebrows/emotion')

    def test_param_does_not_exist(self):

        eyebrows_state = log_eyebrows()
        
        l_angle = eyebrows_state['l_angle']
        v_angle = eyebrows_state['r_angle']
        emotion = eyebrows_state['emotion']

        self.assertEqual(l_angle, None)
        self.assertEqual(v_angle, None)
        self.assertEqual(emotion, None)


class TestLogEyes(unittest.TestCase):

    def test_param_exists(self):
        rospy.set_param('/eyes/x', 100)
        rospy.set_param('/eyes/y', 50)
        rospy.set_param('/eyes/emotion', 'happy')

        eyes_state = log_eyes()
        
        x = eyes_state['x']
        y = eyes_state['y']
        emotion = eyes_state['emotion']

        self.assertEqual(x, 100)
        self.assertEqual(y, 50)
        self.assertEqual(emotion, 'happy')

        rospy.delete_param('/eyes/x')
        rospy.delete_param('/eyes/y')
        rospy.delete_param('/eyes/emotion')

    def test_param_does_not_exist(self):

        eyes_state = log_eyes()
        
        x = eyes_state['x']
        y = eyes_state['y']
        emotion = eyes_state['emotion']

        self.assertEqual(x, None)
        self.assertEqual(y, None)
        self.assertEqual(emotion, None)


class TestLogHead(unittest.TestCase):

    def test_param_exists(self):
        rospy.set_param('/head/h_angle', 100)
        rospy.set_param('/head/v_angle', 50)
        rospy.set_param('/head/emotion', 'happy')

        head_state = log_head()
        
        h_angle = head_state['h_angle']
        v_angle = head_state['v_angle']
        emotion = head_state['emotion']

        self.assertEqual(h_angle, 100)
        self.assertEqual(v_angle, 50)
        self.assertEqual(emotion, 'happy')

        rospy.delete_param('/head/h_angle')
        rospy.delete_param('/head/v_angle')
        rospy.delete_param('/head/emotion')

    def test_param_does_not_exist(self):

        head_state = log_head()
        
        h_angle = head_state['h_angle']
        v_angle = head_state['v_angle']
        emotion = head_state['emotion']

        self.assertEqual(h_angle, None)
        self.assertEqual(v_angle, None)
        self.assertEqual(emotion, None)


if __name__ == '__main__':
    rospy.init_node('test_hardware_logger')
    unittest.main()
