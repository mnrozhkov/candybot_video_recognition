#!/usr/bin/env python3
'''Allows to view from camera and detect face and smile'''
import sys
sys.path.insert(1,'/usr/local/lib/python3.5/dist-packages')


import rospy
from std_msgs.msg import String
import cv2
from coffebot import convert
import time
import logging

logging.basicConfig(filename='viewer.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.ERROR)
    

def main():
    '''Main function
    '''
    try:
        
        publisher = rospy.Publisher('image_capture', String, queue_size=1)
        rospy.init_node('viewer')

        cap = cv2.VideoCapture(0)

        print('view start')
        while True:
            ret, frame = cap.read()
            if ret:
                str_image = convert.ndarray2str(frame)
                publisher.publish(str_image)
                time.sleep(0.1)     

    except Exception as e:        
        logging.error(str(e))
        print(str(e))
    

if __name__ == '__main__':
    main()
