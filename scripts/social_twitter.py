#!/usr/bin/env python3
'''
1. listen command to generate_code
2. scan twitter for posts with the code
'''

import rospy
from coffebot.social.twitter import TwitterCodeScanner
from std_msgs.msg import Bool, String
import time

if __name__ == '__main__':
    rospy.init_node('social_twitter')

    code_scanner = TwitterCodeScanner()

    code_publisher = rospy.Publisher('/social/twitter/code_scanner/code', String, queue_size=1)
    give_candy_publisher = rospy.Publisher('/social/twitter/code_scanner/give_candy', Bool, queue_size=1)

    def callback_scan_command(data: Bool):
        
        if data.data is True:
            code = code_scanner.generate_code()
            code_publisher.publish(code)
            code_posted_in_twitter = code_scanner.listenTwitter(code)
            if code_posted_in_twitter is True:
                give_candy_publisher.publish(True)

    rospy.Subscriber('/social/twitter/code_scanner/scan_command', Bool, callback_scan_command)

    while True:
        try:
            rospy.get_master().getPid()
        except:
            break

        time.sleep(0.1)
