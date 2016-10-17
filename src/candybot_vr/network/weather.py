#!/usr/bin/env python3
'''Allows to get weather'''

import urllib.request

class Weather:

	def __init__(self):
		'''Initialize weather object'''
		
		self.weather = 'Погода в Москве: , '
		self.site = 'https://yandex.ru/pogoda/moscow'
		self.tags = {'temperature': '<div class="current-weather__thermometer current-weather__thermometer_type_now">',
					'wind_speed': 'Ветер: </span> <span class="wind-speed">',
					'humidity' : 'Влажность: </span>',
					'pressure': 'Давление: </span>'}
		self.__parse__()
		
		
	def __parse__(self):
		'''Parses weather from weather site'''
		try:
			response = urllib.request.urlopen(self.site)
			html = response.read().decode('utf-8', 'ignore')
		
			start = html.find(self.tags['temperature'])
			end = html.find('</', start + len(self.tags['temperature']))
			self.weather += 'Температура: ' +  html[start + len(self.tags['temperature']):end].split('\u2009')[0] + ' градусов, '
		
			start = html.find(self.tags['wind_speed'])
			end = html.find('</', start + len(self.tags['wind_speed']))
			value = html[start + len(self.tags['wind_speed']):end].strip().split(' ')[0]
			if value.find('Штиль') == -1:
				value += ' метров в секунду, '
			else:
				value += ', '
			self.weather += 'Ветер: ' +  value
		
			start = html.find(self.tags['humidity'])
			end = html.find('</', start + len(self.tags['humidity']))
			self.weather += 'Влажность: ' +  html[start + len(self.tags['humidity']):end].split('%')[0] + ' процентов, '
		
			start = html.find(self.tags['pressure'])
			end = html.find('</', start + len(self.tags['pressure']))
			self.weather += 'Давление: ' +  html[start + len(self.tags['pressure']):end].split(' ')[0] + ' миллиметров ртутного столба'
		except Exception as e:
			self.weather = 'Не удалось получить сведения'
			print(e)
	
	def get_weather(self):
		'''Returns: string with weather information'''
		return self.weather
