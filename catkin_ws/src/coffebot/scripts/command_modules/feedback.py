import sys
sys.path.insert(1,'/usr/local/lib/python3.5/dist-packages') 

import rospy
from std_msgs.msg import String

from coffebot import convert
import base64
import time
import cv2
import os

FEEDBACK_FOLDER = 'FEEDBACK'
MSG_DURATION = 30 #seconds

def recordMsg():
	raw_audio = b''
	#record audio
	def callback_audio(data):
		raw_audio += base64.b64decode(data.data.encode('utf-8'))
	
	audio_sub = rospy.Subscriber('audio_capture', String, callback_audio)
	
	#record video
	if os.path.exists(FEEDBACK_FOLDER) is not True:
		os.mkdir(FEEDBACK_FOLDER)
	
	new_msg_folder = FEEDBACK_FOLDER + '/' + str(len(os.listdir(FEEDBACK_FOLDER)) + 1)
	os.mkdir(new_msg_folder)
	audio_folder = new_msg_folder + '/audio'
	video_folder = new_msg_folder + '/video'
	
	os.mkdir(audio_folder)
	os.mkdir(video_folder)
	
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(video_folder + '/video.avi', fourcc, 8.0, (640,480))
    
	def callback_image(data):
		frame = convert.str2ndarray(data.data)
		out.write(frame)
			
	image_sub = rospy.Subscriber('image_capture', String, callback_image)
	
	start = time.time()	
	while time.time() - start:
		sleep(0.1)
		
	audio_sub.unregister()
	image_sub.unregister()
	out.release()
	
	wav_data = convert.raw_audio2wav(raw_audio)
	with open(audio_folder + '/audio.wav', 'wb') as af:
		af.write(wav_data)
	
