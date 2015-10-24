import os
class Config(object):
    DEBUG = True
    TESTING = True
    CSRF_ENABLED = True
    SECRET_KEY = 'secret'
    SQLALCHEMY_DATABASE_URI = os.environ['DB_URL']