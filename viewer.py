import cv2
import time


import argparse
import base64

from googleapiclient import discovery
import httplib2
from oauth2client.client import GoogleCredentials


DISCOVERY_URL='https://{api}.googleapis.com/$discovery/rest?version={apiVersion}'


def get_vision_service():
    credentials = GoogleCredentials.get_application_default()
    return discovery.build('vision', 'v1', credentials=credentials,
                           discoveryServiceUrl=DISCOVERY_URL)

def detect(face_file, face_max_results=1, label_max_results=5):
    image_content = face_file.read()
    batch_request = [{
        'image':{
            'content': base64.b64encode(image_content).decode('UTF-8')
            },
        'features':[
            {
                'type': 'FACE_DETECTION',
                'maxResults': face_max_results,
                },
            {
                'type': 'LABEL_DETECTION',
                'maxResults': label_max_results,
                }]
        }]

    service = get_vision_service()
    request = service.images().annotate(body={
        'requests': batch_request,
        })
    response = request.execute()

    return (response['responses'][0]['faceAnnotations'],
            response['responses'][0]['labelAnnotations'] )

def main():
    
    cap = cv2.VideoCapture(0)
    start_time = time.time()
    count = 0

    img_base_path = 'imgs/image'
    face_info_base_path = 'face_info/'
    label_info_base_path = 'label_info/'
    while True:
        write_start = time.time()
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        img_full_path = img_base_path + str(count) + '.jpg'
        print(cv2.imwrite(img_full_path, frame))

       
        with open(img_full_path, 'rb') as img:
            print('write time = ', time.time() - write_start)
            try:
               
                face_info, label_info = detect(img)
                
            except KeyError:
                face_info, label_info = (None, None)

         
        if not (face_info is None or label_info is None):
            
            face_info_full_path = face_info_base_path + str(count) + '.txt'
            label_info_full_path = label_info_base_path + str(count) + '.txt'

            with open(face_info_full_path, 'w') as face_file:
                face_file.write(str(face_info))

            with open(label_info_full_path, 'w') as label_file:
                label_file.write(str(label_info))

            count += 1
           
if __name__ == '__main__':
    main()
