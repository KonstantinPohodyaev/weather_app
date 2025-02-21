# Weather App
![Flask 3.1.0](https://img.shields.io/badge/Flask-2.3.2-blue?logo=flask)
![Flask-Migrate 4.1.0](https://img.shields.io/badge/Flask_Sqlalchemy-2.3.2-orange?logo=flask)
![Flask-SQLAlchemy 3.1.1](https://img.shields.io/badge/Flask_WTF-2.3.2-purple?logo=flask)
![Flask-WTF 1.2.2](https://img.shields.io/badge/Flask_Migrate-2.3.2-red?logo=flask)
![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-green?logo=python)
![requests 2.32.3](https://img.shields.io/badge/requests-2.3.2-white)
![OpenWeatherMap API](https://img.shields.io/badge/OpenWeatherMap-API-yellow?logo=openweathermap)

>Простое и элегантное погодное приложение, созданное с использованием Flask, которое получает актуальные данные о погоде через API `OpenWeatherMap`. Приложение также включает кастомные страницы ошибок для улучшения пользовательского опыта.

## Возможности

- **Актуальные данные о погоде:** Получайте текущую информацию о погоде для любого города.

- **Кастомные страницы ошибок:** Красиво оформленные страницы для ошибок 404 и 400.

- **История запросов:** Просматривайте историю запросов по городам. В базе хранятся до 5-ти запросов об одном городе. При получении еще одного запроса к тому же городу, самая старая запись заменяется новой

- **Адаптивный дизайн:** Использование `Bootstrap5` для удобного отображения на всех устройствах.

## Установка
Клонируйте репозиторий:

```bash
git clone https://github.com/вашusername/weather-app-flask.git
cd weather-app-flask
```
Создайте виртуальное окружение (рекомендуется):

```bash
python -m venv venv
source venv/bin/activate 
# На Windows используйте `. venv\Scripts\activate`
```
Установите зависимости:

```bash
pip install -r requirements.txt
```
Получите API ключ от `OpenWeatherMap`:

Зарегистрируйтесь на `OpenWeatherMap` и получите API ключ.

Создайте файл `.env` в корне проекта и добавьте туда ваш ключ:

```
API_KEY=ваш_api_ключ
```
Выполните миграции:

```bash
flask db upgrade
```

Запустите приложение:
```bash
flask run
```
Откройте в браузере:

Перейдите по адресу: http://127.0.0.1:5000.

## Использование
- **Главная страница:** Введите название города в поле поиска и нажмите "Получить погоду".

- **История запросов:** Перейдите на страницу `/history{название_города}`, чтобы увидеть 5 последних запросов по текущему городу.

- Ошибки: Если город не найден или произошла ошибка, вы всплывающее flash-сообщение, которое будет сигнализировать о конкретной проблеме.

## Кастомные страницы ошибок
- `404` **(Страница не найдена):** Отображается, если запрашиваемая страница не существует.

- `400` **(Некорректный запрос):** Отображается, если сервер не может обработать запрос.

## Авторство
Автор проекта - Константин Походяев `@kspohodyaev`

[GitHub](https://github.com/KonstantinPohodyaev)


