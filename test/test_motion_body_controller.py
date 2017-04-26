#!/usr/bin/env python3
'''
motion_body_controller behavior test
'''

import rospy
import rosgraph

from coffebot.msg import BodyMotion, BodyState
import unittest

import time

REACTION_TIMEOUT = 1 #in seconds


class TestBehaviorMotionBodyController(unittest.TestCase):

    def test_reaction(self):
        global REACTION_TIMEOUT

        ros_is_running = True
        motion_body_controller_is_runnig = True

        master = rosgraph.Master('/motion_body_controller')

        try:
            master.lookupNode('/motion_body_controller')
        except ConnectionRefusedError:
            ros_is_running = False
        except rosgraph.masterapi.MasterError:
            motion_body_controller_is_runnig = False

        self.assertEqual(ros_is_running, True)
        self.assertEqual(motion_body_controller_is_runnig, True)

        body_motion_publisher = rospy.Publisher('/motion_body_controller/body_motion', BodyMotion, queue_size=1)
        body_motion_msg = BodyMotion(angle=45.0, emotion='happy')

        self.angle = None
        self.emotion = None

        self.data_recieved = False

        def callback(data: BodyState):
            self.angle = data.state.angle
            self.emotion = data.state.emotion
            self.data_recieved = True

        body_state_sub = rospy.Subscriber('/motion_body_controller/body_state', BodyState, callback)

        start = time.time()

        while time.time() - start < REACTION_TIMEOUT and data_recieved is False:
            body_motion_publisher.publish(body_motion_msg)
            time.sleep(0.1)

        self.assertEqual(self.angle, body_motion_msg.angle)
        self.assertEqual(self.emotion, body_motion_msg.emotion)

        body_motion_publisher.unregister()
        body_state_sub.unregister()

        del(self.angle, self.emotion, self.data_recieved)

if __name__ == '__main__':

    rospy.init_node('test_motion_body_controller')
    unittest.main()
