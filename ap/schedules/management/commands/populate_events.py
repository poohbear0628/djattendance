from django.core.management.base import BaseCommand
from schedules.models import Event, Schedule

from datetime import time

class Command(BaseCommand):
    # to use: python ap/manage.py populate_events --settings=ap.settings.dev
    def _create_events(self):
        #GENERAL HOUSE SCHEDULE
        for i in range(1,7):
            name = "Rise"
            code = "RI"
            type = "H"
            start = time(6, 30)
            end = time(6, 45)
            weekday = i
            e = Event(name=name, code=code, type=type, start=start, end=end, weekday=weekday)
            e.save()

        for i in [0,1,2,3,5]:
            name = "House Prayer"
            code = "PR"
            type = "H"
            start = time(22, 0)
            end = time(22, 10)
            weekday = i
            e = Event(name=name, code=code, type=type, start=start, end=end, weekday=weekday)
            e.save()

        for i in [0,1,2,3,5]:
            name = "Lights Out"
            code = "LI"
            type = "H"
            start = time(22, 30)
            end = time(22, 45)
            weekday = i
            e = Event(name=name, code=code, type=type, start=start, end=end, weekday=weekday)
            e.save()

        name = "Lights Out"
        code = "LI"
        type = "H"
        start = time(22, 45)
        end = time(23, 0)
        weekday = 4
        e = Event(name=name, code=code, type=type, start=start, end=end, weekday=weekday)
        e.save()

        name = "Lights Out"
        code = "LI"
        type = "H"
        start = time(23, 30)
        end = time(23, 45)
        weekday = 6
        e = Event(name=name, code=code, type=type, start=start, end=end, weekday=weekday)
        e.save()

        name = "Curfew"
        code = "CU"
        type = "H"
        start = time(22, 30)
        end = time(22, 45)
        weekday = 4
        e = Event(name=name, code=code, type=type, start=start, end=end, weekday=weekday)
        e.save()

        name = "Curfew"
        code = "CU"
        type = "H"
        start = time(23, 0)
        end = time(23, 15)
        weekday = 6
        e = Event(name=name, code=code, type=type, start=start, end=end, weekday=weekday)
        e.save()

        #GENERAL MEAL SCHEDULE
        for i in range(1,7):
            name = "Breakfast"
            code = "BF"
            type = "M"
            start = time(7, 30)
            end = time(8, 0)
            weekday = i
            e = Event(name=name, code=code, type=type, start=start, end=end, weekday=weekday)
            e.save()

        for i in [0,1,2,3,5]:
            name = "Dinner"
            code = "DN"
            type = "M"
            start = time(17, 45)
            end = time(18, 15)
            weekday = i
            e = Event(name=name, code=code, type=type, start=start, end=end, weekday=weekday)
            e.save()

        name = "Lunch"
        code = "LU"
        type = "M"
        start = time(11, 45)
        end = time(12, 15)
        weekday = 5
        e = Event(name=name, code=code, type=type, start=start, end=end, weekday=weekday)
        e.save()

        #MAIN CLASS SCHEDULE
        class_names = [('FM', 'Full Ministry of Christ'), ('GW', 'God-ordained Way'), ('GE', "God's Economy") , ('SP', 'Spirit')]
        i = 0
        type = "C"
        for code, name in class_names:
            start = time(8, 25)
            end = time(10, 0)
            i += 1
            weekday = i
            e = Event(name=name, code=code, type=type, start=start, end=end, weekday=weekday)
            e.save()

        class_names = {'MV': 'Monday Revival Meeting', 'MM': 'Ministry Meeting' , 'VC': 'Video Class'}

        name = class_names['MV']
        code = "MV"
        type = "C"
        start = time(18, 45)
        end = time(21, 15)
        weekday = 0
        e = Event(name=name, code=code, type=type, start=start, end=end, weekday=weekday)
        e.save()

        name = class_names['MM']
        code = "MM"
        type = "C"
        start = time(19, 20)
        end = time(21, 15)
        weekday = 2
        e = Event(name=name, code=code, type=type, start=start, end=end, weekday=weekday)
        e.save()

        name = class_names['VC']
        code = "VC"
        type = "C"
        start = time(10, 15)
        end = time(11, 45)
        weekday = 5
        e = Event(name=name, code=code, type=type, start=start, end=end, weekday=weekday)
        e.save()

        #1ST YEAR CLASS SCHEDULE
        class_names = [('TG', 'Triune God'), ('BCI', 'Body of Christ I'), ('ECI', "Experience of Christ as Life I")]
        i = 1
        type = "C"
        for code, name in class_names:
            start = time(10, 15)
            end = time(11, 30)
            i += 1
            # Skip Wed
            if i == 2:
                continue
            weekday = i
            e = Event(name=name, code=code, type=type, start=start, end=end, weekday=weekday)
            e.save()

        class_names = {'CY': "Children's and Young People's Work"}
        name = class_names['CY']
        code = "CY"
        type = "C"
        start = time(8, 25)
        end = time(10, 0)
        weekday = 5
        e = Event(name=name, code=code, type=type, start=start, end=end, weekday=weekday)
        e.save()

        #2ND YEAR CLASS SCHEDULE
        class_names = [('BC2', 'Body of Christ II'), ('LS', 'Life of Service'), ('EC2', 'Experience of Christ as Life II')]

        #1ST YEAR GREEK SCHEDULE
        for i in [1, 3]:
            name = "Greek I"
            code = "GK I"
            type = "C"
            start = time(16, 45)
            end = time(17, 45)
            weekday = i
            e = Event(name=name, code=code, type=type, start=start, end=end, weekday=weekday)
            e.save()

        #OCC TEAM SCHEDULE



    def handle(self, *args, **options):
        self._create_events()