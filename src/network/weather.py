#!/usr/bin/env python3

import json
from pathlib import Path
top = Path(__file__).resolve().parents[0].as_posix()

from urllib import request

from utils import ErrorLogger


class WeatherInfo:

    def __init__(self, openweathermap_key: str, cities_file_name: str=top + '/' + 'cities.txt'):
        '''
        Constructor
        Args:
            openweathermap_key: openweathermap.org api key (https://openweathermap.org/)
            cities_file_name: cities ids database file name
        '''

        self.cities = dict()

        self.key = openweathermap_key

        try:
            self.cities = json.load(open(cities_file_name, 'r'))
        except Exception as e:
            ErrorLogger(__file__, e)

    def _wind_direction(self, deg: int) -> str:
        directions = ['северный','северо-восточный','восточный',
                      'юго-восточный','южный','юго-западный',
                      'западный','северо-западный']

        deg %= 360
        return directions[int(deg) // 45]

    def get_weather(self, city_name='Москва') -> str:
        '''
        Get weather information
        Args:
            city_name: name of city
        Returns:
            weather information in format:
                dictionary = {
                    'temp': temperature,
                    'pressure': pressure,
                    'humidity': humidity,
                    'wind_speed': wind_speed,
                    'wind_speed': wind_direction
                }
        '''
        if len(self.cities) > 0:
            city_id = self.cities.get(city_name.lower().strip())
            if city_id is not None:
                url = 'http://api.openweathermap.org/data/2.5/weather?id=' + \
                      str(list(city_id.values())[0]) + '&appid=' + self.key + \
                      '&units=metric'

                try:
                    req = request.urlopen(url)
                    info = json.loads(req.read().decode('utf-8'))
                    weather = info['main']

                    weather_info = str()
                    weather_info += 'температура: ' + weather['temp'] + ' градусов, '
                    weather_info += 'давление: ' + weather['pressure'] + ' миллиметров ртутного столба, '
                    weather_info += 'облачность: ' + weather['humidity'] + ' процентов, '
                    weather_info += 'ветер: ' + info['wind']['speed'] + ' метров в секунду, '
                    weather_info += self._wind_direction(info['wind']['deg'])

                    return weather_info
                except Exception as e:
                    ErrorLogger(__file__, e)
                    print(str(e))
                    return None
