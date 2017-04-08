#!/usr/bin/env python3
'''
photo capture and save node
1. take command to take video frame and to save it as image
2. save image
'''

import rospy
from coffebot.msg import MakePhoto
import ros_numpy
from sensor_msgs.msg import Image

from coffebot.vision import photo_capture
from coffebot.vision.utils import image_format_converter

import json

from coffebot.topic_controller import Lock


import time


if __name__ == '__main__':

    rospy.init_node('vision_photo_capture')

    print('photo capture start')

    clear_make_photo_pub = rospy.Publisher('make_photo', MakePhoto, queue_size=1)
    lock_make_photo = Lock()
    rospy.Subscriber('make_photo', MakePhoto, lock_make_photo.callback)

    while True:
        ''' REWRITE!!!
        lock.message contains string represantation of dictionary with structure:
        make_photo_dictionary = {
            'make_photo': True,
            'photo_file_name': absolute or relative path with photo file name
        }
        '''
        try:
            rospy.get_master().getPid()
        except:
            break

        img_msg = lock_make_photo.message
        if img_msg is not None:
            make_photo_dictionary = dict()
            make_photo_dictionary['make_photo'] = img_msg.make_photo
            make_photo_dictionary['photo_file_name'] = img_msg.photo_file_name

            if make_photo_dictionary['make_photo'] is True:

                photo_saved = False

                def callback_get_image(data: Image) -> None:
                    '''
                    1. takes message from image topic
                    2. converts it to numpy.ndarray frame
                    3. save it as image file
                    '''

                    frame = ros_numpy.numpify(data)
                    photo_capture.save_photo(frame, make_photo_dictionary['photo_file_name'])
                    image_sub.unregister()

                image_sub = rospy.Subscriber('image', Image, callback_get_image)

        if lock_make_photo.message == img_msg:
            lock_make_photo.message = None
        time.sleep(0.5)
