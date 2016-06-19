from plan import Plan, Job
import os


SITE_ROOT = os.path.dirname(os.path.realpath(__file__))


class DjangoJob(Job):

  def task_template(self):
    return 'cd {path} && python {task} >> {output}'

cron = Plan()

job = DjangoJob(path=SITE_ROOT, task='task.py', output=os.path.join(SITE_ROOT, 'cron.log'), every='1.day', at='02:00')
cron.job(job)

# cron.command('ls /tmp', every='1.day', at='12:00')
# cron.command('pwd', every='2.month')
# cron.command('pwd', every='1.minute')
#cron.command('echo $(pwd) + $(date) >> ' + os.path.join(SITE_ROOT, 'cron.log'), every='1.day', at='16:39')
# cron.command('echo "ray" + $(date) >> ' + os.path.join(SITE_ROOT, 'cron.log'), every='1.minute')


if __name__ == '__main__':
  cron.run('write')
