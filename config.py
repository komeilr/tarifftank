import os
from os.path import join
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(join(basedir, '.env'))

class Config:
    
    BASEDIR = basedir
    TESTING = False
    DEBUG = False
    DEBUG_TB_ENABLED = False
    SECRET_KEY = 'change-this-shitty-key'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    RATELIMIT_DEFAULT = "1/second"

    MAINTENANCE_MODE = False
    


class DevelopmentConfig(Config):
    DEBUG = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    DEBUG_TB_PROFILER_ENABLED = False

    #SQLALCHEMY_ECHO = True
    SQLALCHEMY_ENGINE_OPTIONS = {
    'pool_size':20,
    'pool_recycle':120,
    'pool_pre_ping':True
    }    
    
    RECAPTCHA_USE_SSL = False
    RECAPTCHA_PUBLIC_KEY = '6LfCns8UAAAAABaaZ9dvqNoG4G1fvWlsl_7q37Dn'
    RECAPTCHA_PRIVATE_KEY = '6LfCns8UAAAAAGWtvxN4jnKH5lTopLj3BQA6ZGcz'
    RECAPTCHA_OPTIONS = {'theme':'black'} 


class ProductionConfig(Config):
    FLASK_ENV=os.environ.get('FLASK_ENV') or 'production'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_POOL_RECYCLE = 299
    SQLALCHEMY_POOL_TIMEOUT = 20
    SQLALCHEMY_ENGINE_OPTIONS = {
    'pool_size':20,
    'pool_recycle':120,
    'pool_pre_ping':True    
    }

    PREFERRED_URL_SCHEME = 'https'

    RECAPTCHA_USE_SSL = True
    RECAPTCHA_PUBLIC_KEY = '6LetnM8UAAAAANpxaVKmXhKmqt39CUglb0ZNgxpF'
    RECAPTCHA_PRIVATE_KEY = '6LetnM8UAAAAAEPQXmhQIjCJwPxEnLkeTywHtvGE'
    RECAPTCHA_OPTIONS = {'theme':'black'} 

    WTF_CSRF_TIME_LIMIT = None
    

class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    
    RECAPTCHA_OPTIONS =	{'theme': 'black'}
    RECAPTCHA_PRIVATE_KEY =	'6LfCns8UAAAAAGWtvxN4jnKH5lTopLj3BQA6ZGcz'
    RECAPTCHA_PUBLIC_KEY =	'6LfCns8UAAAAABaaZ9dvqNoG4G1fvWlsl_7q37Dn'
    RECAPTCHA_USE_SSL =	False