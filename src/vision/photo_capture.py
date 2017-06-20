#!/usr/bin/env python3
import sys
sys.path.insert(1,'/usr/local/lib/python3.5/dist-packages')

import cv2
import numpy

from utils import ErrorLogger

def save_photo(frame: numpy.ndarray, photo_name_with_extension: str) -> str or None:
    '''
    1. Take video frame
    2. Save it with specified name

    Args:
        frame: one video frame for photo
        photo_name_with_extension: photo file name with extension to specifying image format
    Returns:
        image file name : if saved successfully
        None: if fails
    '''
    try:
        cv2.imwrite(photo_name_with_extension, frame)
        return photo_name_with_extension
    except Exception as e:
        ErrorLogger(__file__, e)
        return None
