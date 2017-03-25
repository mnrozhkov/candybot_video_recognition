import sys
sys.path.insert(1,'/usr/local/lib/python3.5/dist-packages')

import cv2
import time
import logging

logging.basicConfig(filename='simple_tracker.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.ERROR)

class Face:
    '''Contains information about face'''

    def __init__(self, rect, smile_exists):

    	#face location rectangle {'x': x, 'y': y, 'w': w, 'h': h}
    	self.rect = rect
        self.smile_exists = smile_exists

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

    def printface(self):
    	print('center: ', self.center)
    	print('face square: ', self.square)


class SimpleTracker:


    def __init__(self, face_cascade_file, smile_cascade_file):
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
            return None

        face_cascade = cv2.CascadeClassifier()
        smile_cascade = cv2.CascadeClassifier()

        if not face_cascade.load(self.face_cascade_file):
            logging.error('frontface haarcascade does not exist!' + self.face_cascade_file)
            return None
        elif not smile_cascade.load(self.smile_cascade_file):
        	logging.error('smile haarcascade does not exist!' + self.smile_cascade_file)
            return None
        else:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=min_neighbors)
            for (x,y,w,h) in faces:
                new_face = Face()
                #detect face location
                bounding_poly = {'x': x, 'y': y, 'w': w, 'h': h}

                roi_gray = gray[y:y+h, x:x+w]

                #detect smile
                smile = smile_cascade.detectMultiScale(roi_gray,
                                                       scaleFactor=4,
                                                       minNeighbors=22,
                                                       minSize=(25,25))
                if len(smile) > 0:
                    smile_exists = True
                new_face = Face(rect=bounding_poly, smile_exists=smile_exists)
                self.faces.append(new_face)

            return self.faces
