#!/usr/bin/env python3

'''
conversation with bot
'''

import rospy
import std_msgs
import json

from coffebot.bot_client import APIAIBot

from coffebot.topic_controller import Lock

import time


if __name__ == '__main__':

    rospy.init_node('dialog_bot_manager')

    if rospy.has_param('bot_client_key'):
        bot = APIAIBot(client_key=rospy.get_param('bot_client_key'))

        bot_decision_publisher = rospy.Publisher('bot_dialog', std_msgs.msg.String, queue_size=1)
        lock_bot_request = Lock(msg_type=std_msgs.msg.String)
        rospy.Subscriber('user_speech_text', std_msgs.msg.String, lock_bot_request.callback)
        print('dialog bot manager start')

        while True:
            bot_answer = bot.request(lock_bot_request.message)
            if bot_answer is not None:
                bot_decision_publisher.publish(json.dumps(bot_answer))

            lock_bot_request.message = None
            time.sleep(0.5)
