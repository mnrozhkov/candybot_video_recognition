#!/usr/bin/env python3
'''Allows to view from camera and detect face and smile'''
import sys
sys.path.insert(1,'/usr/local/lib/python3.5/dist-packages')

import rospy
import cv2
from candybot_vr.vision.opencv.detect_face2 import FaceDetector
from candybot_vr.msg import VisionMessage

import argparse

import logging
logging.basicConfig(filename='detect_face2.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.ERROR)

def main(min_neighbors=5):
    '''Main function
    Args:
        min_neighbors: minimal face number
    '''
    try:
        #set viewing parameter 
        rospy.set_param('viewing', True)
        
        publisher = rospy.Publisher('vision_decision', VisionMessage, queue_size=1)
        rospy.init_node('viewer', anonymous=True)

        cap = cv2.VideoCapture(0)

        detector = FaceDetector()
        print('view start')
        while True:
            if rospy.get_param('viewing'):
                ret, frame = cap.read()
                if ret:
                    faces = detector.detect(img=frame)
                    message = VisionMessage()
                    print('vvv', message.face_count, ' ' , message.smile)
                    message.face_count = len(faces)
                    
                    for face in faces:
                        if face.smile:
                            message.smile = True

                    publisher.publish(message)
    except Exception as e:        
        logging.error(str(e))
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--min_neighbors', dest='min_neighbors')
    args = parser.parse_args()

    main(min_neighbors=args.min_neighbors)
    
