from urllib import parse, request
import json

class Weather:

    def __init__(self, appid):
        
        self.appid = appid
        self.url_base = 'http://api.openweathermap.org/data/2.5/weather?'

    def __wind_direction__(self, deg):
        
        directions = ['северный','северо-восточный','восточный',
                      'юго-восточный','южный','юго-западный',
                      'западный','северо-западный']
        
        deg %= 360
        return directions[int(deg) // 45]
            
        
    def get_weather(self, city_name='moscow'):

        url = self.url_base + 'q=' + city_name + '&'
        url += 'appid=' + self.appid + '&' + 'units=metric'
        
        req = request.urlopen(url)
        all_info = json.loads(req.read().decode('utf-8'))
        
        weather_info = 'Температура: ' + str(all_info['main']['temp']) + \
                       ' Давление: ' + str(all_info['main']['pressure']) + \
                       ' Влажность:' + str(all_info['main']['humidity']) + \
                       ' Ветер:' + str(all_info['wind']['speed']) + ' м/с, ' + \
                                self.__wind_direction__(all_info['wind']['deg'])
        
        return weather_info
        
        

