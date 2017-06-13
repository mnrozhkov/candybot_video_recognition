#!/usr/bin/env python3

'''
conversation with bot
'''

import rospy
from candybot_v2.msg import UserSpeechText, APIAIBotAnswer
import json

import aiml
import os

from pathlib import Path
top = Path(__file__).resolve().parents[0].as_posix()

from utils.topic_controller import Lock

import time

import logging
LOG_FOLDER = 'logs'
if os.path.exists(LOG_FOLDER) is False:
    os.mkdir(LOG_FOLDER)

logging.basicConfig(filename=LOG_FOLDER + '/' + __name__ + '.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.DEBUG)


if __name__ == '__main__':

    rospy.init_node('dialog_bot_aimlmanager')

    
    bot = aiml.Kernel()
    aiml_files = os.listdir(top + '/aiml')
    for a_file in aiml_files:
        if a_file[-4:] == 'aiml':
            bot.learn(top + '/aiml/' + a_file)

    bot_decision_publisher = rospy.Publisher('/dialog_bot_aimlmanager/bot_dialog', APIAIBotAnswer, queue_size=1)
    lock_bot_request = Lock()
    rospy.Subscriber('/speech_recognition/user_speech_text', UserSpeechText, lock_bot_request.callback)
    print('dialog bot aimlmanager start')

    while True:
        try:
            rospy.get_master().getPid()
        except:
            break

        user_speech_text_msg = lock_bot_request.message
        print('user text in bot: ', user_speech_text_msg)
        if isinstance(user_speech_text_msg, UserSpeechText):
            try:
                bot_respond = bot.respond(user_speech_text_msg.text)
                print('bot_respond: ', bot_respond)
                bot_answer = json.loads(bot_respond)
                if isinstance(bot_answer, dict):
                    bot_answer_msg = APIAIBotAnswer()
                    bot_answer_msg.text = bot_answer['text']
                    bot_answer_msg.action_name = bot_answer['action']['name']
                    bot_answer_msg.action_parameters_in_json = json.dumps(bot_answer['action']['parameters'])

                    bot_decision_publisher.publish(bot_answer_msg)
            except Exception as e:
            	print('dialog_bot_aimlmanager: error: ', str(e))
                logging.error(str(e))

        if lock_bot_request.message == user_speech_text_msg:
            lock_bot_request.message = None
        time.sleep(0.5)
