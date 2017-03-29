#!/usr/bin/env python3
'''
photo capture and save node
1. take command to take video frame and to save it as image
2. save image
'''

import rospy
import std_msgs

from coffebot.vision import photo_capture
from coffebot.vision.utils import image_format_converter

import json


if __name__ == '__main__':

    rospy.init_node('vision_photo_capture')

    print('photo capture start')

    clear_make_photo_pub = rospy.Publisher('make_photo', std_msgs.msg.String, queue_size=1)

    def callback_make_photo(data: std_msgs.msg.String) -> None:
        '''
        data.data contains string represantation of dictionary with structure:
        make_photo_dictionary = {
            'make_photo': True,
            'photo_file_name': absolute or relative path with photo file name
        }
        '''

        if len(data.data) > 0:
            make_photo_dictionary = json.loads(data.data)

            if make_photo_dictionary['make_photo'] is True:

                photo_saved = False

                def callback_get_image(data: std_msgs.msg.String) -> None:
                    '''
                    1. takes message from image topic
                    2. converts it to numpy.ndarray frame
                    3. save it as image file
                    '''

                    frame = image_format_converter.str2ndarray(data.data)
                    photo_capture.save_photo(frame, make_photo_dictionary['photo_file_name'])
                    image_sub.unregister()

                image_sub = rospy.Subscriber('image', std_msgs.msg.String, callback_get_image)



    rospy.Subscriber('make_photo', std_msgs.msg.String, callback_make_photo)

    rospy.spin()
