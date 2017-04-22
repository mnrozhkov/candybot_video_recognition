#!/usr/bin/env python3

import rospy
from coffebot.msg import Sound

from coffebot.audio.sound_manager import SoundManager
from coffebot.topic_controller import Lock

import time


if __name__ == '__main__':
    rospy.init_node('audio_sound_manager')
    snd_mgr = SoundManager()
    snd_lock = Lock()
    rospy.Subscriber('play_sound', Sound, snd_lock.callback)

    while True:
        try:
            rospy.get_master().getPid()
        except:
            pass

        sound_msg = snd_lock.message
        if isinstance(sound_msg, Sound):
            if len(sound_msg.category) > 0 and len(sound_msg.name) > 0:
                snd_mgr.play_sound(sound_msg.category, sound_msg.name)

        if snd_lock.message == sound_msg:
            snd_lock.message = None

        time.time(0.5)
