#!/usr/bin/env python3

'''
tracking face node
'''

import rospy
from candybot_v2.msg import FaceCoordinates, SmileDetected
import ros_numpy
from sensor_msgs.msg import Image

from vision.utils import image_format_converter
from vision import face_detection

import json

from utils.topic_controller import Lock

import time


if __name__ == '__main__':

    rospy.init_node('vision_face_tracking')

    face_coord_publisher = rospy.Publisher('/vision_face_tracking/face_coord', FaceCoordinates, queue_size=1)
    face_image_publisher = rospy.Publisher('/vision_face_tracking/face_image', Image, queue_size=1)
    smile_detected_publisher = rospy.Publisher('/vision_face_tracking/smile_detected', SmileDetected, queue_size=1)

    tracker = face_detection.FaceTracker()

    lock_image = Lock()
    rospy.Subscriber('/vision_camera_capture/image', Image, lock_image.callback)

    while True:
        try:
            rospy.get_master().getPid()
        except:
            break

        msg = lock_image.message #read image from message

        if isinstance(msg, Image):

            image = ros_numpy.numpify(msg)
            #exctract the closest face region
            face_region = tracker.find_closest_face_region(image)
            print(face_region)

            face_coordinates_msg = FaceCoordinates()
            face_coordinates_msg.x = face_region['x']
            face_coordinates_msg.y = face_region['y']
            face_coordinates_msg.w = face_region['w']
            face_coordinates_msg.h = face_region['h']
            #publish face coordinates
            face_coord_publisher.publish(face_coordinates_msg)

            x = face_region['x']
            y = face_region['y']
            w = face_region['w']
            h = face_region['h']
            if w > 0 and h > 0:
                    face_array = image[x:x+w, y:y+h]
                    face_image_msg = ros_numpy.msgify(Image, face_array, encoding='rgb8')
                    #search smile in face region
                    smile = tracker.detect_smile(face_array)
                    if smile is None:
                        smile = False
                    print('smile: ', smile)
                    #publish smile existance status
                    smile_detected_msg = SmileDetected(detected=smile)
                    smile_detected_publisher.publish(smile_detected_msg)
                    #publish face image
                    face_image_publisher.publish(face_image_msg)

            if lock_image.message == msg:
                lock_image.message = None
            time.sleep(0.5)
