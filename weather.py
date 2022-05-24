import os

import requests

# Possible weather conditions: https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
LATITUDE = os.getenv('LATITUDE')
LONGITUDE = os.getenv('LONGITUDE')

def get_current_condition():
    weather = get_weather().json()
    return weather['weather'][0]['main']

def get_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={LATITUDE}&lon={LONGITUDE}&appid={WEATHER_API_KEY}"
    resp = requests.get(url)
    return resp
