#!/usr/bin/env python3
'''
Initialize to generate hashtags and scan post with social net nodes every 5 minutes
'''

import rospy
from std_msgs.msg import Bool
import time

vk_action_init_pub = rospy.Publisher('/social/vk/newsfeed_scanner/scan_command', Bool, queue_size=1)
twitter_action_init_pub = rospy.Publisher('/social/twitter/code_scanner/scan_command', Bool, queue_size=1)

def callback_vk_give_candy(data: Bool):
    if data.data is True:
        vk_action_init_pub.publish(True)
        rospy.set_param('social_action_time_vk', time.time())

def callback_twitter_give_candy(data: Bool):
    if data.data is True:
        twitter_action_init_pub.publish(True)
        rospy.set_param('social_action_time_twitter', time.time())


if __name__ == '__main__':

    rospy.init_node('social_action_initializer')
    rospy.set_param('social_action_time_vk', time.time())
    rospy.set_param('social_action_time_twitter', time.time())

    vk_sub = rospy.Subscriber('/social/vk/newsfeed_scanner/give_candy', Bool, callback_vk_give_candy)
    twitter = rospy.Subscriber('/social/twitter/code_scanner/give_candy', Bool, callback_twitter_give_candy)


    while True:
        try:
            rospy.get_master().getPid()
        except Exception as e:
            break
        if time.time() - rospy.get_param('social_action_time_vk') > 300:
            vk_action_init_pub.publish(True)
            rospy.set_param('social_action_time_vk', time.time())

        if time.time() - rospy.get_param('social_action_time_twitter') > 300:
            twitter_action_init_pub.publish(True)
            rospy.set_param('social_action_time_twitter', time.time())

        time.sleep(0.1)
