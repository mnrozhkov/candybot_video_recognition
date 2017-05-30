#!/usr/bin/env python3
'''
photo capture and save node
1. take command to take video frame and to save it as image
2. save image
'''

import rospy

import ros_numpy
from sensor_msgs.msg import Image

from vision import photo_capture

import actionlib

from candybot_v2.msg import MakePhotoAction

import time


class MakePhotoServer:

    def __init__(self, topic_name):
        self.server = actionlib.SimpleActionServer(topic_name, MakePhotoAction, self.execute, False)
        self.server.start()

    def execute(self, goal):

        #read goal field : MakePhoto type
        make_photo_msg = goal.make_photo_command
        if make_photo_msg.make_photo is True and len(make_photo_msg.photo_file_name) > 0:

            def callback_get_image(data: Image) -> None:
                '''
                1. takes message from image topic
                2. converts it to numpy.ndarray frame
                3. save it as image file
                '''

                frame = ros_numpy.numpify(data)
                photo_capture.save_photo(frame, make_photo_msg.photo_file_name)
                image_sub.unregister()

            image_sub = rospy.Subscriber('/vision_camera_capture/image', Image, callback_get_image)

        self.server.set_succeeded()


if __name__ == '__main__':

    rospy.init_node('vision_photo_capture')
    print('photo capture start')
    make_photo_server = MakePhotoServer(topic_name='make_photo')

    while True:
        try:
            rospy.get_master().getPid()
        except:
            break

        time.sleep(0.5)
