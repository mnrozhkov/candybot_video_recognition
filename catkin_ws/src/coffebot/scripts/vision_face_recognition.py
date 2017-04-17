#!/usr/bin/env python3

'''
face recognition node
'''

import rospy
from coffebot.msg import FaceFeatures
import ros_numpy
from sensor_msgs.msg import Image

from coffebot.vision.utils import image_format_converter
from coffebot.vision import face_recognition

import time

from coffebot.topic_controller import Lock


if __name__ == '__main__':

    rospy.init_node('vision_face_recognition')

    if rospy.has_param('algorithmia_api_key'):
        face_recognition.set_algorithmia_key(key=rospy.get_param('algorithmia_api_key'))
        face_info_publisher = rospy.Publisher('face_info', FaceFeatures, queue_size=1)

        lock_recognize = Lock()
        rospy.Subscriber('face_image', Image, lock_recognize.callback)
        print('vision face recognition start')

        while True:
            try:
                rospy.get_master().getPid()
            except:
                break

            face_image_msg = lock_recognize.message
            if face_image_msg is not None:
                face_image = ros_numpy.numpify(face_image_msg)
                print(type(face_image))
                if face_image is not None:

                    face_info = dict()

                    #search other features: emotions, celebrities similarity, gender, age
                    binary_face_image = image_format_converter.ndarray2format(face_image)
                    face_features_msg = FaceFeatures()
                    face_features_msg.emotion = face_recognition.recognize_emotion(binary_face_image)
                    face_features_msg.celebrity_name = face_recognition.recognize_celebrities_similarity(binary_face_image)
                    face_features_msg.gender = face_recognition.recognize_gender(binary_face_image)
                    face_features_msg.age = face_recognition.recognize_age(binary_face_image)
                    print(face_features_msg)
                    face_info_publisher.publish(face_features_msg)

            if lock_recognize.message == face_image_msg:
                lock_recognize.message = None
            time.sleep(0.5)
