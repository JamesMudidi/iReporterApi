# Import neccessary depencies
# The OS module provides a way of using OS dependent functionality.
# In this case os.environ() to get the users' environment
import os

# Parent configuration class.
# Shared across all environments
class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')

# Configuration for the Development environment.
class DevelopmentConfig(Config):
    DEBUG = True

# Configuration for the Testing environment, with a separate test database.
class TestingConfig(Config):
    TESTING = True
    DEBUG = True

# Configuration for the Production environment.
class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}