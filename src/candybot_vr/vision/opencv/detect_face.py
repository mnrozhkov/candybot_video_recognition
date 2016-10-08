'''This module allows to detect faces and faces elements on image using
OpenCV library'''

import cv2
import time
import logging

logging.basicConfig(filename='detect_face.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.ERROR)

class FaceDetector:
    '''Face and face elements detector'''
    
    class Face:
        '''Contains information about face'''

        #face location rectangle {'x': x, 'y': y, 'w': w, 'h': h}
        bounding_poly = {}

        #face elements
        landmarks = {}

        smile = False



    def __init__(self):
        self.faces = []
        
    def detect(self, img=None, min_neighbors=5):
        '''Detects faces and faces elements
        Args:
            img: image data - pixel collection, type data is numpy.ndarray
        Returns:
            self.faces: Face objects list
        Raises:
            TypeError: error occured if data is None
        '''
        self.faces = []
        
        if img is None:
            raise TypeError

        face_cascade = cv2.CascadeClassifier()
        eye_cascade = cv2.CascadeClassifier()
        nose_cascade = cv2.CascadeClassifier()
        mouth_cascade = cv2.CascadeClassifier()
        smile_cascade = cv2.CascadeClassifier()
        
        if not face_cascade.load('haarcascades/haarcascade_frontalface_default.xml'):
            logging.error('frontface haarcascade does not exist!')
        if not eye_cascade.load('haarcascades/haarcascade_eye.xml'):
            logging.error('eyes haarcascade does not exist!')
        if not nose_cascade.load('haarcascades/haarcascade_mcs_nose.xml'):
            logging.error('nose haarcascade does not exist!')
        if not mouth_cascade.load('haarcascades/haarcascade_mcs_mouth.xml'):
            logging.error('mouth haarcascade does not exist!')
        if not smile_cascade.load('haarcascades/haarcascade_smile.xml'):
            logging.error('smile haarcascade does not exist!')

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=min_neighbors)
        for (x,y,w,h) in faces:
            new_face = self.Face()
            #detect face location
            new_face.bounding_poly = {'x': x, 'y': y, 'w': w, 'h': h}

            roi_gray = gray[y:y+h, x:x+w]

            #detect eyes location
            eyes = eye_cascade.detectMultiScale(roi_gray)
            if len(eyes) > 0:
                lex, ley, lew, leh = eyes[0]
                new_face.landmarks['LEFT_EYE'] = {'x': lex, 'y': ley, 'w': lew, 'h': leh}

                if len(eyes) > 1:
                    rex, rey, rew, reh = eyes[0]
                    new_face.landmarks['RIGHT_EYE'] = {'x': rex, 'y': rey, 'w': rew, 'h': reh}

            #detect nose
            nose = nose_cascade.detectMultiScale(roi_gray)
            if len(nose) > 0:
                nx, ny, nw, nh = nose[0]
                new_face.landmarks['NOSE'] = {'x': nx, 'y': ny, 'w': nw, 'h': nh}

            #detect mouth
            mouth = mouth_cascade.detectMultiScale(roi_gray)
            if len(mouth) > 0:
                mx, my, mw, mh = mouth[0]
                new_face.landmarks['MOUTH'] = {'x': mx, 'y': my, 'w': mw, 'h': mh}

            #detect smile
            smile = smile_cascade.detectMultiScale(roi_gray)
            if len(smile) > 0:
                new_face.smile = True

            self.faces.append(new_face)
            
        return self.faces
