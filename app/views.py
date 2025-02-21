from flask import render_template, flash

from . import app
from .forms import WeatherForm
from .models import Weather
from .exceptions import OpenWeatherBadRequest


@app.route(
    '/history/<string:city>',
    methods=['GET']
)
def history(city):
    return render_template(
        'history.html',
        weather_objects=Weather.get_weather_objects_by_city(city),
        city=city
    )


@app.route(
    '/',
    methods=['GET', 'POST']
)
def index():
    form = WeatherForm()
    if form.validate_on_submit():
        city = form.city.data
        try:
            new_weather = Weather.create(city)
            return render_template(
                'index.html', form=form, weather=new_weather
            )
        except (OpenWeatherBadRequest, Weather.ValidationError) as error:
            flash(str(error))
    return render_template('index.html', form=form)
