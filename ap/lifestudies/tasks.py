from __future__ import absolute_import

from celery.schedules import crontab
from celery.decorators import periodic_task, task
from celery.utils.log import get_task_logger
from datetime import datetime

from attendance.utils import Period
from terms.models import Term
from accounts.models import Trainee
from lifestudies.models import Discipline
from datetime import date

logger = get_task_logger(__name__)


@periodic_task(run_every=(crontab(hour="*", minute="*", day_of_week="*"))) #Run every minute
def example():
    logger.info("Start task")
    now = datetime.now()
    result = now.day + now.minute
    logger.info("Task finished: result = %i" % result)

#Unfortunately this task doesn't work because the Discipline.calculate_summary static function does not work properly
@periodic_task(run_every=(crontab(hour="10", minute="0", day_of_week="6"))) #Run every Lord's Day at 10pm
def assignDiscipline_periodic():
    logger.info("Start task")
    term = Term.objects.last()
    period = Period(term).period_of_date(date.today())
    for trainee in Trainee.objects.all():
        s = Discipline.calculate_summary(trainee, period)
        logger.info(trainee.firstname + trainee.lastname + " : " + str(s) + " life studies")

#this is very ugly basically copy pasted, not sure how to solve
@task
def assignDiscipline_task():
    logger.info("Start task")
    term = Term.objects.last()
    period = Period(term).period_of_date(date.today())
    for trainee in Trainee.objects.all():
        s = Discipline.calculate_summary(trainee, period)
        logger.info(trainee.firstname + trainee.lastname + " : " + str(s) + " life studies")