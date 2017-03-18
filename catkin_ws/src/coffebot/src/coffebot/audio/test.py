from synthesizer import Talker
from recorder import Recorder
from recognizer import SpeechRecognizer
import convert

import rospy

if __name__ == '__main__':
	'''
	talker = Talker(yandex_voice_key='49d9bb75-7419-45cc-9988-76052abc6c44')
	talker.sayyandex(text='Дорогой длинною!')
	'''
	
	srec = Recorder(pyaudio_config=rospy.get_param('pyaudio'))
	sr = SpeechRecognizer(yandex_voice_key='49d9bb75-7419-45cc-9988-76052abc6c44')
	
	while True:
		input('rec >')
		raw_audio = srec.listen()
		print('recorded!')
		wav = convert.raw_audio2wav(raw_audio=raw_audio, pyaudio_config=rospy.get_param('pyaudio'))
		text = sr.asr_yandex(wav)
		print('text:',text)
