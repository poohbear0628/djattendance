from django_cron import CronJobBase, Schedule
from datetime import datetime

class MyCronJob(CronJobBase):
  RUN_EVERY_MINS = 5 # every 2 hours

  schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
  code = 'ap.cron.my_cron_job'    # a unique code

  def do(self):
    print 'cron job!!!', datetime.now()


class BackupDBCronJob(CronJobBase):
  RUN_AT_TIMES = ['6:00']

  schedule = Schedule(run_at_times=RUN_AT_TIMES)

  def do(self):
    print 'backup db!!', datetime.now()