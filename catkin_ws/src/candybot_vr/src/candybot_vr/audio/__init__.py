#!/usr/bin/env python3

import subprocess


class Sayer:

	def __init__(self, phrase=None, lang = None, voice_type=None):
		self.phrase = phrase
		if lang is None:
			self.lang = 'ru'
		else:
			self.lang = lang
		
		if voice_type is None:
			self.voice_type = 'male1'
		else:
			self.voice_type = voice_type
		
	def say(self):
		if not self.phrase is None:
			echo_proc = subprocess.Popen(['echo', self.phrase], stdout=subprocess.PIPE)
			rhvoice_proc = subprocess.call(['spd-say', '-w', '-o', 'rhvoice',
                                    '-l', self.lang, '-e', '-t', self.voice_type],
                                   stdin=echo_proc.stdout)
	
	def set_phrase(self, phrase):
		
		self.phrase = phrase
		
	def set_lang(self, lang):
		
		self.lang = lang
		
	def set_voice_type(self, voice_type):
		
		self.voice_type = voice_type
		
	def get_available_voices():
		return ['female1', 'female2', 'female3','male1']

