import os

from dotenv import load_dotenv


load_dotenv()


CITY_MAX_LENGTH = 128
COUNTRY_MAX_LENGTH = 128
MIN_TEMPERATURE = -273
MIN_PRESSURE = 0

CITY_PATTERN = r'[!@#$%^&*(){}.+=-_]'

OPEN_WEATHER_KEY = os.getenv('OPEN_WEATHER_KEY')

LANGUAGE = 'ru'
CURRENT_WEATHER_DATA_ENDPOINT = (
    'http://api.openweathermap.org/data/2.5/weather'
)
