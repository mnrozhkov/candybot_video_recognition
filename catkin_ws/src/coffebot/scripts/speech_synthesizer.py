#!/usr/bin/env python3

'''
speech sythesis node
'''

import rospy
import std_msgs

from coffebot.audio.synthesizer import Talker
from coffebot.audio.utils import audio_format_converter

from coffebot.topic_controller import Lock
import time

if __name__ == '__main__':

    rospy.init_node('speech_synthesizer')

    if rospy.has_param('yandex_voice_key') is True:
        talker = Talker(yandex_voice_key=rospy.get_param('yandex_voice_key'))

        synthesized_speech_publisher = rospy.Publisher('speech_audio', std_msgs.msg.String, queue_size=1)
        lock_synthesize = Lock(msg_type=std_msgs.msg.String)
        rospy.Subscriber('bot_speech_text', std_msgs.msg.String, lock_synthesize.callback)
        print('speech synthesis start')

        while True:
            msg = lock_synthesize.message
            print(msg)
            wav_bytes = talker.text_to_speech(msg)
            if wav_bytes is not None:
                str_wav_data = audio_format_converter.audio2str(wav_bytes)
                if str_wav_data is not None:
                    synthesized_speech_publisher.publish(str_wav_data)

            lock_synthesize.message = None
            time.sleep(0.5)
