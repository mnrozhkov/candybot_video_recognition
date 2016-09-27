import cv2
from detect_face2 import FaceDetector
import time


fd = FaceDetector()

def sample(image=None):
    if image is None:
        raise TypeError

    try:
        faces = fd.detect(img=cv2.imread(image))
    except TypeError:
        print('Image file not found!')

    print('Face number=', len(faces))
    print('First face:')
    print('\t Location: ', faces[0].bounding_poly)
    print('\t Landmarks: ', faces[0].landmarks)
    print('\t Smile: ', faces[0].smile)


#sample with one face image
#sample('images/0.png')

#sample with many faces image
#sample('images/SAM_0049.JPG')


cam = cv2.VideoCapture(0)

while True:
    start = time.time()
    ret, frame = cam.read()
    if ret == True:
        faces = fd.detect(frame)
        for face in faces:
            x = face.bounding_poly['x']
            y = face.bounding_poly['y']
            w = face.bounding_poly['w']
            h = face.bounding_poly['h']
            
            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0),2)
    cv2.imshow('image', frame)
    cv2.waitKey(1)
    print(time.time() - start)
    
cv2.destroyAllWindows()
