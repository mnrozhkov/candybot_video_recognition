#!/usr/bin/env python3

import rospy
import json

import logging
import os
LOG_FOLDER = 'logs'
if os.path.exists(LOG_FOLDER) is False:
    os.mkdir(LOG_FOLDER)

logging.basicConfig(filename=LOG_FOLDER + '/' + __name__ + '.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.DEBUG)

import time


def read_pyaudio_config() -> dict or None:
	'''
	read pyaudio configuration from ROS Parameter Server and return it as dictionary
	'''

	if rospy.has_param('pyaudio'):
		pyaudio_config = rospy.get_param('pyaudio')
		if isinstance(pyaudio_config, dict):
			return pyaudio_config
		elif isinstance(pyaudio_config, str):
			try:
				return json.loads(pyaudio_config)
			except Exception as e:
				logging.error(str(e))
				return None
		else:
			return None


def log_recognized_text(text: str, path: str) -> None:
    '''
    write text into file with time.ctime() as name
    Args:
        text: recognized text
        path: save path
    '''

    try:
        with open(path + '/recognized_text.txt', 'a') as f:
            f.write('[{0}] {1}\n\n'.format(time.ctime(), text))
    except:
        pass
