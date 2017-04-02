#!/usr/bin/env python3

'''
face recognition node
'''

import rospy
import std_msgs

from coffebot.vision.utils import image_format_converter
from coffebot.vision import face_recognition

import json
import time

from coffebot.topic_controller import Lock


if __name__ == '__main__':

    rospy.init_node('vision_face_recognition')

    if rospy.has_param('algorithmia_api_key'):
        face_recognition.set_algorithmia_key(key=rospy.get_param('algorithmia_api_key'))

        face_info_publisher = rospy.Publisher('face_info', std_msgs.msg.String, queue_size=1)
        face_detected_publisher = rospy.Publisher('face_detected', std_msgs.msg.Bool, queue_size=1)

        lock_recognize = Lock(msg_type = std_msgs.msg.String)
        rospy.Subscriber('face_image', std_msgs.msg.String, lock_recognize.callback)
        print('vision face recognition start')

        while True:
            msg = lock.message
            if msg is not None:
                face_image = image_format_converter.str2ndarray(msg)
                print(type(face_image))
                if face_image is not None:
                    face_detected_publisher.publish(True)

                    face_info = dict()

                    #search other features: emotions, celebrities similarity, gender, age
                    binary_face_image = image_format_converter.ndarray2format(face_image)
                    face_info['emotions'] = face_recognition.recognize_emotions(binary_face_image)
                    face_info['celebrities_similarity'] = face_recognition.recognize_celebrities_similarity(binary_face_image)
                    face_info['gender'] = face_recognition.recognize_gender(binary_face_image)
                    face_info['age'] = face_recognition.recognize_age(binary_face_image)
                    print(face_info)
                    face_info_publisher.publish(json.dumps(face_info))

            lock.message = None
            time.sleep(0.5)
