# from flask import current_app, request, Response, jsonify, g, session
from flask import current_app
from ..tasks import tasks
import jobs


@tasks.route('/core_pull/<tenant_id>')
def core_device_pull(tenant_id):
    result = jobs.runthis.apply_async()
    current_app.logger.info(result)
    return 'This should return, like, nonw'
