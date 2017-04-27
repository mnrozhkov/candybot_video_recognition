#!/usr/bin/env python3
'''
motion_eyebrows_controller behavior test
'''

import rospy
import rosgraph

from coffebot.msg import EyebrowsMotion, EyebrowsState
import unittest

import time

REACTION_TIMEOUT = 1 #in seconds


class TestBehaviorMotionEyebrowsController(unittest.TestCase):

    def test_reaction(self):
        global REACTION_TIMEOUT

        ros_is_running = True
        motion_eyebrows_controller_is_runnig = True

        master = rosgraph.Master('/motion_eyebrows_controller')

        try:
            master.lookupNode('/motion_eyebrows_controller')
        except ConnectionRefusedError:
            ros_is_running = False
        except rosgraph.masterapi.MasterError:
            motion_eyes_controller_is_runnig = False

        self.assertEqual(ros_is_running, True)
        self.assertEqual(motion_eyebrows_controller_is_runnig, True)

        eyebrows_eyebrows_publisher = rospy.Publisher('/motion_eyebrows_controller/eyebrows_motion', EyebrowsMotion, queue_size=1)
        eyebrows_eyebrows_msg = EyebrowsMotion(l_angle=45.0, r_angle=45.0,  emotion='happy')

        self.l_angle = None
        self.r_angle = None
        self.emotion = None

        self.data_recieved = False

        def callback(data: EyebrowsState):
            self.l_angle = data.state.l_angle
            self.r_angle = data.state.r_angle
            self.emotion = data.state.emotion
            self.data_recieved = True

        eyebrows_state_sub = rospy.Subscriber('/motion_eyebrows_controller/eyebrows_state', EyebrowsState, callback)

        start = time.time()

        while time.time() - start < REACTION_TIMEOUT and data_recieved is False:
            eyebrows_motion_publisher.publish(eyebrows_motion_msg)
            time.sleep(0.1)

        self.assertEqual(self.l_angle, eyebrows_motion_msg.l_angle)
        self.assertEqual(self.r_angle, eyebrows_motion_msg.r_angle)
        self.assertEqual(self.emotion, eyebrows_motion_msg.emotion)

        eyebrows_motion_publisher.unregister()
        eyebrows_state_sub.unregister()

        del(self.l_angle, self.r_angle, self.emotion, self.data_recieved)


if __name__ == '__main__':

    rospy.init_node('test_motion_eyebrows_controller')
    unittest.main()
