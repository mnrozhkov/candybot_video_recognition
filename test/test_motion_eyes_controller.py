#!/usr/bin/env python3
'''
motion_eyes_controller behavior test
'''

import rospy
import rosgraph

from coffebot.msg import EyesMotion, EyesState
import unittest

import time

import math

REACTION_TIMEOUT = 1 #in seconds

WIDHT = 128
HEIGHT = 128

CENTER_X = WIDHT // 2
CENTER_Y = HEIGHT // 2

EYES_RADIUS = 64
PUPIL_RADIUS = 25
PUPIL_ORBIT_RADIUS = EYES_RADIUS - PUPIL_RADIUS

class TestBehaviorMotionEyesController(unittest.TestCase):

    def test_reaction(self):
        global REACTION_TIMEOUT
        global WIDHT
        global HEIGHT

        global CENTER_X
        global CENTER_Y

        global EYES_RADIUS = 64
        global PUPIL_RADIUS = 25
        global PUPIL_ORBIT_RADIUS = EYES_RADIUS - PUPIL_RADIUS

        ros_is_running = True
        motion_eyes_controller_is_runnig = True

        master = rosgraph.Master('/motion_eyes_controller')

        try:
            master.lookupNode('/motion_eyes_controller')
        except ConnectionRefusedError:
            ros_is_running = False
        except rosgraph.masterapi.MasterError:
            motion_eyes_controller_is_runnig = False

        self.assertEqual(ros_is_running, True)
        self.assertEqual(motion_eyes_controller_is_runnig, True)

        eyes_motion_publisher = rospy.Publisher('/motion_eyes_controller/eyes_motion', EyesMotion, queue_size=1)
        eyes_motion_msg = EyesMotion(angle=45.0, distance_from_center_percent = 0.8,  emotion='happy')

        self.x = None
        self.y = None
        self.emotion = None

        self.data_recieved = False

        def callback(data: EyesState):
            self.x = data.x
            self.y = data.y
            self.emotion = data.state.emotion
            self.data_recieved = True

        eyes_state_sub = rospy.Subscriber('/motion_eyes_controller/eyes_state', EyesState, callback)

        start = time.time()

        while time.time() - start < REACTION_TIMEOUT and data_recieved is False:
            eyes_motion_publisher.publish(eyes_motion_msg)
            time.sleep(0.1)

        self.assertEqual(self.x, math.ceil(PUPIL_ORBIT_RADIUS * eyes_motion_msg.distance_from_center_percent * math.cos(eyes_motion_msg.angle)) + CENTER_X)
        self.assertEqual(self.x, math.ceil(PUPIL_ORBIT_RADIUS * eyes_motion_msg.distance_from_center_percent * math.sin(eyes_motion_msg.angle)) + CENTER_Y)
        self.assertEqual(self.emotion, eyes_motion_msg.emotion)

        eyes_motion_publisher.unregister()
        eyes_state_sub.unregister()

        del(self.x, self.y, self.emotion, self.data_recieved)


if __name__ == '__main__':

    rospy.init_node('test_motion_eyes_controller')
    unittest.main()
