#!/usr/bin/env python3

from pathlib import Path

import sys
sys.path.insert(1, '/usr/local/lib/python3.5/dist-packages')

import rospy
from coffebot.msg import *
import time
import numpy

from coffebot.audio.utils.audio_format_converter import raw_audio2wav
import json

import cv2

import os

class TopicStat:
	'''
	writes statistics by publishing through topics
	'''

	def __init__(self, image_extension='.png'):
		'''
		constructor
		'''
		
		self.subscribers = list() #list of subscribers
		self.image_extension = image_extension #default image format extension is png
		
		self.BASE_PATH = Path(__file__).resolve().parents[0].as_posix()
	
	def _create_topic_folder(self, topic_name: str) -> str:
		'''
		if folder woith topic name does not exists create it
		returns topic folder name
		'''
		
		topic_name_folder = self.BASE_PATH + '/' + topic_name.replace('/','_')
		if not os.path.exists(topic_name_folder):
			os.mkdir(topic_name_folder)
		return topic_name_folder
	
	def _save_audio(self, topic_name: str, audio_data: bytes):
		'''
		saves audio file with audio data and with timestamp as name
		'''
		
		timestamp = time.ctime()
		#pyaudio_config = json.loads(rospy.get_param('pyaudio'))
		pyaudio_config = rospy.get_param('pyaudio')
		wav_data = raw_audio2wav(audio_data, pyaudio_config)
		topic_name_folder = self._create_topic_folder(topic_name)
		print(topic_name_folder)
		with open(topic_name_folder + '/' + timestamp + '.wav', 'wb') as f:
			f.write(wav_data)
		
	def _save_image(self, topic_name: str, image: numpy.ndarray):
		'''
		saves image file with image data and with timestamp as name
		'''
		
		timestamp = time.ctime()
		topic_name_folder = self._create_topic_folder(topic_name)
		cv2.imwrite(topic_name_folder + '/' + timestamp + self.image_extension, image)
		
	def _save_text(self, topic_name: str, text: str):
		'''
		appends text into stat file (in topic name folder) with timestamp
		'''
		
		timestamp = time.ctime()
		topic_name_folder = self._create_topic_folder(topic_name)
		with open(topic_name_folder + '/' + 'stat', 'a') as f:
			f.write('[' + timestamp + '] ' + text + '\n')
		
	def add_subscriber(self, topic_name: str, msg_type, callback):
		'''
		add new ROS Subscriber to listen specified topic
		'''
		
		self.subscribers.append(rospy.Subscriber(topic_name, msg_type, callback))
		

if __name__ == '__main__':
	rospy.init_node('topic_stat')
	
	ts = TopicStat()
	ts.add_subscriber('/audio_capture/audio', Audio, lambda data: ts._save_audio('/audio_capture/audio', data.content))
	ts.add_subscriber('/core_decision_manager/pattern', MotionPattern, lambda data: ts._save_text('/core_decision_manager/pattern', data.name))
	ts.add_subscriber('/core_decision_manager/emotion', Emotion, lambda data: ts._save_text('/core_decision_manager/emotion', data.name))
	ts.add_subscriber('/speech_recognition/user_speech_text', UserSpeechText, lambda data: ts._save_text('/speech_recognition/user_speech_text', data.text))
	ts.add_subscriber('/core_decision_manager/bot_speech_text', BotSpeechText, lambda data: ts._save_text('/core_decision_manager/bot_speech_text', data.text))
	ts.add_subscriber('/core_decision_manager/bot_speech_text', BotSpeechText, lambda data: ts._save_text('/core_decision_manager/bot_speech_text', data.text))
	
	print('topic_stat start')
	while True:
		try:
			rospy.get_master().getPid()
		except:
			break
			
		time.sleep(0.1)
	
