#!/usr/bin/env python3

'''
speech recognition node
'''

import rospy
from candybot_v2.msg import Audio, UserSpeechText

from audio.recognizer import SpeechRecognizer
from audio.utils import audio_format_converter, read_pyaudio_config, log_recognized_text

from utils.topic_controller import Lock

import time

from pathlib import Path
recognized_text_folder = Path(__file__).resolve().parents[1].as_posix() + '/recognized_text'
import os
if os.path.exists(recognized_text_folder) is False:
    os.mkdir(recognized_text_folder)

if __name__ == '__main__':

    rospy.init_node('speech_recognition')

    if rospy.has_param('yandex_voice_key') is True:
        sr = SpeechRecognizer(yandex_voice_key=rospy.get_param('yandex_voice_key'))

        recognized_text_publisher = rospy.Publisher('/speech_recognition/user_speech_text', UserSpeechText, queue_size=1)
        lock_recognize = Lock()
        rospy.Subscriber('/audio_capture/audio', Audio, lock_recognize.callback)
        print('speech recognition start')

        while True:
            try:
                rospy.get_master().getPid()
            except:
                break

            recognize_text_msg = lock_recognize.message

            if isinstance(recognize_text_msg, Audio):
                wav_data = audio_format_converter.raw_audio2wav(recognize_text_msg.content, read_pyaudio_config())
                recognized_text = sr.recognize_speech(wav_data)
                print(recognized_text)
                log_recognized_text(recognized_text, recognized_text_folder)
                if recognized_text is not None:
                    user_speech_text_msg = UserSpeechText(text = recognized_text)
                    recognized_text_publisher.publish(user_speech_text_msg)

            if lock_recognize.message == recognize_text_msg:
                lock_recognize.message = None
            time.sleep(0.5)
