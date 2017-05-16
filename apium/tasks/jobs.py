from apium.extensions import celery
import time


@celery.task
def runthis():
    for i in range(0, 5):
        print 'lololool'
        time.sleep(1)
