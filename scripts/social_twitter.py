#!/usr/bin/env python3
'''
1. listen command to generate_code
2. scan twitter for posts with the code
'''

import rospy
from social.stwitter import TwitterCodeScanner
from std_msgs.msg import Bool, String
import time

if __name__ == '__main__':
    rospy.init_node('social_twitter')
    rospy.set_param('twitter_hashtag', '')
    print('social_twitter')

    code_scanner = TwitterCodeScanner()

    code_publisher = rospy.Publisher('/social/twitter/code_scanner/code', String, queue_size=1)
    give_candy_publisher = rospy.Publisher('/social/twitter/code_scanner/give_candy', Bool, queue_size=1)

    def callback_scan_command(data: Bool):

        if data.data is True:
            code = code_scanner.generate_code()
            print('twitter: track and code: ', code)
            rospy.set_param('twitter_hashtag', code)
            code_publisher.publish(code)
            code_posted_in_twitter = code_scanner.listenTwitter(code)
            if code_posted_in_twitter is True:
                print('twitter give candy')
                give_candy_publisher.publish(True)
            # rospy.set_param('social_twitter_generate_hashtag', False)
            # rospy.set_param('social_action_time_twitter', time.time())
            print(0)

    #rospy.Subscriber('/social/twitter/code_scanner/scan_command', Bool, callback_scan_command)

    rospy.set_param('social_twitter_loaded', True)
    while True:
        try:
            rospy.get_master().getPid()
        except:
            break

        # if rospy.get_param('social_twitter_generate_hashtag') is True:
        #     callback_scan_command(Bool(data=True))

        callback_scan_command(Bool(data=True))
        time.sleep(0.1)
