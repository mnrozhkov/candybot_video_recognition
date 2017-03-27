#!/usr/bin/env python3

'''
speech recognition node
'''

import pospy
import std_msgs

from coffebot.audio.recognizer import SpeechRecognizer
from coffebot.audio.utils import audio_format_converter


if __name__ == '__main__':

    rospy.init_node('speech_recognition')

    if rospy.has_param('yandex_voice_key') is True:
        sr = SpeechRecognizer(yandex_voice_key=rospy.get_param('yandex_voice_key'))

        recognized_text_publisher = rospy.Publisher('speech_text', std_msgs.msg.String, queue_size=1)

        def callback_recognize(data: std_msgs.msg.String) -> None:
            raw_audio = audio_format_converter.str2audio(data.data)
            wav_data = audio_format_converter.raw_audio2wav(raw_audio)
            recognized_text = sr.recognize_speech(wav_data)
            if recognized_text is not None:
                recognized_text_publisher.publish(recognized_text)


        rospy.Subscriber('audio', std_msgs.msg.String, callback_recognize)

        rospy.spin()
