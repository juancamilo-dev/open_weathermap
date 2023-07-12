import json

from icon_manager import Icon_manager
from api_secret import Api_secret
from weather_api import Weather_api

def main(api_key):

    city = input('Enter City Name: ')

    api = Weather_api(api_key)
    weather_data = api.get_weather(city)
    api.show_weather_data(weather_data)


if __name__ == "__main__":    
    api_secret_instance = Api_secret()
    decrypted_api_key = api_secret_instance.get_decrypted_api_key()
    if decrypted_api_key:
        main(decrypted_api_key)

