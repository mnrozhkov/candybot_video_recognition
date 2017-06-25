#!/usr/bin/env python3

import sys
sys.path.insert(1,'/usr/local/lib/python3.5/dist-packages')

from pathlib import Path
BASE_PATH = Path(__file__).resolve().parents[1].as_posix()

import cv2
import numpy
from typing import List, Dict

from utils import ErrorLogger

FACE_HARRCASCADE_FILE = BASE_PATH + '/haarcascades/haarcascade_frontalface_default.xml'
SMILE_HARRCASCADE_FILE = BASE_PATH + '/haarcascades/haarcascade_smile.xml'


def detect_faces(image: numpy.ndarray or None = None, min_neighbors=5) -> List[Dict[str,int]] or None:
    '''
    Detect faces regions list by image

    Args:
        image: source image
    Returns:
        list of dicts of faces regions coordinates and sizes:
            dictionary = {'x': x,
                          'y': y,
                          'w': w
                          'h': h
                          }
            if image is not None;

        None if image is None
    '''

    if image is None:
        return None

    face_cascade = cv2.CascadeClassifier()
    if not face_cascade.load(FACE_HARRCASCADE_FILE):
        logging.error('haarcascades not found in ' +  BASE_PATH)
        return None

    face_regions = list()

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=min_neighbors)
    for (x,y,w,h) in faces:
        #detect face location
        face_regions.append({'x': int(x), 'y': int(y), 'w': int(w), 'h': int(h)})

    return face_regions


def detect_smile(face_image: numpy.ndarray or None = None, min_neighbors=22) -> bool or None:
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

    smile_cascade = cv2.CascadeClassifier()
    if not smile_cascade.load(SMILE_HARRCASCADE_FILE):
        logging.error('haarcascade smile not found in ' + BASE_PATH)
        return None

    gray = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)
    smiles = smile_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=min_neighbors, minSize=(2,2))
    if len(smiles) > 0:
        return True

    return False
