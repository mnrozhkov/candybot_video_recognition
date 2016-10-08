#!/usr/bin/env python3
'''Allows to view from camera and detect face and smile'''

import rospy
import cv2
from candybot_vr.vision.opencv.detect_face2 import FaceDetector
from candybot_vr.msg import VisionMessage

import argparse

def main(min_neighbors=5):
    '''Main function
    Args:
        min_neighbors: minimal face number
    '''
    
    print('start')
    #set viewing parameter 
    rospy.set_param('viewing', True)
    
    publisher = rospy.Publisher('vision_decision', VisionMessage, queue_size=1)
    rospy.init_node('viewer', anonymous=True)

    cap = cv2.VideoCapture(0)

    detector = FaceDetector()
    
    while True:
        if rospy.get_param('viewing'):
            ret, frame = cap.read()
            if ret:
                faces = detector.detect(img=frame)
                message = VisionMessage()
                message.face_count = len(faces)
                for face in faces:
                    if face.smile:
                        message.smile = True

                rospy.set_param('listening', False)
                rospy.set_param('viewing', False)
                publisher.publish(message)
                

    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--min_neighbors', dest='min_neighbors')
    args = parser.parse_args()

    main(min_neighbors=args.min_neighbors)
    
