import base64
from googleapiclient import discovery
import httplib2
from oauth2client.client import GoogleCredentials

import logging
import time

logging.basicConfig(filename='vision_recognition.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.INFO)


# [START get_vision_service]
DISCOVERY_URL='https://{api}.googleapis.com/$discovery/rest?version={apiVersion}'


class VisionRecognition:
    '''Allows to detect and to recognize objects on image'''


    class Label:
        '''Holds label parameters'''

        descriprion = ''
        score = 0.0
        
        
    class Face:
        '''Holds face parameters and information about face elements'''

        #face location
        bounding_poly = []
        fd_bounding_poly = []

        #face elements
        landmarks = {}
        
        roll_angle = 0
        pan_angle = 0
        tilt_angle = 0
        detection_confidence = 0
        landmarking_confidence = 0

        #possible, likely and very likely emotions list
        emotions = []


    class Text:
        '''Holds text parameters'''

        locale = ''
        description = ''
        bounding_poly = []
        
    
    def __init__(self, image=None, max_results=4):
        '''VisionRecognition constructor
        Args:
            image: file name of image to recognize
            max_results: maximum features to recognize
        Raises:
            TypeError: error occured when image is not initialized (is None)
        '''
        
        if image is None:
            raise TypeError
        self.labels = []
        self.faces = []
        self.texts = []
        
        self.dominant_color = (0,0,0)

        with open(image, 'rb') as image_file:
            image_content = image_file.read()

        #request header    
        self.batch_request = [{
            'image': {
                'content': base64.b64encode(image_content).decode('UTF-8')
                },
            'features': [
                {
                    'type': 'LABEL_DETECTION',
                    'maxResults': max_results,
                },
                {
                    'type': 'FACE_DETECTION',
                    'maxResults': max_results,
                },
                {
                    'type': 'TEXT_DETECTION',
                    'maxResults': max_results,
                },
                {
                    'type': 'IMAGE_PROPERTIES',
                    'maxResults': max_results,
                }
                ]
            }]

    def __extract__(self):
        '''Extracts information about objects'''

        response = self.response['responses'][0]
            
        #extract labels info
        try:
            labels = response['labelAnnotations']
        except KeyError:
            labels = []

        for label in labels:
            new_label = self.Label()
            new_label.description = label['description']
            new_label.score = label['score']
            self.labels.append(new_label)

        #extract faces info
        try:
            faces = response['faceAnnotations']
        except KeyError:
            faces = []

        for face in faces:
            new_face = self.Face()
            new_face.bounding_poly = face['boundingPoly']['vertices']
            new_face.bounding_poly = face['fdBoundingPoly']['vertices']

            new_face_landmarks = face['landmarks']
            for landmark in new_face_landmarks:
                new_face.landmarks[landmark['type']] = landmark['position']

            new_face.roll_angle = face['rollAngle']
            new_face.pan_angle = face['panAngle']
            new_face.tilt_angle = face['tiltAngle']
            new_face.detection_confidence = face['detectionConfidence']
            new_face.landmark_confidence = face['landmarkingConfidence']

            emotions = ['joyLikelihood', 'sorrowLikelihood',
                        'angerLikelihood', 'surpriseLikelihood']
            for emotion in emotions:
                em_value = face[emotion]
                if em_value in ['POSSIBLE', 'LIKELY', 'VERY_LIKELY']:
                        new_face.emotions.append(emotion)
            
            self.faces.append(new_face)

        #extract text info
        try:
            texts = response['textAnnotations']
        except KeyError:
            texts = []

        for text in texts:
            new_text = self.Text()
            new_text.locale = text['locale']
            new_text.description = text['description']
            new_text.bounding_poly = text['boundingPoly']['vertices']
            self.texts.append(new_text)

        #extract dominant color
        try:
            colors = response['imagePropertiesAnnotation']['dominantColors']['colors']
        except KeyError:
            colors = []

        max_pixel_fraction = 0
        for color in colors:
            if color['pixelFraction'] > max_pixel_fraction:
                max_pixel_fraction = color['pixelFraction']
                color_value = color['color']
                self.dominant_color = (color_value['red'], color_value['green'], color_value['blue'])
            
    
    def recognize_all(self):
        '''Recognizes all features on image'''

        #create Google Credentials
        credentials = GoogleCredentials.get_application_default()
        #connect to Google Cloud Vision API Service
        service = discovery.build('vision', 'v1', credentials=credentials,
                           discoveryServiceUrl=DISCOVERY_URL)

        #form request
        request = service.images().annotate(body={
            'requests': self.batch_request,
            })
        #recieve response

        self.response = request.execute()
        logging.info(str(self.response))
        
        #extract information from response
        self.__extract__()
        

    def get_labels(self):
        '''Returns labels list'''

        return self.labels

    def get_faces(self):
        '''Returns faces list'''
        
        return self.faces

    def get_texts(self):
        '''Returns texts list'''
        
        return self.texts
    
    def get_dominant_color(self):
        '''Returns tuple in the form (R,G,B)'''
        
        return self.dominant_color
