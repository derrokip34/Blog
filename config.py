import os
class Config():
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://derrick:montolivo@localhost/blog'
    QUOTE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    SECRET_KEY = 'AFSLoTBl'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://derrick:montolivo@localhost/blog'

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://derrick:montolivo@localhost/blog'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://derrick:montolivo@localhost/blog'
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'testing': TestConfig
}