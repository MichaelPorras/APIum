# from flask import current_app, request, Response, jsonify, g, session
from flask import current_app
from ..tasks import tasks
import jobs
import time


@tasks.route('/test')
def core_device_pull():
    result = jobs.runthis.apply_async()
    current_app.logger.info(result)
    current_time = time.strftime("%c")
    return 'Current date time is %s' % current_time
