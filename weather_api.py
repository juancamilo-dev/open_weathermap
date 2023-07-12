import requests
import json

from urllib.parse import urlencode
from art import *

from icon_manager import Icon_manager


class Weather_api:


    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'http://api.openweathermap.org/data/2.5/'

    def build_url(self, city):
        params = {
                'q' : city,
                'appid' : self.api_key,
                'lang' : 'es',
                'units' : 'metric'
                }

        encoded_params = urlencode(params)
        
        url = f'{self.base_url}weather?{encoded_params}'
        return url

    def get_weather(self, city):
        #url = f'{self.base_url}weather?q={city}&appid={self.api_key}&lang=es&units=metric'
        url = self.build_url(city)
        #print(url)
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_icon_code(self, weather_data):
        if weather_data:
           id_icon = weather_data['weather'][0]['icon']
           icon_manager = Icon_manager(id_icon)
           icon_manager.download_icon()
        else:
            return None

    def show_weather_data(self, weather_data):
        if weather_data:
            #print(weather_data)
            city = weather_data['name']
            country = weather_data['sys']['country']
            temperature = weather_data['main']['temp']
            temp_min = weather_data['main']['temp_min']
            temp_max = weather_data['main']['temp_max']
            clouds = weather_data['clouds']['all']
            description = weather_data['weather'][0]['description']
            icon = self.get_icon_code(weather_data)

            tprint(city, 'rand')
            print(f' {icon} {description.capitalize()}')
            print(f'{city}, {country}. Cuenta con una temperatura de:')
            print(f'{temperature} °C, una temperatura máxima de: {temp_max}°C')
            print(f'y una temperatura mínima de: {temp_min}°C')
            print(f'Con una nubosidad de {clouds}%')
        else:
            print('Error fetching weather data')
        
