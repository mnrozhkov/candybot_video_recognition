#!/usr/bin/env python3
import logging

logging.basicConfig(filename='face_recognition.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.ERROR)

from coffebot.vision.utils import opencv, algorithmia
import numpy


def set_algorithmia_key(key: str):
    algorithmia.api_key = key


def recognize_emotions(face_image: numpy.ndarray or None = None) -> dict or None:

    if face_image is None:
        return None

    return algorithmia.get_emotions(face_image)


def recognize_celebrities_similarity(face_image: numpy.ndarray or None = None) -> list or None:

    if face_image is None:
        return None

    return algorithmia.celebrities_similarity(face_image)


def recognize_2faces_similarity(face_image1: numpy.ndarray or None = None, face_image2: numpy.ndarray or None = None) -> float or None:

    if face_image is None:
        return None

    return algorithmia.verify_faces(face_image1, face_image2)


def recognize_gender(face_image: numpy.ndarray or None = None) -> dict or None:

    if face_image is None:
        return None

    return algorithmia.gender(face_image)


def recognize_age(face_image: numpy.ndarray or None = None) -> dict or None:

    if face_image is None:
        return None

    return algorithmia.age(face_image)
