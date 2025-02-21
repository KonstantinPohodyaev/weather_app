from http import HTTPStatus

from flask import render_template

from . import app


@app.errorhandler(HTTPStatus.BAD_REQUEST)
def bad_request_error(error):
    return (
        render_template('errors/400.html'),
        HTTPStatus.BAD_REQUEST
    )


@app.errorhandler(HTTPStatus.NOT_FOUND)
def not_found_error(error):
    return (
        render_template('errors/404.html'),
        HTTPStatus.NOT_FOUND
    )


@app.errorhandler(HTTPStatus.INTERNAL_SERVER_ERROR)
def internal_error(error):
    return (
        render_template('errors/500.html'),
        HTTPStatus.INTERNAL_SERVER_ERROR
    )
