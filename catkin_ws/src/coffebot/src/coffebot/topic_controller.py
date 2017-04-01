#!/usr/bin/env python3

class Lock:
    '''
    needs to lock processing new message during processing the old one
    '''

    def __init__(self, msg_type):
        self.msg_type = msg_type
        self.message = None


    def callback(self, data: self.msg_type):
        self.message = data.data
