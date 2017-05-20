#!/usr/bin/env python3

import json
from pathlib import Path
top = Path(__file__).resolve().parents[0].as_posix()

from urllib import request

key = ''
initialized = False

cities = dict()

def init(cities_file_name):

    global cities
    global initialized

    try:
        cities = json.load(open(top + '/' + cities_file_name, 'r'))
        initialized = True
    except Exception as e:
        logging.error(str(e))


def get_weather(city_name):

    if initialized is True and len(cities) > 0:
        city_id = cities.get(city_name.lower().strip())
        if city_id is not None:
            url = 'http://api.openweathermap.org/data/2.5/weather?id=' + \
                  str(list(city_id.values())[0]) + '&appid=' + key

            try:
                req = request.urlopen(url)
                return req.read()
            except Exception as es:
                logging.error(str(e))
                return None
