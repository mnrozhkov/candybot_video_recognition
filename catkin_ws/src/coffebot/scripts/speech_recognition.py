#!/usr/bin/env python3

'''
speech recognition node
'''

import rospy
import std_msgs
from coffebot.msg import Audio, UserSpeechText

from coffebot.audio.recognizer import SpeechRecognizer
from coffebot.audio.utils import audio_format_converter

from coffebot.topic_controller import Lock

import time


if __name__ == '__main__':

    rospy.init_node('speech_recognition')

    if rospy.has_param('yandex_voice_key') is True:
        sr = SpeechRecognizer(yandex_voice_key=rospy.get_param('yandex_voice_key'))

        recognized_text_publisher = rospy.Publisher('user_speech_text', UserSpeechText, queue_size=1)
        lock_recognize = Lock()
        rospy.Subscriber('audio', Audio, lock_recognize.callback)
        print('speech recognition start')

        while True:
            try:
                rospy.get_master().getPid()
            except:
                break

            msg = lock_recognize.message

            if msg is not None:
                wav_data = audio_format_converter.raw_audio2wav(msg.content, rospy.get_param('pyaudio'))
                recognized_text = sr.recognize_speech(wav_data)
                print(recognized_text)
                if recognized_text is not None:
                    user_speech_text_msg = UserSpeechText()
                    user_speech_text_msg.text = recognized_text
                    recognized_text_publisher.publish(user_speech_text_msg)

            if lock_recognize.message == msg:
                lock_recognize.message = None
            time.sleep(0.5)
