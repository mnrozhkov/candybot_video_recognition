#!/usr/bin/env python3
import sys
from pathlib import Path
top = Path(__file__).resolve().parents[0].as_posix()
sys.path.append(top)

from .utils import opencv
from typing import Dict

import numpy


class FaceTracker:
    '''
    Simple face tracker class
    Functionality:
        1. search the closest face region on image
        2. search smile on some face region
    '''

    def find_closest_face_region(self, image: numpy.ndarray or None = None, min_neighbors: int=5) -> Dict[str, int] or None:
        '''Detects faces and searches closest
        Args:
            img: numpy.ndarray
        Returns:
            coordinates and sizes of closest face in format Dict[str,int] :
                if face found
            None : if face not found
        '''

        if image is None:
            return None

        faces = opencv.detect_faces(image)

        closest_face = {'x': 0, 'y': 0, 'w': 0, 'h': 0}
        max_face_square = 0
        if faces is not None and len(faces) > 0:
            print('faces!')
            for face in faces:
                current_square = face['w'] * face['h']
                if current_square > max_face_square:
                    closest_face = face
                    max_face_square = current_square

        return closest_face

    def detect_smile(self, face_image: numpy.ndarray or None = None) -> bool or None:
        '''
        Detect smile in face region
        Args:
            face_image: face region
        Returns:
            True : if smile detected
            False : if smile not detected
        '''

        if face_image is None:
            return None

        return opencv.detect_smile(face_image)
