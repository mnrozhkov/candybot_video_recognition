#!/usr/bin/env python3

from pathlib import Path

import sys
sys.path.insert(1, '/usr/local/lib/python3.5/dist-packages')

import rospy
from candybot_v2.msg import *
from sensor_msgs.msg import Image

import time
import numpy
import ros_numpy

from audio.utils.audio_format_converter import raw_audio2wav
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
	# ts.add_subscriber('/audio_capture/audio', Audio, lambda data: ts._save_audio('/audio_capture/audio', data.content))
	# ts.add_subscriber('/core_decision_manager/pattern', MotionPattern, lambda data: ts._save_text('/core_decision_manager/pattern', data.name))
	# ts.add_subscriber('/core_decision_manager/emotion', Emotion, lambda data: ts._save_text('/core_decision_manager/emotion', data.name))
	# ts.add_subscriber('/speech_recognition/user_speech_text', UserSpeechText, lambda data: ts._save_text('/speech_recognition/user_speech_text', data.text))
	# ts.add_subscriber('/core_decision_manager/bot_speech_text', BotSpeechText, lambda data: ts._save_text('/core_decision_manager/bot_speech_text', data.text))
	# ts.add_subscriber('/core_decision_manager/bot_speech_text', BotSpeechText, lambda data: ts._save_text('/core_decision_manager/bot_speech_text', data.text))
	ts.add_subscriber('/motion_body_controller/body_motion', BodyMotion, lambda data: ts._save_text('/motion_body_controller/body_motion', 'angle: {0}, emotion: {1}'.format(data.angle, data.emotion)))
	ts.add_subscriber('/motion_eyebrows_controller/eyebrows_motion', EyebrowsMotion, lambda data: ts._save_text('/motion_eyebrows_controller/eyebrows_motion', 'l_angle: {0}, r_angle: {1}, emotion: {2}'.format(data.l_angle, data.r_angle, data.emotion)))
	ts.add_subscriber('/motion_eyes_controller/eyes_motion', EyesMotion, lambda data: ts._save_text('/motion_eyes_controller/eyes_motion', 'angle: {0}, distance_from_center_percent: {1}, emotion: {2}'.format(data.angle, data.distance_from_center_percent, data.emotion)))
	ts.add_subscriber('/motion_head_controller/head_motion', HeadMotion, lambda data: ts._save_text('/motion_head_controller/head_motion', 'h_angle: {0}, v_angle: {1}, emotion: {1}'.format(data.h_angle, data.v_angle, data.emotion)))
	# ts.add_subscriber('/dialog_bot_manager/bot_dialog', APIAIBotAnswer, lambda data: ts._save_text('/dialog_bot_manager/bot_dialog', 'text: {0}, action_name: {1}, action_parameters_in_json: {2}'.format(data.text, data.action_name, data.action_parameters_in_json)))

	ts.add_subscriber('/motion_body_controller/body_state', BodyState, lambda _data: data = _data.state, ts._save_text('/motion_body_controller/body_state', 'angle: {0}, emotion: {1}'.format(data.angle, data.emotion)))
	ts.add_subscriber('/motion_eyebrows_controller/eyebrows_motion', EyebrowsState, lambda _data: data = _data.state, ts._save_text('/motion_eyebrows_controller/eyebrows_state', 'l_angle: {0}, r_angle: {1}, emotion: {2}'.format(data.l_angle, data.r_angle, data.emotion)))
	ts.add_subscriber('/motion_eyes_controller/eyes_motion', EyesState, lambda data: ts._save_text('/motion_eyes_controller/eyebrows_state', 'x: {0}, y: {1}, emotion: {2}'.format(str(data.x), str(data.y), data.emotion)))
	ts.add_subscriber('/motion_head_controller/head_motion', HeadState, lambda _data: data = _data.state ts._save_text('/motion_head_controller/head_state', 'h_angle: {0}, v_angle: {1}, emotion: {1}'.format(data.h_angle, data.v_angle, data.emotion)))

	# ts.add_subscriber('/social/twitter/code_scanner/code', String, lambda data: ts._save_text('/social/twitter/code_scanner/code', data.data))
	# ts.add_subscriber('/social/vk/newsfeed_scanner/hashtag', String, lambda data: ts._save_text('/social/vk/newsfeed_scanner/hashtag', data.data))

	# ts.add_subscriber('/speech_recognition/user_speech_text', UserSpeechText, lambda data: ts._save_text('/speech_recognition/user_speech_text', data.text))
	# ts.add_subscriber('/speech_synthesizer/speech_audio', Audio, lambda data: ts._save_audio('/speech_synthesizer/speech_audio', data.content))

	# ts.add_subscriber('/vision_camera_capture/image', Image, lambda data: ts._save_image('/vision_camera_capture/image', ros_numpy.numpify(data)))
	ts.add_subscriber('/vision_face_recognition/face_info', FaceFeatures, lambda data: ts._save_text('/vision_face_recognition/face_info', 'emotion: {0}, gender: {1}, age: [{2}, {3}]'.format(data.emotion, data.gender, str(data.min_age), str(data.max_age))))
	ts.add_subscriber('/vision_face_tracking/face_coord', FaceCoordinates, lambda data: ts._save_text('/vision_face_tracking/face_coord', 'x: {0}, y: {1}, w: {2}, h: {3}'.format(str(data.x), str(data.y), str(data.w), str(data.h))))
	# ts.add_subscriber('/vision_face_tracking/face_image', Image, lambda data: ts._save_image('/vision_face_tracking/face_image', ros_numpy.numpify(data)))

	print('topic_stat start')
	while True:
		try:
			rospy.get_master().getPid()
		except:
			break

		time.sleep(0.1)
