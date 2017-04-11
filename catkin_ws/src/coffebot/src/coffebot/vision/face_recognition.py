#!/usr/bin/env python3
import logging
import os
LOG_FOLDER = 'logs'
if os.path.exists(LOG_FOLDER) is False:
    os.mkdir(LOG_FOLDER)

logging.basicConfig(filename=LOG_FOLDER + '/' + __name__ + '.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.DEBUG)

from coffebot.vision.utils import opencv, algorithmia
import numpy


def set_algorithmia_key(key: str):
    algorithmia.api_key = key


def recognize_emotions(face_image: numpy.ndarray or None = None) -> dict or None:

    if face_image is None:
        return None

    try:
        return algorithmia.get_emotions(face_image)
    except Exception as e:
        logging.error(str(e))
        return None


def recognize_celebrities_similarity(face_image: numpy.ndarray or None = None) -> list or None:

    if face_image is None:
        return None

    try:
        return algorithmia.celebrities_similarity(face_image)
    except Exception as e:
        logging.error(str(e))
        return None


def recognize_2faces_similarity(face_image1: numpy.ndarray or None = None, face_image2: numpy.ndarray or None = None) -> float or None:

    if face_image is None:
        return None

    try:
        return algorithmia.verify_faces(face_image1, face_image2)
    except Exception as e:
        logging.error(str(e))
        return None


def recognize_gender(face_image: numpy.ndarray or None = None) -> dict or None:

    if face_image is None:
        return None

    try:
        return algorithmia.gender(face_image)
    except Exception as e:
        logging.error(str(e))
        return None


def recognize_age(face_image: numpy.ndarray or None = None) -> dict or None:

    if face_image is None:
        return None

    try:
        return algorithmia.age(face_image)
    except Exception as e:
        logging.error(str(e))
        return None
