from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

from .constants import CITY_MAX_LENGTH


DATA_REQUIRED_MESSAGE = 'Это поле обязательно к заполнению!'

WEATHER_CITY_LABEL = 'Город'
WEATHER_REGEXP_MESSAGE = 'В названии города есть недопустимые символы!'

WEATHER_SUBMIT_LABEL = 'Запросить'


class WeatherForm(FlaskForm):
    city = StringField(
        WEATHER_CITY_LABEL,
        validators=[
            DataRequired(
                message=DATA_REQUIRED_MESSAGE
            ),
            Length(
                max=CITY_MAX_LENGTH
            )
        ]
    )
    submit = SubmitField(WEATHER_SUBMIT_LABEL)
