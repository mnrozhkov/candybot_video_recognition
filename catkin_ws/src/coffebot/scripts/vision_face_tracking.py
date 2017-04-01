#!/usr/bin/env python3

'''
tracking face node
'''

import rospy
import std_msgs

from coffebot.vision.utils import image_format_converter
from coffebot.vision import face_detection

import json


if __name__ == '__main__':

    rospy.init_node('vision_face_tracking')

    face_coord_publisher = rospy.Publisher('face_coord', std_msgs.msg.String, queue_size=1)
    face_image_publisher = rospy.Publisher('face_image', std_msgs.msg.String, queue_size=1)
    smile_detected_publisher = rospy.Publisher('smile_detected', std_msgs.msg.Bool, queue_size=1)
    tracker = face_detection.FaceTracker()

    def callback_image(data: std_msgs.msg.String) -> None:
        image = image_format_converter.str2ndarray(data.data)

        face_region = tracker.find_closest_face_region(image)
        print(face_region)
        print(type(face_region['h']))
        face_coord_publisher.publish(json.dumps(face_region))

        x = face_region['x']
        y = face_region['y']
        w = face_region['w']
        h = face_region['h']
        if w > 0 and h > 0:
            face_array = image[x:x+w, y:y+h]
            str_face_array = image_format_converter.ndarray2str(face_array)

            #search smile
            smile = tracker.detect_smile(face_image)
            if smile is None:
                smile = False
            print('smile: ', smile)
            smile_detected_publisher.publish(smile)
            face_image_publisher.publish(str_face_array)

    rospy.Subscriber('image', std_msgs.msg.String, callback_image)

    rospy.spin()
