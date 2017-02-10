from weather import Weather
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

w = Weather(appid='9c321878cd88f7d6721253a59639816f')

def main(city_name):
	city_name = city_name.lower()
	cities = json.load(open(sys.path[0] + '/' + 'cities2.txt','r'))
		
	nf_city = normal_form(city_name)
	if nf_city in cities.keys():
		city = cities[nf_city]
	elif city_name in cities.keys():
		city = cities[city_name]
	else:
		city = 'moscow'
	print(w.get_weather(city))


if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--city_name')
	args = parser.parse_args()
	main(city_name=args.city_name.strip())
	
