#!/usr/bin/env python3
import sys
sys.path.insert(1,'/usr/local/lib/python3.5/dist-packages')

import cv2
import numpy
from typing import List
import ffmpy

import time

import logging
import os
LOG_FOLDER = 'logs'
if os.path.exists(LOG_FOLDER) is False:
    os.mkdir(LOG_FOLDER)

logging.basicConfig(filename=LOG_FOLDER + '/' + __name__ + '.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.DEBUG)


def create_video(frames: List[numpy.ndarray], video_name_with_extension: str) -> str or None:
    '''
    1. Take frames list and video file name;
    2. Save frames in avi file

    Args:
        frames: list of video frames
        video_name_with_extension: video file name with extension to specifying video format
    Returns:
        video file name : if file saved successfully
        None: if failed
    '''

    try:
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(video_name_with_extension, fourcc, 8.0, (640,480))

        for frame in frames:
            out.write(frame)
        out.release()
        return video_name_with_extension
    except Exception as e:
        logging.error(str(e))
        return None


def merge_audio_video(wav_file_name: str, avi_file_name: str, audio_video_file_name: str) -> str or None:
    '''
    1. takes names of .wav and .avi file
    2. merges them into one file using FFmpeg library (https://pypi.python.org/pypi/ffmpy)

    Args:
        wav_file_name: wave file name
        avi_file_name: avi file name
        audio_video_file_name: merged audio/video filename
    Returns:
        merged audio/video filename : if saved successfully
        None : if failed
    '''

    try:
        ffmpy.FFmpeg(inputs={wav_file_name: None, avi_file_name: None}, outputs={audio_video_file_name: None}).run()
        return audio_video_file_name
    except Exception as e:
        logging.error(str(e))
        return None
