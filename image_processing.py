'''sends images from IM_PATH to Google Vision API,
recieves response and formats it and then writes it
into file
'''

import os
import argparse
import base64

from PIL import Image
from PIL import ImageDraw

from googleapiclient import discovery
import httplib2
from oauth2client.client import GoogleCredentials

import json
import dict_fortmatting_test

# [START get_vision_service]
DISCOVERY_URL='https://{api}.googleapis.com/$discovery/rest?version={apiVersion}'


def get_vision_service():
    credentials = GoogleCredentials.get_application_default()
    return discovery.build('vision', 'v1', credentials=credentials,
                           discoveryServiceUrl=DISCOVERY_URL)
# [END get_vision_service]


# [START detect_face]
def detect_face(face_file, max_results=1):
    """Uses the Vision API to detect faces in the given file.

    Args:
        face_file: A file-like object containing an image with faces.

    Returns:
        An array of dicts with information about the faces in the picture.
    """
    image_content = face_file.read()
    batch_request = [{
        'image': {
            'content': base64.b64encode(image_content).decode('UTF-8')
            },
        'features': [{
            'type': 'FACE_DETECTION',
            'maxResults': max_results,
            }]
        }]

    service = get_vision_service()
    request = service.images().annotate(body={
        'requests': batch_request,
        })
    response = request.execute()

    return response['responses'][0]['faceAnnotations'][0]
# [END detect_face]


#image folder name
IM_PATH = 'images'
#image folder info name
IM_INFO_PATH = 'images_info'

if os.path.exists(IM_PATH):
    images = os.listdir(IM_PATH)

if not os.path.exists(IM_INFO_PATH):
    os.mkdir(IM_INFO_PATH)

count = 0

for img in images:
    image_info = detect_face(open(IM_PATH + '/' + img,'rb'))
    full_path = IM_INFO_PATH + '/' + str(count)
    with open(full_path, 'w') as file:
        file.write(dict_fortmatting_test.format_dict(image_info))
        #json.dump(image_info, file)
    count += 1
