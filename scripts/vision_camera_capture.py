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

from utils import ErrorLogger


if __name__ == '__main__':
    rospy.init_node('vision_camera_capture')

    try:

        publisher = rospy.Publisher('/vision_camera_capture/image', Image, queue_size=1)
        cap = cv2.VideoCapture(0)

        print('view start')
        while True:
            try:
                rospy.get_master().getPid()
            except:
                break

            ret, frm = cap.read()
            if ret:
                frame = cv2.flip(frm, 0)
                #frame = frm
                image = ros_numpy.msgify(Image, frame, encoding='bgr8')
                publisher.publish(image)
                time.sleep(0.1)

    except Exception as e:
        ErrorLogger(__file__, e)
