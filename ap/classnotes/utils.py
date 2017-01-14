from datetime import datetime, date

from django.db import models

from .models import Classnotes, Classnotes_Tracker
from attendance.models import Roll
from attendance.utils import Period
from leaveslips.models import IndividualSlip, GroupSlip
from terms.models import Term
from accounts.models import Trainee
from classes.models import Class

def approve_classnotes(classnotes):
	'''
		Changes the status of Classnotes to 'approve'
		Decrement classnotes_owed count; 
		decrement absence_counts if classnotes type is R
	'''
	classnotes.status = 'A'
	classnotes.save()

	tracker = Classnotes_Tracker.objects.get(trainee=classnotes.trainee)
	clname = classnotes.classname
	tracker.classnotes_owed[clname] = str(int(tracker.classnotes_owed[clname]) - 1)
	tracker.save()

def assign_classnotes(period):
	for trainee in Trainee.objects.filter(is_active=True).all():
		assign_individual_classnotes(trainee, period)

def assign_individual_classnotes(trainee, period):
	'''
		Assign Classnotes based on class absences
		- Any special leave of absence (eg. interviews, wedding): 
			1 class notes / absence
		- Sickness & Unexcused absences & Others:
			1 class notes the number of absence >= 3
	'''
	# look at trainee's absences (for class event).
	# Increment absence_counts based on classname (HStore)
	tracker = Classnotes_Tracker.objects.filter(trainee=trainee).first()
	if not tracker:
		tracker = Classnotes_Tracker(trainee=trainee, absence_counts={}, \
			classnotes_owed={})

	for roll in trainee.rolls.all():
		current_term = Term.current_term()
		start = models.DateField(2016, 8, 22)
		end = models.DateField(2016, 12, 31)
		# if roll.date >= start and \
		# 	roll.date <= end:
		if roll.date >= Period(current_term).start(period) and \
			roll.date <= Period(current_term).end(period):
	    # if roll.event.date() > tracker.date_assigned \
	    # 	and roll.event.date() <= date.today():
			if roll.status == 'A' and roll.event.type == 'C':
				classname = roll.event.name
				if classname in tracker.absence_counts:
					tracker.absence_counts[classname] = str(int(tracker.absence_counts[classname]) + 1)
				else:
					tracker.absence_counts[classname] = '1'

				leavesliplist = get_leaveslip(trainee, roll)		            
				if leavesliplist:
					for leaveslip in leavesliplist:
						# Special: Wedding, Graduation, Funeral, etc.
						if leaveslip.type == 'FWSHP' or leaveslip.type == 'FUNRL' or \
            				leaveslip.type == 'INTVW' or leaveslip.type == 'GRAD' or \
            				leaveslip.type == 'WED':
							generate_classnotes(trainee, roll, tracker, 'S')

						# Regular: Sickness, Unexcused, Others, Fellowship, Notif only
						if leaveslip.type == 'OTHER' or leaveslip.type == 'SICK' or leaveslip.type == 'FWSHP' \
							or leaveslip.type == 'SPECL' or leaveslip.type == 'NOTIF':
							if classname in tracker.absence_counts:
								tracker.absence_counts[classname] = str(int(tracker.absence_counts[classname]) + 1)

							else:
								tracker.absence_counts[classname] = '1'
							if int(tracker.absence_counts[classname]) > 2:
								generate_classnotes(trainee, roll, tracker, 'R')
				else:
					# no leaveslip -> unexcused absence
					if classname in tracker.absence_counts:
						tracker.absence_counts[classname] = str(int(tracker.absence_counts[classname]) + 1)
					else:
						tracker.absence_counts[classname] = '1'
					if int(tracker.absence_counts[classname]) > 2:
						generate_classnotes(trainee, roll, tracker, 'R')

	tracker.date_assigned = date.today()
	tracker.save()

def get_leaveslip(trainee, roll):
	leavesliplist = None # potential for multiple leaveslips to a single role
	qset = IndividualSlip.objects.filter(trainee=trainee, status='A')
	if qset:
		for leaveslip in qset:
			if roll in leaveslip.rolls.all():
				leavesliplist.add(leaveslip)
	
	qset = GroupSlip.objects.filter(trainee=trainee, status='A')
	if qset:
		for leaveslip in qset:
			if roll in leaveslip.rolls.all():
				leavesliplist.add(leaveslip)

	return leavesliplist

def generate_classnotes(trainee, roll, tracker, type):
	trainee_class = Class.objects.filter(name=roll.event.name).first()
	classname = trainee_class.name
	if not Classnotes.objects.filter(trainee=trainee, classname=trainee_class, \
									classdate=roll.date).first():
		classnotes = Classnotes(trainee=trainee, classname=trainee_class, \
								classdate=roll.date, date_assigned=date.today(), \
								type=type, content='')
		if classname in tracker.classnotes_owed:
			tracker.classnotes_owed[classname] = str(int(tracker.classnotes_owed[classname]) + 1)
		else:
			tracker.classnotes_owed[classname] = '1'
		if type == 'R':
			tracker.absence_counts[classname] = str(int(tracker.absence_counts[classname]) - 1)
	else:
		classnotes = Classnotes.objects.get(trainee=trainee, classname=trainee_class, \
											classdate=roll.date)
		# In the case of multiple leave slips for one absence,
		# special case has a higher priority.
		if classnotes.type == 'R' and type == 'S':
			classnotes.type = type
			tracker.absence_counts[classname] = str(int(tracker.absence_counts[classname]) + 1)

	classnotes.save()
	tracker.save()