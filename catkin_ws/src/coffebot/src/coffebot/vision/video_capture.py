#!/usr/bin/env python3
import sys
sys.path.insert(1,'/usr/local/lib/python3.5/dist-packages')

import cv2
import numpy
from typing import List
import ffmpy

import time

def create_video(frames: List[numpy.ndarray], video_name_with_extension: str) -> str:
    '''
    1. takes frames list and video file name
    2. saves frames in avi file
    '''
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(video_name_with_extension, fourcc, 8.0, (640,480))

    for frame in frames:
        out.write(frame)
    out.release()
    return video_name_with_extension


def merge_audio_video(wav_file_name: str, avi_file_name: str, audio_video_file_name: str) -> str:
    '''
    1. takes names of .wav and .avi file
    2. merges them into one file
    '''

    ffmpy.FFmpeg(inputs={wav_file_name: None, avi_file_name: None}, outputs={audio_video_file_name: None}).run()
    return audio_video_file_name
