from apium import create_app
from apium.extensions import celery

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        celery.start()
