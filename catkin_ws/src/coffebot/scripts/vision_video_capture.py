#!/usr/bin/env python3

'''
video capture and save node
1. take command to record video
2. take frames for video and audio parts for audio
3. make temporary audio and video files
4. merge audio and video file
5. delete temporary files
'''

import rospy
import std_msgs

from coffebot.vision.utils import image_format_converter
from coffebot.audio.utils import audio_format_converter
from coffebot.vision import video_capture
import json
import time

import os

from coffebot.topic_controller import Lock

import time


if __name__ == '__main__':

    rospy.init_node('vision_video_capture')
    lock_start_video_record = Lock(msg_type=std_msgs.msg.String)
    rospy.Subscriber('record_video', std_msgs.msg.String, lock_start_video_record.callback)
    print('vision video capture start')

    while True:
        '''
        lock.message contains string represantation of dictionary with structure:
        record_video_dictionary = {
            'start_video': True,
            'duration': seconds,
            'video_file_name': absolute or relative path with video file name
        }
        '''
        record_video_dictionary = json.loads(lock_start_video_record.message)

        if record_video_dictionary['start_video'] is True:
            frames = list()
            audio_buffer_list = list()

            def callback_get_image(data: std_msgs.msg.String) -> None:
                '''
                1. takes message from image topic
                2. converts it to numpy.ndarray frame
                3. appends the frame to frames list
                '''

                frame = image_format_converter.str2ndarray(data.data)
                frames.append(frame)

            def callback_get_audio(data: std_msgs.msg.String) -> None:
                '''
                1. takes audio from audio topic
                2. converts it to bytes
                3. adds it to audio buffer
                '''

                audio_subbufer = audio_format_converter.str2audio(data.data)
                audio_buffer_list.append(audio_subbufer)


            image_sub = rospy.Subscriber('image', std_msgs.msg.String, callback_get_image)
            audio_sub = rospy.Subscriber('audio', std_msgs.msg.String, callback_get_audio)

            start = time.time()

            #recieve video frames and audio parts during duration time
            while time.time() - start < record_video_dictionary['duration']:
                pass

            #after time exceed release audio and image Subscribers to stop recieve data
            image_sub.unregister()
            audio_sub.unregister()

            #make temporary wave file
            audio_buffer = b''.join(audio_buffer_list)
            if len(audio_buffer) > 0:
                print('tmp files')
                tmp_wav_file_name = 'tmp.wav'
                wav_binary_data = audio_format_converter.raw_audio2wav(audio_buffer, rospy.get_param('pyaudio'))
                wav_file = open(tmp_wav_file_name, 'wb')
                wav_file.write(wav_binary_data)

                #make temporary avi file
                tmp_avi_file_name = video_capture.create_video(frames, 'tmp.avi')

                #merge audio and video and delete temporary files
                video_capture.merge_audio_video(tmp_wav_file_name, tmp_avi_file_name, record_video_dictionary['video_file_name'])
                os.remove(tmp_wav_file_name)
                os.remove(tmp_avi_file_name)

        lock_start_video_record.message = None
        time.sleep(0.5)
