from django.core.management.base import BaseCommand
from services.models import Service, Category, Worker, WorkerGroup, ServiceSlot, ScheduleCategory, SeasonalServiceSchedule
from terms.models import Term
from datetime import time

WEEKDAYS = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: "Lord's Day",
}


def create_weekly_service_for_days(wg_db, service_wgs, name, code, days, start, seasonal_schedule, end=None):
    # Create category to group all services in
    category, created = Category.objects.get_or_create(name=name)
    category.save()

    for day in days:
        day_name = '%s (%s)' % (name, WEEKDAYS[int(day)])
        s, created = Service.objects.get_or_create(name=day_name, code=code, category=category, weekday=int(day), start=start, end=end)
        s.schedule.add(seasonal_schedule)
        s.save()
        # Check if service is defined in service_wgs and add workergroup from wg_db
        if name in service_wgs:
            for slotname, count in service_wgs[name]:
                slot = ServiceSlot(name=slotname, service=s, worker_group=wg_db[slotname], workers_required=count)
                slot.save()


class Command(BaseCommand):
    # to use: python ap/manage.py populate_services --settings=ap.settings.dev
    def _create_services(self):
        every_day = ['']
        tue_sun = [i for i in range(1, 7)]
        mon_sat = [i for i in range(0, 6)]
        tue_fri = [i for i in range(1, 5)]
        mon_thur = [i for i in range(0, 3)]

        '''
            Designated services:
            A/V
            Shuttle Drivers
            Outline Sisters
            Piano Service
            Badges

            AP
            AM
            SS
        '''

        workergroups = ['*', '1TB', '1TS', 'B', 'RetB', 'S', 'RetS', 'Trainees', 'B car', 'S*', 'B*', 'S car']
        allworkers = Worker.objects.all()

        wg_db = {}

        for wg in workergroups:
            nwg, created = WorkerGroup.objects.get_or_create(name=wg)
            if created:
                nwg.workers = allworkers
                nwg.save()

            wg_db[wg] = nwg

        services = {
            'Breakfast Prep'   : ('br prp',   tue_sun, (6, 30), (7, 50)),
            'Breakfast Cleanup': ('br clnup', tue_sun, (7, 50), (8, 50)),
            'Lunch Cleanup'    : ('lnch clnup', [5,],  (11, 50), (12, 50)),
            'Lunch Prep'       : ('lnch prp',   [5,],  (7, 55), (12, 30)),
            'Supper Prep'      : ('sppr prp', mon_sat, (15, 30), (18, 10)),
            'Supper Cleanup'   : ('sppr clnup', mon_sat,(18, 10), (19, 30)),
            'Supper Delivery'  : ('sppr dlvry', [1, 2, 3, 5], (18, 15), (19, 15)),
            'Restroom Cleaning': ('rstrm cln', [1, 2, 3, 5], (18, 10), (19, 20)),
            'Chairs'           : ('chairs', [0, 2],    (18, 15), (19, 0)),
            'Sack Lunch'       : ('sack lnch', mon_thur, (18, 20), (19, 20)),
            'Space Cleaning'   : ('space cln', [2,],    (18, 10), (19, 15)),
            'Dust Mopping'     : ('dust mop', [5,],     (11, 55), (13, 30))
        }

        service_wgs = {
            'Breakfast Cleanup': [('*', 2), ('1TB', 0), ('1TS', 0), ('B', 7), ('RetB', 0), ('RetS', 0), ('S', 8)],
            'Breakfast Prep'   : [('*', 1), ('Trainees', 10)],
            'Chairs'           : [('*', 6), ('B', 26)],
            'Dust Mopping'     : [('*', 2), ('S', 16)],
            'Lunch Cleanup'    : [('*', 2), ('1TB', 0), ('1TS', 0), ('B', 7), ('RetB', 0), ('RetS', 0), ('S', 8)],
            'Lunch Prep'       : [('1TB', 0), ('1TS', 0), ('B', 3), ('RetB', 0), ('RetS', 0), ('S', 5)],
            'Restroom Cleaning': [('B*', 1), ('S*', 1), ('B', 2), ('S', 3)],
            'Sack Lunch'       : [('*', 2), ('1TS', 0), ('RetS', 0), ('S', 21)],
            'Space Cleaning'   : [('*', 4), ('S', 10)],
            'Supper Cleanup'   : [('*', 2), ('1TB', 0), ('1TS', 0), ('B', 7), ('RetB', 0), ('RetS', 0), ('S', 8)],
            'Supper Delivery'  : [('B car', 1), ('S car', 1)],
            'Supper Prep'      : [('1TB', 0), ('1TS', 0), ('B', 3), ('RetB', 0), ('RetS', 0), ('S', 5)],
        }

        # Create regular FTTA schedule
        schedule_category, created = ScheduleCategory.objects.get_or_create(name='FTTA')
        schedule_category.save()
        seasonal_schedule, created = SeasonalServiceSchedule.objects.get_or_create(name='FTTA', category=schedule_category)
        seasonal_schedule.save()

        for name, (code, days, (sh, sm), (eh, em)) in services.items():
            create_weekly_service_for_days(wg_db, service_wgs, name, code, days, time(sh, sm), seasonal_schedule, time(eh, em))

        print 'done'

    def handle(self, *args, **options):
        self._create_services()


'''
Breakfast Cleanup   Breakfast cleanups

Breakfast Prep  Prepare breakfast for all the trainees

Chairs  Making the chairs straight

Designated Services

Dust Mopping    Dust mopping service

Floor Non-designated    Floor Non-designated

Guard Duty  Guard the training center facilities

Hall Vacuuming  Vacuuming the training center

Lunch Cleanup   Lunch cleanups

Lunch Prep  Prepare lunch for all the trainees

Restroom Cleaning   Restroom cleaning

Sack Lunch  Prepare lunches for campus trainees

Sack Supper

Space Cleaning

Supper Cleanup  Supper cleanups

Supper Delivery Delivering meals to the houses

Supper Prep Prepare supper for all the trainees
'''