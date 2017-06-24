#!/usr/bin/env python3
'''
Initialize to generate hashtags and scan post with social net nodes every 5 minutes
'''

import rospy
from std_msgs.msg import Bool
import time

if __name__ == '__main__':

    rospy.init_node('social_action_initializer')

    vk_action_init_pub = rospy.Publisher('/social/vk/newsfeed_scanner/scan_command', Bool, queue_size=1)
    twitter_action_init_pub = rospy.Publisher('/social/twitter/code_scanner/scan_command', Bool, queue_size=1)

    while True:
        try:
            rospy.get_master().getPid()
        except Exception as e:
            break

        vk_action_init_pub.publish(True)
        twitter_action_init_pub.publish(True)

        time.sleep(300)
