#!/usr/bin/env python3

'''
face recognition node
'''

import rospy
from candybot_v2.msg import FaceFeatures
import ros_numpy
from sensor_msgs.msg import Image

from vision.utils import image_format_converter
from vision.utils import algorithmia

import time

from utils.topic_controller import Lock


if __name__ == '__main__':

    rospy.init_node('vision_face_recognition')

    if rospy.has_param('algorithmia_api_key'):
        algorithmia.api_key=rospy.get_param('algorithmia_api_key')
        face_info_publisher = rospy.Publisher('/vision_face_recognition/face_info', FaceFeatures, queue_size=1)

        lock_recognize = Lock()
        rospy.Subscriber('/vision_face_tracking/face_image', Image, lock_recognize.callback)
        print('vision face recognition start')

        while True:
            try:
                rospy.get_master().getPid()
            except:
                break

            face_image_msg = lock_recognize.message
            if isinstance(face_image_msg, Image):
                face_image = ros_numpy.numpify(face_image_msg)
                print(type(face_image))
                if face_image is not None:

                    #search other features: emotions, celebrities similarity, gender, age
                    binary_face_image = image_format_converter.ndarray2format(face_image)
                    face_features = algorithmia.get_face_features(binary_face_image)
                    if face_features is not None:
                        face_features_msg = FaceFeatures()
                        face_features_msg.emotion = face_features['emotion']
                        face_features_msg.gender = face_features['gender']
                        age_interval = face_features['age']
                        if age_interval is not None:
                            face_features_msg.min_age, face_features_msg.max_age = age_interval

                        print(face_features_msg)
                        face_info_publisher.publish(face_features_msg)

            if lock_recognize.message == face_image_msg:
                lock_recognize.message = None
            time.sleep(0.5)
