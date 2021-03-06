#!/usr/bin/env python3

'''
conversation with bot
'''

import rospy
from coffebot.msg import UserSpeechText, APIAIBotAnswer
import json

from coffebot.bot_client import APIAIBot

from coffebot.topic_controller import Lock

import time


if __name__ == '__main__':

    rospy.init_node('dialog_bot_manager')

    if rospy.has_param('bot_client_key'):
        bot = APIAIBot(client_key=rospy.get_param('bot_client_key'))

        bot_decision_publisher = rospy.Publisher('bot_dialog', APIAIBotAnswer, queue_size=1)
        lock_bot_request = Lock()
        rospy.Subscriber('user_speech_text', UserSpeechText, lock_bot_request.callback)
        print('dialog bot manager start')

        while True:
            try:
                rospy.get_master().getPid()
            except:
                break

            user_speech_text_msg = lock_bot_request.message
            print('user text in bot: ', user_speech_text_msg)
            if user_speech_text_msg is not None:
                bot_answer = bot.request(user_speech_text_msg.text)
                print('bot_answer:', bot_answer)
                if bot_answer is not None:
                    bot_answer_msg = APIAIBotAnswer()
                    bot_answer_msg.text = bot_answer['text']
                    bot_answer_msg.action_name = bot_answer['action']['name']
                    bot_answer_msg.action_parameters_in_json = json.dumps(bot_answer['action']['parameters'])

                    bot_decision_publisher.publish(bot_answer_msg)

            if lock_bot_request.message == user_speech_text_msg:
                lock_bot_request.message = None
            time.sleep(0.5)
