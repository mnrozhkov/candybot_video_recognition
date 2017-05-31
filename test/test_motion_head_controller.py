#!/usr/bin/env python3
'''
motion_head_controller behavior test
'''

import rospy
import rosgraph

from candybot_v2.msg import HeadMotion, HeadState
import unittest

import time

REACTION_TIMEOUT = 1 #in seconds


class TestBehaviorMotionHeadController(unittest.TestCase):

    def test_reaction(self):
        global REACTION_TIMEOUT

        ros_is_running = True
        motion_head_controller_is_runnig = True

        master = rosgraph.Master('/motion_head_controller')

        try:
            master.lookupNode('/motion_head_controller')
        except ConnectionRefusedError:
            ros_is_running = False
        except rosgraph.masterapi.MasterError:
            motion_head_controller_is_runnig = False

        self.assertEqual(ros_is_running, True)
        self.assertEqual(motion_head_controller_is_runnig, True)

        head_motion_publisher = rospy.Publisher('/motion_head_controller/head_motion', HeadMotion, queue_size=1)
        head_motion_msg = HeadMotion(h_angle=45.0, v_angle=45.0, emotion='happy')

        self.h_angle = None
        self.v_angle = None
        self.emotion = None

        self.data_recieved = False

        def callback(data: HeadState):
            self.h_angle = data.state.h_angle
            self.v_angle = data.state.v_angle
            self.emotion = data.state.emotion
            self.data_recieved = True

        head_state_sub = rospy.Subscriber('/motion_head_controller/head_state', HeadState, callback)

        start = time.time()

        while time.time() - start < REACTION_TIMEOUT and self.data_recieved is False:
            head_motion_publisher.publish(head_motion_msg)
            time.sleep(0.1)

        self.assertEqual(self.h_angle, head_motion_msg.h_angle)
        self.assertEqual(self.v_angle, head_motion_msg.v_angle)
        self.assertEqual(self.emotion, head_motion_msg.emotion)

        head_motion_publisher.unregister()
        head_state_sub.unregister()

        del(self.h_angle, self.v_angle, self.emotion, self.data_recieved)

if __name__ == '__main__':

    rospy.init_node('test_motion_head_controller')
    unittest.main()
