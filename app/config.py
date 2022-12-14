from distutils.util import strtobool
from os import environ


class __DBConfig:
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = strtobool(environ.get('SQLALCHEMY_TRACK_MODIFICATIONS'))


class __GoogleSpreadsheetConfig:
    GOOGLE_SPREADSHEET_ID = environ.get('GOOGLE_SPREADSHEET_ID')
    GOOGLE_API_KEY = environ.get('GOOGLE_API_KEY')


class __TelegramBotConfig:
    TG_TOKEN = environ.get('TG_TOKEN')
    TG_CHAT_ID = environ.get('TG_CHAT_ID')


class Config(__DBConfig, __GoogleSpreadsheetConfig, __TelegramBotConfig):
    DEBUG: bool = strtobool(environ.get('DEBUG', default='False'))
    SECRET_KEY: str = environ.get('SECRET_KEY')

    TMP_FILE_PATH: str = environ.get('TMP_FILE_PATH')
    PERMANENT_FILE_PATH: str = environ.get('PERMANENT_FILE_PATH')

    PAGE_LENGTH: int = 16


config = Config()
