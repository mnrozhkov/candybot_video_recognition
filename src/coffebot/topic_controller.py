#!/usr/bin/env python3

class Lock:
    '''
    needs to lock processing new ROS message during processing the old one
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.message = None

    def callback(self, data):
        '''
        Callback function
        Args:
            data: any data publish by some ROS topic
        '''
        self.message = data
