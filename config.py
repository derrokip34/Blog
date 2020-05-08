import os
class Config():
    QUOTE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'

class ProdConfig(Config):
    pass

class TestConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'testing': TestConfig
}