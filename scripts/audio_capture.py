#!/usr/bin/env python3
'''
    1. capture sound
    2. convert it to string
    3. publish string
'''

import sys

import rospy
import base64
import logging
import time

from audio.recorder import Recorder
from candybot_v2.msg import Audio

import os
LOG_FOLDER = 'logs'
if os.path.exists(LOG_FOLDER) is False:
    os.mkdir(LOG_FOLDER)

logging.basicConfig(filename=LOG_FOLDER + '/' + __name__ + '.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.DEBUG)


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
    rospy.init_node('audio_capture')

    publisher = rospy.Publisher('/audio_capture/audio', Audio, queue_size=1)

    print('start listen')
    while True:
        try:
            rospy.get_master().getPid()
        except:
            break
        #if sound detected record raw data until silence
        if rospy.has_param('min_rms'):
            min_rms = rospy.get_param('min_rms')
            audio_recorder.set_min_rms(min_rms)
        raw_audio = audio_recorder.listen_audio()
        if isinstance(raw_audio, bytes):
            msg = Audio(content=raw_audio)
            publisher.publish(msg)

        time.sleep(0.1)
