#!/usr/bin/env python3

'''
tracking face node
'''

import rospy
import std_msgs
from coffebot.msg import FaceCoordinates

from coffebot.vision.utils import image_format_converter
from coffebot.vision import face_detection

import json

from coffebot.topic_controller import Lock

import time


if __name__ == '__main__':

    rospy.init_node('vision_face_tracking')

    face_coord_publisher = rospy.Publisher('face_coord', FaceCoordinates, queue_size=1)
    face_image_publisher = rospy.Publisher('face_image', std_msgs.msg.String, queue_size=1)
    smile_detected_publisher = rospy.Publisher('smile_detected', std_msgs.msg.Bool, queue_size=1)
    tracker = face_detection.FaceTracker()
    lock_image = Lock()
    rospy.Subscriber('image', std_msgs.msg.String, lock_image.callback)

    while True:
        try:
            rospy.get_master().getPid()
        except:
            break

        msg = lock_image.message

        if msg is not None:

            image = image_format_converter.str2ndarray(msg)

            face_region = tracker.find_closest_face_region(image)
            print(face_region)
            print(type(face_region['h']))

            face_coordinates_msg = FaceCoordinates()
            face_coordinates_msg.x = face_region['x']
            face_coordinates_msg.y = face_region['y']
            face_coordinates_msg.w = face_region['w']
            face_coordinates_msg.h = face_region['h']

            face_coord_publisher.publish(face_coordinates_msg)

            x = face_region['x']
            y = face_region['y']
            w = face_region['w']
            h = face_region['h']
            if w > 0 and h > 0:
                    face_array = image[x:x+w, y:y+h]
                    str_face_array = image_format_converter.ndarray2str(face_array)

                    #search smile
                    smile = tracker.detect_smile(face_array)
                    if smile is None:
                            smile = False
                    print('smile: ', smile)
                    smile_detected_publisher.publish(smile)
                    face_image_publisher.publish(str_face_array)

            if lock_image.message == msg:
                lock_image.message = None
            time.sleep(0.5)
