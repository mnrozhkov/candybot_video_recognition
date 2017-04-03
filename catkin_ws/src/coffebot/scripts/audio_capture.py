#!/usr/bin/env python3
'''
    1. capture sound
    2. convert it to string
    3. publish string
'''

import sys

import rospy
from std_msgs.msg import String
import base64
import logging
import time

from coffebot.audio.recorder import Recorder
from coffebot.audio.utils import audio_format_converter

logging.basicConfig(filename='listener.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.ERROR)


if __name__ == '__main__':

    #set listening parameter
    min_rms=500
    if rospy.has_param('pyaudio'):
        pyaudio_config = rospy.get_param('pyaudio')
    else:
        pyaudio_config = {
            'format': 8,
            'channels': 1,
            'rate': 16000,
            'frames_per_buffer': 1024
        },

    audio_recorder = Recorder(min_rms=min_rms, pyaudio_config=pyaudio_config)

    publisher = rospy.Publisher('audio', String, queue_size=1)
    rospy.init_node('audio_capture')

    print('start listen')
    while True:

        #if sound detected record raw data until silence
        if rospy.has_param('min_rms'):
            min_rms = rospy.get_param('min_rms')
            audio_recorder.set_min_rms(min_rms)
        raw_audio = audio_recorder.listen_audio()
        if raw_audio is not None:
            str_raw_audio = audio_format_converter.audio2str(raw_audio)
            publisher.publish(str_raw_audio)

        time.sleep(0.1)
