#!/usr/bin/env python3

'''
speech sythesis node
'''

import rospy
from coffebot.msg import Audio, BotSpeechText

from coffebot.audio.synthesizer import Talker
from coffebot.audio.utils import audio_format_converter

from coffebot.topic_controller import Lock
import time


if __name__ == '__main__':

    rospy.init_node('speech_synthesizer')

    if rospy.has_param('yandex_voice_key') is True:
        talker = Talker(yandex_voice_key=rospy.get_param('yandex_voice_key'))

        synthesized_speech_publisher = rospy.Publisher('speech_audio', Audio, queue_size=1)
        lock_synthesize = Lock()
        rospy.Subscriber('bot_speech_text', BotSpeechText, lock_synthesize.callback)
        print('speech synthesis start')

        while True:
            try:
                rospy.get_master().getPid()
            except:
                break

            bot_speech_text_msg = lock_synthesize.message
            print('speech synthesis data:', bot_speech_text_msg)
            if bot_speech_text_msg is not None:
                wav_bytes = talker.text_to_speech(bot_speech_text_msg.text)
                if wav_bytes is not None:
                    message = Audio()
                    message.content = wav_bytes
                    synthesized_speech_publisher.publish(message)

            if lock_synthesize.message == bot_speech_text_msg:
                lock_synthesize.message = None
            time.sleep(0.5)
