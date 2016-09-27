'''This module allows to detect faces and faces elements on image using
OpenCV library'''

import cv2
import time
import logging

logging.basicConfig(filename='detect_face2.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.ERROR)

class FaceDetector:
    '''Face and face elements detector'''
    
    class Face:
        '''Contains information about face'''

        #face location rectangle {'x': x, 'y': y, 'w': w, 'h': h}
        bounding_poly = {}

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
        smile_cascade = cv2.CascadeClassifier()
        
        if not face_cascade.load('haarcascades/haarcascade_frontalface_default.xml'):
            logging.error('frontface haarcascade does not exist!')
        if not smile_cascade.load('haarcascades/haarcascade_smile.xml'):
            logging.error('smile haarcascade does not exist!')

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=min_neighbors)
        for (x,y,w,h) in faces:
            new_face = self.Face()
            #detect face location
            new_face.bounding_poly = {'x': x, 'y': y, 'w': w, 'h': h}

            roi_gray = gray[y:y+h, x:x+w]
            
            #detect smile
            smile = smile_cascade.detectMultiScale(roi_gray)
            if len(smile) > 0:
                new_face.smile = True

            self.faces.append(new_face)
            
        return self.faces
