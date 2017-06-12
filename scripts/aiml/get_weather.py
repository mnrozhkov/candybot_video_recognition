#!/usr/bin/env python3

import rospy
from network.weather import WeatherInfo
import sys
import argparse
import json
from pymorphy2 import MorphAnalyzer

def normal_form(phrase):
        
        morph = MorphAnalyzer()
        words = phrase.split()
        normal_words = []
        for word in words:
            normal_words.append(morph.parse(word)[0].normal_form)

        return ' '.join(normal_words)

def main(city_name):
	rospy.init_node('get_weather')
	if rospy.has_param('openweathermap_key') is True:
		w = WeatherInfo(openweathermap_key=rospy.get_param('openweathermap_key'))
		nf_city = normal_form(city_name.lower())
		weather_info = w.get_weather(city_name=nf_city)
		weather_string = str()
		weather_string += 'температура: ' + str(weather_info['temp']) + ', '
		weather_string += 'давление: ' + str(weather_info['pressure']) + ' миллиметров ртутного столба, '
		weather_string += 'ветер: ' + str(weather_info['wind_speed']) + ' метров в секунду, ' + str(weather_info['wind_direction']) + ', '
		weather_string += 'влажность: ' + str(weather_info['humidity']) + ' процентов'
		
		print(weather_string)


if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--city_name')
	args = parser.parse_args()
	main(city_name=args.city_name.strip())
	
