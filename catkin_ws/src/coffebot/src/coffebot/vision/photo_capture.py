#!/usr/bin/env python3
import sys
sys.path.insert(1,'/usr/local/lib/python3.5/dist-packages')

import cv2
import numpy


def save_photo(frame: numpy.ndarray, photo_name_with_extension: str) -> str:
    '''
    1. takes video frame
    2. saves it with specified name
    '''

    cv2.imwrite(photo_name_with_extension, frame)
    return photo_name_with_extension
