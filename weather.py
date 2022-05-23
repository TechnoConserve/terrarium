import os

import requests

WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
LATITUDE = os.getenv('LATITUDE')
LONGITUDE = os.getenv('LONGITUDE')


def get_weather():
    resp = requests.get(
        f"https://api.openweathermap.org/data/2.5/onecall?lat={LATITUDE}&lon={LONGITUDE}&APPID={WEATHER_API_KEY}")
    return resp