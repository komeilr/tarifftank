import os


BASEDIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    global BASEDIR
    TESTING = False
    DEBUG = False
    DEBUG_TB_ENABLED = True
    SECRET_KEY = 'change-this-shitty-key'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_POOL_SIZE = 20
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_size':20,
        'pool_recycle':120,
        'pool_pre_ping':True
    }

    RATELIMIT_DEFAULT = "1/second"


class DevelopmentConfig(Config):
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    DEBUG_TB_PROFILER_ENABLED = False
    #SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_POOL_RECYCLE = 299
    SQLALCHEMY_POOL_TIMEOUT = 20
    

class TestingConfig(Config):
    TESTING = True
