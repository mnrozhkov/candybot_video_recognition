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
            return r['results']['confidence']
    except Exception as e:
        logging.error(str(e))
        return None
