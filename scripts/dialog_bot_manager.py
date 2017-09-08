#!/usr/bin/env python3

'''
conversation with bot
'''

import rospy
from pathlib import Path
TOP = Path(__file__).resolve().parents[1].as_posix()

from std_msgs.msg import String
from candybot_v2.msg import UserSpeechText, APIAIBotAnswer, BotSpeechText
from core.dialog_manager import DialogManager
import json
#from apiai_service.bot_client import APIAIBot
from utils.topic_controller import Lock
import time

BOT_NAME = "арнольд"


if __name__ == '__main__':

    rospy.init_node('dialog_bot_manager')

    if rospy.has_param('bot_client_key'):
        #bot = APIAIBot(client_key=rospy.get_param('bot_client_key'))
        scheme_file_path = None
        if rospy.has_param('scheme_file'):
            scheme_filename = rospy.get_param('scheme_file')
            if isinstance(scheme_filename, str) and len(scheme_filename) > 0:
                scheme_file_path = TOP + '/run/' + rospy.get_param('scheme_file')
        print('scheme_file:', scheme_file_path)
        d_manager = DialogManager(scheme_file=scheme_file_path, \
                                  apiai_bot_client_key=rospy.get_param('bot_client_key'))

        #bot_decision_publisher = rospy.Publisher('/dialog_bot_manager/bot_dialog', APIAIBotAnswer, queue_size=1)

        speech_synthesis_publisher = rospy.Publisher('/core_decision_manager/bot_speech_text', BotSpeechText, queue_size=1)
        action_publisher = rospy.Publisher('/action_manager/action_name', String, queue_size=1)

        lock_bot_request = Lock()
        rospy.Subscriber('/speech_recognition/user_speech_text', UserSpeechText, lock_bot_request.callback)
        print('dialog bot manager start')

        while True:
            try:
                rospy.get_master().getPid()
            except:
                break

            speech_text = str()
            pause_duration = 0

            user_speech_text_msg = lock_bot_request.message
            print('user text in bot: ', user_speech_text_msg)
            if isinstance(user_speech_text_msg, UserSpeechText) and user_speech_text_msg.text.strip().lower().startswith(BOT_NAME):
                speech_text = user_speech_text_msg.text.split(BOT_NAME)[1]
                if rospy.has_param('start_listen_to_speech'):
                    pause_duration = time.time() - rospy.get_param('start_listen_to_speech')
                    rospy.delete_param('start_listen_to_speech')

            print('speech_text: ', speech_text)

            d_manager.make_next_intent(speech_text=speech_text, pause_duration=pause_duration)
            print('bot text:', d_manager.say_to_user)
            print('bot action:', d_manager.action_name)
            if len(d_manager.say_to_user):
                speech_synthesis_publisher.publish(BotSpeechText(text=d_manager.say_to_user))
            action_publisher.publish(d_manager.action_name)

                # bot_answer = bot.request(user_speech_text_msg.text)
                # print('bot_answer:', bot_answer)
                # if isinstance(bot_answer, dict):
                #     bot_answer_msg = APIAIBotAnswer()
                #     bot_answer_msg.text = bot_answer['text']
                #     bot_answer_msg.action_name = bot_answer['action']['name']
                #     bot_answer_msg.action_parameters_in_json = json.dumps(bot_answer['action']['parameters'])
                #
                #     bot_decision_publisher.publish(bot_answer_msg)

            if lock_bot_request.message == user_speech_text_msg:
                lock_bot_request.message = None
            time.sleep(0.5)
