import os


class base_config(object):
    """Default configuration options."""
    SITE_NAME = 'Apium'

    BROKER_HOST = os.environ.get('CELERY_HOST', 'localhost')
    BROKER_PORT = os.environ.get('CELERY_PORT', '6379')
    BROKER_URL = 'redis://{}:{}/0'.format(BROKER_HOST, BROKER_PORT)
    BROKER_BACKEND = BROKER_URL

    CELERY_BROKER_URL = BROKER_URL
    CELERY_RESULT_BACKEND = CELERY_BROKER_URL


class dev_config(base_config):
    """Development configuration options."""
    DEBUG = True
    ASSETS_DEBUG = True


class test_config(base_config):
    """Testing configuration options."""
    TESTING = True
