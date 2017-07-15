#!/usr/bin/env python3
'''
1. listen command to generate_hashtag
2. scan newsfeed (vk) for posts with the hashtag
'''

import rospy
from social.svk import VkNeewsfeedScanner
from std_msgs.msg import Bool, String
import time

if __name__ == '__main__':
    rospy.init_node('social_vk')
    print('social_vk started!')

    if rospy.has_param('vk_api_access_key') and rospy.has_param('vk_group_access_token') and rospy.has_param('vk_group_id'):
        newsfeed_scanner = VkNeewsfeedScanner(access_token=rospy.get_param('vk_api_access_key'), group_access_token=rospy.get_param('vk_group_access_token'), group_id=rospy.get_param('vk_group_id'), required_hashtag='#funrobots')

        hashtag_publisher = rospy.Publisher('/social/vk/newsfeed_scanner/hashtag', String, queue_size=1)
        give_candy_publisher = rospy.Publisher('/social/vk/newsfeed_scanner/give_candy', Bool, queue_size=1)

        def callback_scan_command(data: Bool):
            if data.data is True:
                hashtag = newsfeed_scanner.generate_hashtag()
                print('vk: hashtag: ', hashtag)
                rospy.set_param('vk_hashtag', hashtag)
                hashtag_publisher.publish(hashtag)
                hashtag_posted_in_vk = newsfeed_scanner.listen(hashtag, 120)
                if hashtag_posted_in_vk is True:
                    print('vk give candy')
                    give_candy_publisher.publish(True)
                #rospy.set_param('social_vk_generate_hashtag', False)
                #rospy.set_param('social_action_time_vk', time.time())

        #rospy.Subscriber('/social/vk/newsfeed_scanner/scan_command', Bool, callback_scan_command)

        #rospy.set_param('social_vk_loaded', True)
        while True:
            try:
                rospy.get_master().getPid()
            except:
                break

            # if rospy.get_param('social_vk_generate_hashtag') is True:
            #     callback_scan_command(Bool(data=True))
            callback_scan_command(Bool(data=True))
            time.sleep(0.1)
