import requests
import logging
import json

logging.basicConfig(filename='face_recognition.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.ERROR)

HOST = 'api.findface.pro'
TOKEN = 'bbpwYV-3rMcIP1-9ZNrgYo9GGqWPG9Zp'


def verify_faces(photo1, photo2):
    '''Compares two photos.
    Args:
        photo1: first image file name
        photo2: second image file name
    Returns:
        float confidence value: if data recieved
        None: if failed
    '''
    try:
        img1 = open(photo1, 'rb').read()
        img2 = open(photo2, 'rb').read()
        
        url = 'https://' + HOST + '/v0/verify'
        header = {'Host': HOST,
                  'Authorization': 'Token ' + TOKEN,
                  }

        files = {
            'photo1': img1,
            'photo2': img2
            }
        
        response = requests.post(url, headers=header, files=files)
        return json.loads(response.text)['results'][0]['confidence']
    except Exception as e:
        logging.error(str(e))
        return None


def add_face(photo):
    '''Adds photo to gallery.
    Args:
        photo: image file name
    Returns:
        response: json response with info about addition
    '''
    try:
        url = 'https://' + HOST + '/v0/face'
        header = {'Host': HOST,
                  'Authorization': 'Token ' + TOKEN,
                  }
        img = open(photo, 'rb').read()
        files = {'photo': img}

        response = requests.post(url, headers=header,files=files)
        return json.loads(response.text)
    except Exception as e:
        logging.error(str(e))
        return None


def delete_face(face_id):
    '''Deletes photo from gallery.
    Args:
        face_id: face id in gallery
    Returns:
        response: json response with info about deleting
        response = '' if face deleted
    '''

    try:
        url = 'https://' + HOST + '/v0/face/id/' + str(face_id)
        header = {'Host': HOST,
                  'Authorization': 'Token ' + TOKEN,
                  }

        response = requests.delete(url, headers=header)
        return json.loads(response.text)
    except Exception as e:
        logging.error(str(e))
        return None

def identify_face(photo):
    '''Finds similar photo in gallery.
    Args:
        photo: image file name
    Returns:
        response: json response with info about photo comparison
    '''
    
    try:
        url = 'https://' + HOST + '/v0/identify'
        header = {'Host': HOST,
                  'Authorization': 'Token ' + TOKEN,
                  }
        img = open(photo, 'rb').read()
        files = {'photo': img}

        response = requests.post(url, headers=header,files=files)
        return json.loads(response.text)
    except Exception as e:
        logging.error(str(e))
        return None

def all_faces_info():
    '''Return information about all faces in dataset'''

    try:
        url = 'https://' + HOST + '/v0/faces'
        header = {'Host': HOST,
                  'Authorization': 'Token ' + TOKEN,
                  }

        response = requests.get(url, headers=header)
        return json.loads(response.text)
    except Exception as e:
        logging.error(str(e))
        return None


def face_info(face_id):
    '''Returns photo info by its id in gallery
    Args:
        face_id: face id in gallery
    Returns:
        face information
    '''

    try:
        url = 'https://' + HOST + '/v0/faces/id/' + str(face_id)
        header = {'Host': HOST,
                  'Authorization': 'Token ' + TOKEN,
                  }

        response = requests.get(url, headers=header)
        return json.loads(response.text)
    except Exception as e:
        logging.error(str(e))
        return None
