#!/usr/bin/env python3

'''
conversation with bot
'''

import pospy
import std_msgs
import json

from coffebot.bot_client import APIAIBot


if __name__ == '__main__':

    rospy.init_node('dialog_bot_manager')

    if rospy.has_param('bot_client_key'):
        bot = APIAIBot(client_key=rospy.get_param('bot_client_key'))

        bot_decision_publisher = rospy.Publisher('bot_decision', std_msgs.msg.String, queue_size=1)

        def callback_bot_request(data: std_msgs.msg.String) -> None:
            bot_answer = bot.request(data.data)
            if bot_answer is not None:
                bot_decision_publisher.publish(json.dumps(bot_answer))


        rospy.Subscriber('user_speech_text')

        rospy.spin()
