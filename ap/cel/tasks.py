from __future__ import absolute_import

from celery.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from datetime import datetime


logger = get_task_logger(__name__)

def add1(a, b):
	return a + b

# A periodic task that will run every minute (the symbol "*" means every)
@periodic_task(run_every=(crontab(hour="*", minute="*", day_of_week="*")))
def example():
    logger.info("Start task")
    now = datetime.now()
    result = add1(now.day, now.minute)
    logger.info("Task finished: result = %i" % result)


