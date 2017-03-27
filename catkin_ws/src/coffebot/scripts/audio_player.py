#!/usr/bin/env python3

'''
play audio node
'''

import pospy
import std_msgs

from coffebot.audio.player import Player
from coffebot.audio.utils import audio_format_converter
import io


if __name__ == '__main__':

    rospy.init_node('audio_player')

    player = Player()


    def callback_audio(data):
        pass


    def callback_speech(data: std_msgs.msg.String) -> None:
        wav_bytes = audio_format_converter.str2audio(data.data)
        wav_source = io.BytesIO(wav_bytes)
        wav_source.seek(0)
        player.play_audio(wav_source)


    rospy.Subscriber('play_audio', std_msgs.msg.String, callback_audio)
    rospy.Subscriber('speech_audio', std_msgs.msg.String, callback_speech)

    rospy.spin()
