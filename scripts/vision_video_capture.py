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
from coffebot.msg import Audio
import ros_numpy
from sensor_msgs.msg import Image

from coffebot.audio.utils import audio_format_converter
from coffebot.vision import video_capture

import os

import actionlib

from coffebot.msg import MakeVideoAction

import time


class MakeVideoServer:

    def __init__(self, topic_name):
        self.server = actionlib.SimpleActionServer(topic_name, MakeVideoAction, self.execute, False)
        self.server.start()

    def execute(self, goal):

        #read goal field : MakeVideo type
        make_video_msg = goal.make_video_command
        if make_video_msg.start_video is True and len(make_video_msg.video_file_name) > 0:
            frames = list() #list of video frames for video
            audio_buffer_list = list() #audio buffers list

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


            image_sub = rospy.Subscriber('/vision_camera_capture/image', Image, callback_get_image)
            audio_sub = rospy.Subscriber('/audio_capture/audio', Audio, callback_get_audio)

            start = time.time()

            #recieve video frames and audio parts during duration time
            while time.time() - start < make_video_msg.duration:
                pass

            #after time exceed release audio and image Subscribers to stop recieve data
            image_sub.unregister()
            audio_sub.unregister()

            audio_buffer = b''.join(audio_buffer_list)
            if len(audio_buffer) > 0:
                print('tmp files')
                #make temporary wave file
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

        self.server.set_succeeded()


if __name__ == '__main__':

    rospy.init_node('vision_video_capture')
    server = MakeVideoServer(topic_name='make_video')
    print('vision video capture start')

    while True:
        try:
            rospy.get_master().getPid()
        except:
            break

        time.sleep(0.5)
