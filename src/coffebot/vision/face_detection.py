#!/usr/bin/env python3

from coffebot.vision.utils import opencv
from typing import Dict

import numpy


class FaceTracker:


    def find_closest_face_region(self, image: numpy.ndarray or None = None, min_neighbors: int=5) -> Dict[str, int] or None:
        '''Detects faces and searches closest
        Args:
            img: numpy.ndarray
        Returns:
            Dict[str,int]: coordinates and sizes of closest face
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

        if face_image is None:
            return None

        return opencv.detect_smile(face_image)
