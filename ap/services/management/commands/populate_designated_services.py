from datetime import date, datetime, time, timedelta

from accounts.models import Trainee
from django.core.management.base import BaseCommand
from services.models.assignment import Assignment
from services.models.seasonal_service_schedule import SeasonalServiceSchedule
from services.models.service import Category, Service, ServiceSlot
from services.models.service_hours import ServiceAttendance, ServiceRoll
from services.models.week_schedule import WeekSchedule
from services.models.worker import Worker
from services.models.workergroup import WorkerGroup
from terms.models import Term


# run populate_services before this script
class Command(BaseCommand):
  # to use: python ap/manage.py populate_designated_services --settings=ap.settings.dev
  def _create_services(self):
    scheduler = Trainee.objects.get(firstname="David", lastname="Ye")

    ws, created = WeekSchedule.objects.get_or_create(start=get_next_tuesday(), scheduler=scheduler)
    cat, created = Category.objects.get_or_create(name="Designated Service")
    sched = SeasonalServiceSchedule.objects.get(name='FTTA')
    wg = WorkerGroup.objects.get(name='Trainees')
    serv, created = Service.objects.get_or_create(
        name="Attendance Project", code="AP", category=cat, designated=True, weekday=5, start=time(12, 30), end=time(16)
    )
    wg = WorkerGroup.objects.get(name='Trainees')
    serv.schedule.add(sched)
    serv.save()
    sl, created = ServiceSlot.objects.get_or_create(name="Attendance Project", service=serv, worker_group=wg)
    trainee1 = Trainee.objects.get(lastname="Salamanca")
    assign, created = Assignment.objects.get_or_create(week_schedule=ws, service=serv, service_slot=sl)
    assign.workers.add(trainee1.worker)
    assign.save()

    serv2, created = Service.objects.get_or_create(
        name="Meal Ushering", code="MU", category=cat, designated=True, weekday=5, start=time(12, 30), end=time(16)
    )
    serv2.schedule.add(sched)
    serv2.save()
    sl2, created = ServiceSlot.objects.get_or_create(name="Meal Ushering", service=serv2, worker_group=wg)
    trainee2 = Trainee.objects.get(firstname="Bill")
    assign2, created = Assignment.objects.get_or_create(week_schedule=ws, service=serv2, service_slot=sl2)
    assign2.workers.add(trainee2.worker)
    assign2.save()

  def _create_attendance(self):
    workers = Worker.objects.filter(trainee__is_active=True)
    current_term = Term.curren_term()
    week_range = range(0, current_term.term_week_of_date(date.today()))
    for worker in workers:
      services = worker.designated.all()
      for service in services:
        for week in week_range:
          service_attendance = ServiceAttendance.objects.get_or_create(designated_service=service, worker=worker, term=current_term, week=week)[0]
          service_attendance.excused = True
          service_attendance.save()

  def _delete_duplicates(model, unique_fields):  # id/pk is always unique, so don't include it in unique_fields
    from django.db.models import Count, Min
    ret = []
    # finds a duplicates and gets the lower pk value of each duplicate
    master_pks = model.objects.values(*unique_fields).annotate(Min('pk'), count=Count('pk')).filter(count__gt=1).values_list('pk__min', flat=True)
    # gets a dict of {id: object_to_keep}
    masters = model.objects.in_bulk(list(master_pks))
    for master in masters.values():  # for each object
      # create a filter dictionary of {field: mater_object_value}
      d = dict(zip(unique_fields, [getattr(master, f) for f in unique_fields]))
      # get duplicates, filter out the pk we are keeping and delete the rest
      to_delete = model.objects.filter(**d).exclude(pk=master.pk)
      print to_delete
      msg = to_delete.delete()
      ret.append(msg)
    return ret

  def handle(self, *args, **options):
    print('* Deleting existing designated service data...')
    ServiceRoll.objects.all().delete()
    ServiceAttendance.objects.all().delete()
    print('* Populating designated services...')
    self._create_services()


def get_next_tuesday():
  today = datetime.now().date()
  t = timedelta((12 - today.weekday()) % 7)  # Mon-0, Sun-6
  return today + t
