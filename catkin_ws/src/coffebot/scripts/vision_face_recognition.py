#!/usr/bin/env python3

'''
face recognition node
'''

import pospy
import std_msgs

from coffebot.vision.utils import image_format_converter
from coffebot.vision import face_recognition

import json


if __name__ == '__main__':

    rospy.init_node('vision_face_recognition')

    if rospy.has_param('algorithmia_api_key'):
        face_recognition.set_algorithmia_key(key=rospy.get_param('algorithmia_api_key'))

        face_info_publisher = rospy.Publisher('face_info', std_msgs.msg.String, queue_size=1)
        face_detected_publisher = rospy.Publisher('face_detected', std_msgs.msg.Bool, queue_size=1)
        smile_detected_publisher = rospy.Publisher('smile_detected', std_msgs.msg.Bool, queue_size=1)

        def callback_recognize(data: std_msgs.msg.String) -> None:
            face_image = image_format_converter.str2ndarray(data.data)
            if face_image is not None:
                face_detected_publisher.publish(True)

                face_info = dict()

                #search smile
                smile = face_recognition.recognize_smile(face_image)
                if smile is None:
                    smile = False
                smile_detected_publisher.publish(smile)
                face_info['smile'] = smile

                #search other features: emotions, celebrities similarity, gender, age
                face_info['emotions'] = face_recognition.recognize_emotions(face_image)
                face_info['celebrities_similarity'] = face_recognition.recognize_celebrities_similarity(face_image)
                face_info['gender'] = face_recognition.recognize_gender(face_image)
                face_info['age'] = face_recognition.recognize_age(face_image)

                face_info_publisher.publish(json.dumps(face_info))

        rospy.Subscriber('face_image', std_msgs.msg.String, callback_recognize)

        rospy.spin()
