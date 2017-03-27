import apiai
import random
import json
from typing import Dict
import logging

logging.basicConfig(filename='bot_client.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.ERROR)


class APIAIBot:
	'''
	simple bot class based on apiai
	'''

	def __init__(self,client_key: str):
		self.client_key = client_key
		self._make_session_id()
		self._connect()

	def _make_session_id(self):
		'''
		creates session_id
		'''
		symbols = '0123456789abcdef'
		self.session_id = ''
		for i in range(36):
		    self.session_id += symbols[random.randint(0, len(symbols) - 1)]

	def _connect(self):
		'''
		connects to api.ai
		'''
		self._ai = apiai.ApiAI(self.client_key)

	def request(self, msg: str) -> Dict or None:
		'''
		makes request and returns response from api.ai bot
		'''
		try:
			req = self._ai.text_request()
			req.lang = 'ru'
			req.session_id = self.session_id
			req.query = msg
			response = json.loads(req.getresponse().read().decode('utf-8'))

			return self._parse_intent(response)
		except Exception as e:
			logging.error(str(e))
			return None

	def _parse_intent(self, intent: Dict) -> Dict:
		try:
			answer = dict()
			#extract bot answer
			answer['text'] = intent['result']['fulfillment']['speech']
			#if command is complete (all required fields are filled), extract the command information
			if 'actionIncomplete' in intent['result']:
				if intent['result']['actionIncomplete'] is False:
					answer['action'] = dict()
					answer['action']['name'] = intent['result']['action']
					answer['action']['parameters'] = intent['result']['parameters']
			return answer
		except Exception as e:
			logging.error(str(e))
			return None
