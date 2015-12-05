from __future__ import absolute_import

BROKER_URL = 'amqp://localhost'
CELERY_RESULT_BACKEND = 'rpc://'
CELERY_RESULT_PERSISTENT = True
# CELERY_RESULT_BACKEND = 'amqp://localhost'

# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_ACCEPT_CONTENT=['json']
CELERY_TIMEZONE = 'US/Pacific-New'

CELERY_SEND_TASK_SENT_EVENT=True

from datetime import timedelta
from celery.schedules import crontab

CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'tasks.add',
        'schedule': timedelta(seconds=30),
        'args': (16, 16)
    },
    # Executes every LD night at 10:00PM
    'assign-discipline': {
        'task': 'tasks.assignDiscipline',
        'schedule': crontab(hour=16, minute=14, day_of_week=5),
        'args': (),
    },
}

CELERY_ENABLE_UTC = True