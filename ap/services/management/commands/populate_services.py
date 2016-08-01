from django.core.management.base import BaseCommand
from services.models import Service, Category
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


def create_weekly_service_for_days(name, code, days, start, end=None):
    # Create category to group all services in
    category, created = Category.objects.get_or_create(name=name)
    category.save()

    for day in days:
        day_name = '%s (%s)' % (name, WEEKDAYS[int(day)])
        s, created = Service.objects.get_or_create(name=day_name, code=code, category=category, weekday=int(day), start=start, end=end)
        s.save()


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

        services = {
            'Breakfast Prep'   : ('br prp',   tue_sun, (6, 0), (7, 45)),
            'Breakfast Cleanup': ('br clnup', tue_sun, (7, 45), (9, 0)),
            'Lunch Cleanup'    : ('lnch clnup', [5,],  (12, 30), (2, 0)),
            'Supper Prep'      : ('sppr prp', mon_sat, (15, 0), (18, 0)),
            'Supper Cleanup'   : ('sppr clnup', mon_sat,(18, 0), (20, 0)),
            'Restroom Cleaning': ('rstrm cln', [0, 2], (18, 0), (19, 30)),
            'Chairs'           : ('chairs', [0, 2],    (18, 20), (19, 00)),
            'Sack Lunch'       : ('sack lnch', mon_thur, (18, 0), (19, 0)),
        }

        for name, (code, days, (sh, sm), (eh, em)) in services.items():
            create_weekly_service_for_days(name, code, days, time(sh, sm), time(eh, em))

        print 'done'

    def handle(self, *args, **options):
        self._create_services()