from flask import current_app
from marshmallow import ValidationError


class CustomException(Exception):
    def __init__(self, http_code, message, **params):
        self.http_code = http_code
        self.message = message
        self.body = {**params}

    @property
    def json(self):
        return {
            'error': type(self).__name__,
            'msg': self.message,
            'body': self.body
        }


class Unauthorized(CustomException):
    def __init__(self, message: str = 'Пользователь не авторизован.'):
        super().__init__(http_code=401, message=message)


class Forbidden(CustomException):
    def __init__(self, message: str = 'Пользователю запрещена данная операция.'):
        super().__init__(http_code=403, message=message)


class NoSuchEntityError(CustomException):
    def __init__(self, message: str = 'Нет такой сущности.'):
        super().__init__(http_code=404, message=message)


class LogicError(CustomException):
    def __init__(self, message='Логическая ошибка.'):
        super().__init__(http_code=409, message=message)


@current_app.errorhandler(CustomException)
def handle_requests(error: CustomException):
    return error.json, error.http_code


@current_app.errorhandler(ValidationError)
def handle_requests(error: ValidationError):
    return {'error': error.messages}, 422
