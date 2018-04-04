from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from attendance.models import *
from schedules.models import *
from accounts.models import *
from terms.models import Term
from leaveslips.models import *
from datetime import *
import random
import pickle

def new_roll(trainees=[], am=[]):
    events = Event.objects.filter(type="C")
    status = ['P', 'A', 'T', 'U', 'L']
    for trainee in trainees:
        if trainee.gender == "B":
            cur_am = random.choice(am.filter(gender="B"))
        elif trainee.gender == "S":
            cur_am = random.choice(am.filter(gender="S"))
        for e in events:
            random.seed()
            week = Term.current_term().term_week_of_date(date.today())
            trainee_stat = random.choice(status)
            if trainee_stat == "P":
                Roll(event=e, trainee=trainee, status=random.choice(status), submitted_by=cur_am, date=Term.get_date(Term.current_term(), week, e.weekday)).save()
            elif trainee_stat == "A":
                Roll(event=e, trainee=trainee, status="A", submitted_by=cur_am, date=Term.get_date(Term.current_term(), week, e.weekday)).save()
            else:
                Roll(event=e, trainee=trainee, status=random.choice(['A', trainee_stat]), submitted_by=cur_am, date=Term.get_date(Term.current_term(), week, e.weekday)).save()

class Command(BaseCommand):
    # to use: python ap/manage.py populate_rolls --settings=ap.settings.dev
    def _create_rolls(self):
        # change the array below to get different trainees
        trainees = Trainee.objects.filter(current_term__gt=2)
        am = Trainee.objects.filter(groups__name="attendance_monitors")
        if not len(am):
          am_group = Group.objects.get(name='attendance_monitors')
          bro = Trainee.objects.filter(gender='B').order_by('?').first()
          sis = Trainee.objects.filter(gender='S').order_by('?').first()
          print('no attendance monitors found, selecting random brother {0} and sister {1}'.format(bro, sis))
          bro.groups.add(am_group)
          sis.groups.add(am_group)
        new_roll(trainees, am)

    def _check_rolls(self):
        total = 0
        fixed = 0
        AM = Trainee.objects.filter(groups__name="attendance_monitors")
        for t in Trainee.objects.all():
            t_exist = False
            for r in Roll.objects.filter(trainee=t):
                week, day = Term.current_term().reverse_date(r.date)
                exist = False
                for sch in t.active_schedules.filter(weeks__contains=week):
                    if r.event in sch.events.all():
                        exist = True

                if not exist and r.event:
                    # print t.full_name2
                    # attached_IS = IndividualSlip.objects.filter(trainee=t, rolls__in=[r])
                    # attached_GS = GroupSlip.objects.filter(trainees__in=[t])
                    # GS_exist = False
                    # for gs in attached_GS:
                    #     if r.event in gs.events:
                    #         GS_exist = True
                    # if not attached_IS and GS_exist:

                        total+=1
                        if r.submitted_by == t:
                            submit = 'themself'
                        elif r.submitted_by in AM:
                            submit = 'Attendance Monitor ' + r.submitted_by.full_name
                        elif r.submitted_by:
                            submit = r.submitted_by.full_name

                        if not t_exist:
                            if t.current_term > 2:
                                sa = 'in their 2nd year'
                            else:
                                sa = 'in their 1st year'

                            if t.self_attendance:
                                sa = sa + ' on self attendance'
                            else:
                                sa = sa + ' not on self attendance'
                            print t.full_name2, sa
                            t_exist = True
                        
                        print 'Roll ID', r.id, 'for', r.event.name,'with Event ID', r.event.pk, 'on', r.date, 'submitted by', submit
                    # else:

                        t_sch = t.active_schedules.filter(weeks__contains=week).order_by('priority')
                        update = False
                        for sch in list(reversed(t_sch)):
                            for ev in sch.events.all():
                                if ev.name == r.event.name and ev.weekday == r.event.weekday and not update:
                                    print 'Attached ID', r.event.id, 'Should be', ev.id
                                    r.event = ev
                                    r.save()
                                    update = True
                                    fixed+=1
                  
            if t_exist:
                print 
        print 'total', count
        print 'fixed', fixed
        print 'pulled on', datetime.now()
        
    def _check_present_rolls(self):
        print ('* Looking through rolls with present status and making sure they have a leaveslip attached')
        for r in Roll.objects.filter(status='P'):
            attached_IS = IndividualSlip.objects.filter(rolls__in=[r])
            if not attached_IS:
                print r.id, r, r.event

    def combine_rolls_with_leaveslip(self):
        print ('* Looking at rolls with present status whichs should be attached to a leaveslip, and a duplicate roll with a non-present status for the same event, date, and trainee. Combining them')
        for r in Roll.objects.filter(status='P'):
            same_roll = Roll.objects.filter(event=r.event, trainee=r.trainee, date=r.date).exclude(status='P')
            if same_roll.count() > 1:
                print r.id, r, "has more than one duplicate rolls"
            elif same_roll.count() == 1:
                dup_roll = same_roll.first()
                r.status = dup_roll.status
                r.submitted_by = dup_roll.submitted_by
                r.save()
                if dup_roll.leaveslips is None:
                    dup_roll.delete()
                else:
                    print dup_roll, "has a leaveslip attached"

    def handle(self, *args, **options):
        # print('* Populating rolls...')
        # self._create_rolls()
        # print ('* Looking through rolls...')
        # self._check_rolls()
        self._check_present_rolls()
        # self.combine_rolls_with_leaveslip()