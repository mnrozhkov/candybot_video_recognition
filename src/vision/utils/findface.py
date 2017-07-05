#!/usr/bin/env python3
'''
Uses findface.pro api
'''

import requests

from utils import ErrorLogger

token = ''


def detect_closest_face(img: bytes) -> dict or None:
    '''
    detect faces and return closest face info
    Args:
        img: image bynary data
    Returns:
        dictionary: {'emotions': list of emotions, 'gender': 'male'|'female', 'age': int}
    '''

    url = 'https://api.findface.pro/v1/detect'
    header = {
        'Host': 'api.findface.pro',
        'Authorization': 'Token ' + token
        }

    files = {'photo': img}
    data = {
        'emotions': True,
        'gender': True,
        'age': True
        }

    try:
        r = requests.post(url=url, files=files, headers=header, data=data).json()
        faces = r['faces']
        info = dict()
        max_face_square = 0

        for face in faces:
            square = (face['x2'] - face['x1']) * (face['y2'] - face['y1'])
            if square > max_face_square:
                info = {'emotions': face['emotions'], 'gender': face['gender'], 'age': face['age']}
                max_face_square = square
        if len(info) == 0:
            return None
        else:
            return info
    except Exception as e:
        ErrorLogger(__file__, e)
        return None


def verify_faces(img1: bytes, img2: bytes) -> float or None:
    '''
    take two face images binary data and calculate its similarity confidence
    Args:
        img1: the first image binary data
        img2: the second image binary data
    Returns:
        similarity confidence: if faces are verified
        None: in othes case
    '''

    url = 'https://api.findface.pro/v1/verify'
    header = {
        'Host': 'api.findface.pro',
        'Authorization': 'Token ' + token
        }

    files = {
        'photo1': img1,
        'photo2': img2
        }
    try:
        r = requests.post(url=url, files=files, headers=header).json()
        if r['verified'] is True:
            return r['results'][0]['confidence']
    except Exception as e:
        ErrorLogger(__file__, e)
        return None


def upload_face_2_gallery(img: bytes) -> int or None:
    '''
    take face image and upload it to findface.pro gallery
    Args:
        img: face image binary data
    Returns:
        img id in gallery : if uploaded
        None : if failed
    '''

    url = 'https://api.findface.pro/v1/face'
    header = {
        'Host': 'api.findface.pro',
        'Authorization': 'Token ' + token
        }

    files = {'photo': img}

    try:
        r = requests.post(url=url, files=files, headers=header).json()
        return r['results'][0]['id']
    except Exception as e:
        ErrorLogger(__file__, e)
        return None


def identify_face(img: bytes) -> float or None:
    '''
    take face image and search it in findface.pro galleries
    Args:
        img: face image binary data
    Returns:
        confidence: if uploaded
        None : if failed
    '''

    url = 'https://api.findface.pro/v1/identify'
    header = {
        'Host': 'api.findface.pro',
        'Authorization': 'Token ' + token
        }

    files = {'photo': img}

    try:
        r = requests.post(url=url, files=files, headers=header).json()
        results = r['results']
        return results[ list(results.keys())[0] ]['confidence']
    except Exception as e:
        ErrorLogger(__file__, e)
        return None
