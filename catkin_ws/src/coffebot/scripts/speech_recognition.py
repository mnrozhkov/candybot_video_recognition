#!/usr/bin/env python3

'''
speech recognition node
'''

import rospy
import std_msgs

from coffebot.audio.recognizer import SpeechRecognizer
from coffebot.audio.utils import audio_format_converter

from coffebot.topic_controller import Lock

import time


if __name__ == '__main__':

    rospy.init_node('speech_recognition')

    if rospy.has_param('yandex_voice_key') is True:
        sr = SpeechRecognizer(yandex_voice_key=rospy.get_param('yandex_voice_key'))

        recognized_text_publisher = rospy.Publisher('user_speech_text', std_msgs.msg.String, queue_size=1)
        lock_recognize = Lock()
        rospy.Subscriber('audio', std_msgs.msg.String, lock_recognize.callback)
        print('speech recognition start')

        while True:
            msg = lock_recognize.message
            
            if msg is not None:
                raw_audio = audio_format_converter.str2audio(msg)
                wav_data = audio_format_converter.raw_audio2wav(raw_audio, rospy.get_param('pyaudio'))
                recognized_text = sr.recognize_speech(wav_data)
                print(recognized_text)
                if recognized_text is not None:
                    recognized_text_publisher.publish(recognized_text)

            lock_recognize.message = None
            time.sleep(0.5)
