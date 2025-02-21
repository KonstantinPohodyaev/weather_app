import re

from . import db

from .constants import (
    CITY_MAX_LENGTH, COUNTRY_MAX_LENGTH, CITY_PATTERN,
    MIN_TEMPERATURE, MIN_PRESSURE
)
from .open_weather_api import get_weather_params


CITY_REGEXP_ERROR = (
    'Название города {city} содержит недопустимые символы: '
    '{wrong_symbols}'
)
MIN_TEMPERATURE_ERROR = (
    'Не допустимо низкая температура! '
    'Минимально возможная: {min_temperature}. '
    'Получено: {current_temperature}.'
)
MIN_PRESSURE_ERROR = (
    'Не допустимо низкое давление! '
    'Минимально возможное: {min_pressure}. '
    'Получено: {current_pressure}.'
)
MAX_LENGTH_COUNTRY_ERROR = (
    'Превышена максимально допустимая длина названия страны. '
    'Максимальная длина: {max_length}. '
    'Получено: {current_length}'
)


class Weather(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(CITY_MAX_LENGTH), nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    pressure = db.Column(db.Float, nullable=False)
    country = db.Column(db.String(COUNTRY_MAX_LENGTH), nullable=False)
    date = db.Column(db.DateTime, default=db.func.current_timestamp())

    class ValidationError(Exception):
        pass

    @classmethod
    def get_weather_objects_by_city(cls, city):
        return cls.query.filter_by(city=city).order_by(cls.date)

    @classmethod
    def create(cls, city):
        city = city.capitalize()
        wrong_symbols = re.findall(CITY_PATTERN, city)
        if wrong_symbols:
            raise cls.ValidationError(
                CITY_REGEXP_ERROR.format(
                    city=city,
                    wrong_symbols=wrong_symbols
                )
            )
        new_weather_params = get_weather_params(city)
        temperature = new_weather_params['temperature']
        pressure = new_weather_params['pressure']
        country = new_weather_params['country']
        if temperature < MIN_TEMPERATURE:
            raise cls.ValidationError(
                MIN_TEMPERATURE_ERROR.format(
                    min_temperature=MIN_TEMPERATURE,
                    current_temperature=temperature
                )
            )
        if pressure < MIN_PRESSURE:
            raise cls.ValidationError(
                MIN_PRESSURE_ERROR.format(
                    min_pressure=MIN_PRESSURE,
                    current_pressure=pressure
                )
            )
        if len(country) > COUNTRY_MAX_LENGTH:
            raise cls.ValidationError(
                MAX_LENGTH_COUNTRY_ERROR.format(
                    max_length=COUNTRY_MAX_LENGTH,
                    current_length=len(country)
                )
            )
        weather_objects_by_city = cls.get_weather_objects_by_city(city)
        if weather_objects_by_city.count() == 5:
            db.session.delete(weather_objects_by_city.first())
        new_weather_params = get_weather_params(city)
        new_object = cls(
            city=city,
            temperature=temperature,
            pressure=pressure,
            country=country
        )
        db.session.add(new_object)
        db.session.commit()
        return new_object
