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
from coffebot.msg import MakeVideo, Audio
import ros_numpy
from sensor_msgs.msg import Image

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
    lock_start_video_record = Lock()
    rospy.Subscriber('record_video', MakeVideo, lock_start_video_record.callback)
    print('vision video capture start')

    while True:
        '''REWRITE
        lock.message contains string represantation of dictionary with structure:
        record_video_dictionary = {
            'start_video': True,
            'duration': seconds,
            'video_file_name': absolute or relative path with video file name
        }
        '''

        try:
            rospy.get_master().getPid()
        except:
            break

        make_video_msg = lock_start_video_record.message

        if make_video_msg is not None:

            if make_video_msg.start_video is True:
                frames = list()
                audio_buffer_list = list()

                def callback_get_image(data: Image) -> None:
                    '''
                    1. takes message from image topic
                    2. converts it to numpy.ndarray frame
                    3. appends the frame to frames list
                    '''

                    frame = ros_numpy.numpify(data)
                    frames.append(frame)

                def callback_get_audio(data: Audio) -> None:
                    '''
                    1. takes audio from audio topic
                    2. converts it to bytes
                    3. adds it to audio buffer
                    '''

                    audio_subbufer = data.content
                    audio_buffer_list.append(audio_subbufer)


                image_sub = rospy.Subscriber('image', Image, callback_get_image)
                audio_sub = rospy.Subscriber('audio', Audio, callback_get_audio)

                start = time.time()

                #recieve video frames and audio parts during duration time
                while time.time() - start < make_video_msg.duration:
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
                    video_capture.merge_audio_video(tmp_wav_file_name, tmp_avi_file_name, make_video_msg.video_file_name)
                    os.remove(tmp_wav_file_name)
                    os.remove(tmp_avi_file_name)

        if lock_start_video_record.message == make_video_msg:
            lock_start_video_record.message = None
        time.sleep(0.5)
