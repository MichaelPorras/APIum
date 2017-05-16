import time
import logging
from flask import Flask, g
from apium.extensions import celery
from apium import config
from apium.tasks import tasks


def create_app(config=config.base_config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    configure_logging(app)
    app.logger.info('starting application')

    @app.before_request
    def before_request():
        g.request_start_time = time.time()
        g.request_time = lambda: '%.5fs' % (time.time() - g.request_start_time)

    @app.route('/', methods=['GET'])
    def index():
        return 'Hello'

    return app


def register_extensions(app):
    celery.config_from_object(app.config)


def configure_logging(app):
    l = logging.getLogger('werkzeug')
    l.setLevel(10000)

    for h in app.logger.handlers:
        h.setLevel(10000)

    fmt = logging.Formatter('[%(asctime)s] {%(filename)s:%(lineno)d} '
                            '%(levelname)s - %(message)s')

    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)
    sh.setFormatter(fmt)
    app.logger.setLevel(logging.DEBUG)
    app.logger.addHandler(sh)


def register_blueprints(app):
    app.register_blueprint(tasks, url_prefix='/tasks')
