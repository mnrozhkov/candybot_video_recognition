#!/usr/bin/env python3

#events set
events = set()
#dictionary: event -> handler
event_hanlers = dict()

class EventRecognizer:

	def __init__(self, data):
		pass
		
	def find_event(self):
		pass

		
class Event:

	def __init__(self):
		pass

		
class EventHandler:
	
	def __init__(self):
		pass
		
	def handle(self, params):
		pass
		
		
class Narrator(EventHandler):
	'''Tells about something'''
	
	def __init__(self):
		pass
	
	def __tell__(self, what):
		pass
	
	def handle(self, params):
		self.__tell__(self, what=params)
			
		
class Demonstrator:
	'''Demonstrates something'''
	
	def __init__(self):
		pass
		
	def demonstrate(self, what):
		pass
		
		
class Writer:
	'''Writes text or video'''
	
	def __init__(self):
		pass
		
	def write(self, write_method, what):
		pass
		
		
#use example
#detect event
phrase = ''
event_recognizer = EventRecognizer(phrase)
#get event and event parameters (phrase text except event word)
event, params = event_recognizer.find_event()
if not event is None:
	#call event handler with its parameters
	event_hanlers[event](params)
