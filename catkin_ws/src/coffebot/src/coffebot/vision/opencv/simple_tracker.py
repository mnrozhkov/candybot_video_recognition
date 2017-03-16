import sys
sys.path.insert(1,'/usr/local/lib/python3.5/dist-packages')

import cv2
import time
import logging

logging.basicConfig(filename='simple_tracker.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.ERROR)

class Face:
    '''Contains information about face'''
    
    def __init__(self, rect):

    	#face location rectangle {'x': x, 'y': y, 'w': w, 'h': h}
    	self.rect = rect
    	x1 = self.rect['x'] #coordinates of left up angle
    	y1 = self.rect['y']
    	
    	x2 = x1 + self.rect['w'] #coordinates of right down angle
    	y2 = y1 + self.rect['h']
    	
    	self.center = ( (x1 + x2) / 2, (y1 + y2) / 2) #rectangle center coordinates
    	self.square = self.rect['w'] * self.rect['h'] #rectangle square
    	
    def __lt__(self, other): #overload operator <, is needed for sort
    	if self.square > other.square: #the larger the area the closer the image (the smaller distance)
    		return True
    	return False
    	
    def __repr__(self):
    	print('center: ', self.center)
    	print('face square: ', self.square)

    
class SimpleTracker:
    
    
    def __init__(self, face_cascade_file):
        self.faces = []
        self.face_cascade_file = face_cascade_file
        
        
    def find_faces(self, img=None, min_neighbors=5):
        '''Detects faces and faces elements
        Args:
            img: numpy.ndarray
        Returns:
            self.faces: Face objects list
        Raises:
            TypeError: error occured if data is None
        '''
        self.faces = []
        
        if img is None:
            raise TypeError

        face_cascade = cv2.CascadeClassifier()
        
        if not face_cascade.load(self.face_cascade_file):
            logging.error('frontface haarcascade does not exist!' + self.face_cascade_file)
        

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=min_neighbors)
        for (x,y,w,h) in faces:
            new_face = Face({'x': x, 'y': y, 'w': w, 'h': h})
            self.faces.append(new_face)
            
        return self.faces
        
