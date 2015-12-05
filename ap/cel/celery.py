from __future__ import absolute_import

from celery import Celery
from cel import celeryconfig

app = Celery('cel',
             # broker='amqp://localhost',
             # backend='amqp://localhost',
             include=['cel.tasks', 'lifestudies.tasks'])

# Optional configuration, see the application user guide.
app.config_from_object('cel.celeryconfig')

if __name__ == '__main__':
    app.start()