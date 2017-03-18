import sys
sys.path.insert(1,'/usr/local/lib/python3.5/dist-packages') 

import rospy
from std_msgs.msg import String
from coffebot import convert
import cv2
import time


def tellJokes(parameters=None):
	pass
	
def askPuzzle(parameters=None):
	pass
	
def makePhoto(parameters=None):
	MAX_PHOTO_COUNT = 3
	photo_count = 0
	def callback_image(data.data):
		if photo_count == MAX_PHOTO_COUNT:
			image = convert.str2ndarray(data.data)
			cv2.imwrite('photo', image)
		else:
			photo_count += 1
	sub = rospy.Subscriber('audio_capture', String, callback_image)
	while photo_count < MAX_PHOTO_COUNT:
		time.sleep(0.1)
	sub.unregister()
	
	
def playGane(parameters=None):
	pass
