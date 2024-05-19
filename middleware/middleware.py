from flask import request

import app


def log_request_info():
    app.logger.info('Headers: {}', request.headers)
    app.logger.info('Body: {}', request.get_data().decode("utf-8"))


def log_response_info(response):
    app.logger.info('Response: %s', response.get_data(as_text=True))
    return response


def init_app(app):
    app.before_request(log_request_info)
    app.after_request(log_response_info)
