import cv2
from detect_face import FaceDetector

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
sample('images/0.png')

#sample with many faces image
sample('images/SAM_0049.JPG')
