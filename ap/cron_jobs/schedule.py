from plan import Plan, Job
import os
import sys


SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
MANAGE_ROOT = os.path.dirname(SITE_ROOT)

LOG_FILE = 'cron.log'
LOG_PATH = os.path.join(SITE_ROOT, LOG_FILE)


PROJECT_RELATED_ENV = ['SECRET_KEY', 'ABSENTEE_ROSTER_RECIPIENTS', 'VIRTUAL_ENV',
                        'DJANGO_SETTINGS_MODULE', 'DATABASE_URL',
                        ]

ENVIRONMENT = {}

# Add in environment vars relevant to the proj
for var in PROJECT_RELATED_ENV:
  if var in os.environ:
    ENVIRONMENT[var] = os.environ[var]


class DjangoJob(Job):

  def task_template(self):
    return 'cd %s && python {task} >> {output}' % (SITE_ROOT)

class DjangoCommandJob(Job):

  def task_template(self):
    # return 'source ~/.bashrc && workon %s && cd %s && python manage.py {task} >> %s' % (VIRTUALENV, MANAGE_ROOT, LOG_PATH)
    return 'cd %s && {environment} %s manage.py {task} >> {output}' % (MANAGE_ROOT, sys.executable)

cron = Plan(environment=ENVIRONMENT, output=LOG_PATH)


#################################### Job definitions ###################################

job = DjangoJob(task='task.py', every='1.day', at='02:00')
cron.job(job)

absentee_report_job = DjangoCommandJob(task='send_absentee_roster_emails', every='1.minute')
cron.job(absentee_report_job)
# cron.command('env > ~/cronenv', every='1.minute')
# cron.command('ls /tmp', every='1.day', at='12:00')
# cron.command('pwd', every='2.month')
# cron.command('pwd', every='1.minute')
#cron.command('echo $(pwd) + $(date) >> ' + os.path.join(SITE_ROOT, 'cron.log'), every='1.day', at='16:39')
cron.command('echo "ray" + $(date) >>', every='1.minute')


#################################### Flush #######################################

cron.run('write')
