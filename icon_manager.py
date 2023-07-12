import requests

#from weather_api import Weather_api


class Icon_manager:

    def __init__(self, id_icon):
        self.id_icon = str(id_icon)
        self.base_url = 'https://openweathermap.org/img/wn/'
        self.end_point = '@2x.png'
        

    #https://openweathermap.org/img/wn/10d@2x.png

    def build_url_icon(self):
        url = self.base_url + self.id_icon + self.end_point
        return url 

    def download_icon(self):
        url = self.build_url_icon()
        icon_response = requests.get(url)
        if icon_response.status_code == 200:
            with open('icon.png', 'wb') as file:
                file.write(icon_response.content)
        else:
            print('Error url icon')
