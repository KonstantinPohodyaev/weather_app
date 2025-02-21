from http import HTTPStatus

import requests

from .constants import (
    CURRENT_WEATHER_DATA_ENDPOINT, OPEN_WEATHER_KEY
)
from .tools import lead_hpa_to_mm_mercury
from .exceptions import OpenWeatherBadRequest


OPEN_WEATHER_BAD_REQUEST = (
    'К сожалению мы не можем обработать город {city}. '
    'Проверьте, правильно ли  вы указали его название.'
)


def get_weather_params(city):
    response = requests.get(
        CURRENT_WEATHER_DATA_ENDPOINT,
        params=dict(
            q=city,
            appid=OPEN_WEATHER_KEY,
            units='metric',
            lang='ru'
        )
    )
    if response.status_code != HTTPStatus.OK:
        raise OpenWeatherBadRequest(
            OPEN_WEATHER_BAD_REQUEST.format(city=city)
        )
    weather = response.json()
    return dict(
        temperature=weather['main']['temp'],
        pressure=lead_hpa_to_mm_mercury(weather['main']['pressure']),
        country=weather['sys']['country']
    )
