import os

class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '5g\x01\xb4u}\xe2\xe7\xb1\x94\x12\xf1\x11^\\n\x15,\xf9(e|\xd5\x0f'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class DevConfig(BaseConfig):
    DEBUG = True

class HerokuConfig(BaseConfig):
    DEBUG = False
