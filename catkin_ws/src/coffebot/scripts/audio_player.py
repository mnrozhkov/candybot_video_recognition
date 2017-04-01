#!/usr/bin/env python3

'''
play audio node
'''

import rospy
import std_msgs

from coffebot.audio.player import Player
from coffebot.audio.utils import audio_format_converter
import io

from coffebot.topic_controller import Lock

import time


if __name__ == '__main__':

    rospy.init_node('audio_player')

    player = Player()

    lock_speech = Lock(msg_type=std_msgs.msg.String)
    rospy.Subscriber('speech_audio', std_msgs.msg.String, lock_speech.callback)
    print('play audio start')

    def callback_audio(data):
        pass

    rospy.Subscriber('play_audio', std_msgs.msg.String, callback_audio)

    while True:
        wav_bytes = audio_format_converter.str2audio(lock_speech.message)
        wav_source = io.BytesIO(wav_bytes)
        wav_source.seek(0)
        player.play_audio(wav_source)
        lock_speech.message = None

        time.sleep(0.5)
