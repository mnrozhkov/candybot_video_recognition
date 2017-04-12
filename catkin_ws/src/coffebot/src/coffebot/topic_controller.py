#!/usr/bin/env python3

class Lock:
    '''
    needs to lock processing new message during processing the old one
    '''

    def __init__(self):
        self.message = None


    def callback(self, data):
        self.message = data
