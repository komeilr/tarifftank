import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    TESTING = False
    DEBUG = False
    SECRET_KEY = 'change-this-shitty-key'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 20


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass


class TestingConfig(Config):
    TESTING = True
