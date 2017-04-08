#!/usr/bin/env python3
'''
    1. capture image from camera
    2. image_format_converter it to string
    3. publish string
'''
import sys
sys.path.insert(1,'/usr/local/lib/python3.5/dist-packages')

import rospy
from sensor_msgs.msg import Image

import ros_numpy

import cv2
import time
import logging

logging.basicConfig(filename='viewer.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.ERROR)


if __name__ == '__main__':
    try:

        publisher = rospy.Publisher('image', Image, queue_size=1)
        rospy.init_node('viewer')

        cap = cv2.VideoCapture(0)

        print('view start')
        while True:
            try:
                rospy.get_master().getPid()
            except:
                break

            ret, frame = cap.read()
            if ret:
                image = ros_numpy.msgify(Image, frame, encoding='rgb8')
                publisher.publish(image)
                time.sleep(0.1)

    except Exception as e:
        logging.error(str(e))
        print(str(e))
