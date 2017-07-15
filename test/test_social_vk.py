#!/usr/bin/env python3

import rospy
from std_msgs.msg import Bool
import unittest
import rosgraph
import time

TIMEOUT = 10


class TestVkPost(unittest.TestCase):

    def test(self):
        global TIMEOUT

        ros_is_running = True
        social_vk_is_running = True

        master = rosgraph.Master('/social_vk')

        try:
            master.lookupNode('/social_vk')
        except ConnectionRefusedError:
            ros_is_running = False
        except rosgraph.masterapi.MasterError:
            social_vk_is_running = False

        self.assertEqual(ros_is_running, True)
        self.assertEqual(social_vk_is_running, True)

        self.give_candy_command_recieved = False

        def callback_give_candy(data: Bool):
            if isinstance(data, Bool) and data.data == True:
                self.give_candy_command_recieved = True

        give_candy_sub = rospy.Subscriber('/social/vk/newsfeed_scanner/give_candy', Bool, callback_give_candy)

        session = vk.Session(access_token=rospy.get_param('vk_api_access_key'))
        api = vk.API(session)
        group_id = rospy.get_param('vk_group_id')
        group_access_token = get_param('vk_group_access_token')
        hashtag = rospy.get_param('vk_hashtag')

        api.wall.post(owner_id=-group_id, message='msg', access_token=group_access_token)

        start = time.time()
        while time.time() - start < TIMEOUT and self.give_candy_command_recieved is False:
            time.sleep(0.1)

        self.assertEqual(self.give_candy_command_recieved, True)

        give_candy_sub.unregister()
