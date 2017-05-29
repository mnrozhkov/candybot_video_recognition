#!/usr/bin/env python3
'''
Uses findface.pro api
'''
import requests

import os
LOG_FOLDER = 'logs'
if os.path.exists(LOG_FOLDER) is False:
    os.mkdir(LOG_FOLDER)

logging.basicConfig(filename=LOG_FOLDER + '/' + __name__ + '.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.DEBUG)

token = ''

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

    url = 'https://api.findface.pro/v0/verify'
    header = {
        'Host': 'api.findface.pro',
        'Authorization': 'Token ' + token
        }

    files = {
        'photo1': img1,
        'photo2': img2
        }
    try:
        r = requests.post(url=url, files=files, headers=header)
        if r['verified'] is True:
            return r['results'][0]['confidence']
    except Exception as e:
        logging.error(str(e))
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

    url = 'https://api.findface.pro/v0/face'
    header = {
        'Host': 'api.findface.pro',
        'Authorization': 'Token ' + token
        }

    files = {'photo': img}
    
    try:
        r = requests.post(url=url, files=files, headers=header)
        return r['results'][0]['id']
    except Exception as e:
        logging.error(str(e))
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

    url = 'https://api.findface.pro/v0/identify'
    header = {
        'Host': 'api.findface.pro',
        'Authorization': 'Token ' + token
        }

    files = {'photo': img}
    
    try:
        r = requests.post(url=url, files=files, headers=header)
        results = r['results']
        return results[ list(results.keys())[0] ]['confidence']
    except Exception as e:
        logging.error(str(e))
        return None
    
