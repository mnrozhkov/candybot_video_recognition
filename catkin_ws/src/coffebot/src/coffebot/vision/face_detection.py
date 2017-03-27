#!/usr/bin/env python3
import logging

logging.basicConfig(filename='face_detection.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.ERROR)

from utils.opencv import find_faces
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

        faces = find_faces(image)

        closest_face = {'x': 0, 'y': 0, 'w': 0, 'h': 0}
        max_face_square = 0

        for face in faces:
            current_square = face['w'] * face['h']
            if current_square > max_face_square:
                closest_face = face
                max_face_square = current_square

        return closest_face
