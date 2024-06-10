import os

# https://flask.palletsprojects.com/en/2.3.x/config/


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_URI_DEV')


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
