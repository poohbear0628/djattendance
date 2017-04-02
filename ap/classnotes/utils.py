from datetime import datetime, date

from django.db import models

from .models import Classnotes
from attendance.models import Roll
from attendance.utils import Period
from leaveslips.models import IndividualSlip, GroupSlip
from terms.models import Term
from accounts.models import Trainee
from classes.models import Class


def assign_classnotes():

	trainee = Trainee.objects.get(pk=7)
	update_classnotes_list(trainee)
	assign_individual_classnotes(trainee)
	# for trainee in Trainee.objects.filter(is_active=True).all():
	#	update_classnotes_list(trainee)
	# 	assign_individual_classnotes(trainee)

def assign_individual_classnotes(trainee):
	'''
		Assign Classnotes based on class absences
		- Any special leave of absence (eg. interviews, wedding): 
			1 class notes / absence
		- Sickness & Unexcused absences & Others:
			1 class notes the number of absence >= 3
	'''
	# look at trainee's absences (for class event).
	# Increment absence_counts based on classname (HStore)
	regular_absence_counts = {}
	term = Term.current_term()
	rolls = trainee.rolls.all().filter(date__ge=term.start).filter(date__le=term.end)
	rolls = rolls.extra(order_by = ['date'])
	for roll in rolls:
		
		# TODO:
		# 1. count from the beginning of the term each time
		# 2. have to initialize the tracker
		# 3. get the actual number of classnotes object to know the actual
		#		regular classnotes a trainee has done
		# might not need the tracker object if we are counting from the beginning each time
		# just need a local variable
		print roll
		print roll.date
		if roll.status == 'A' and roll.event.type == 'C':
			classname = roll.event.name
			number_classnotes = calculate_number_classnotes(trainee, roll)
			leavesliplist = get_leaveslip(trainee, roll)
			print 'leaveslip list'
			print len(leavesliplist)
			print 'absence count'
			if classname in regular_absence_counts:
				print regular_absence_counts[classname]
			print 'number classnotes'
			print number_classnotes
			if leavesliplist:
				for leaveslip in leavesliplist:
					# Special: Wedding, Graduation, Funeral, etc.
					if leaveslip.type == 'FWSHP' or leaveslip.type == 'FUNRL' or \
        				leaveslip.type == 'INTVW' or leaveslip.type == 'GRAD' or \
        				leaveslip.type == 'WED':
						generate_classnotes(trainee, roll, 'S')

					# Regular: Sickness, Unexcused, Others, Fellowship, Notif only
					if leaveslip.type == 'OTHER' or leaveslip.type == 'SICK' or leaveslip.type == 'FWSHP' \
						or leaveslip.type == 'SPECL' or leaveslip.type == 'NOTIF':
						if classname in regular_absence_counts:
							regular_absence_counts[classname] += 1
							if (regular_absence_counts[classname] - number_classnotes) > 2:
								generate_classnotes(trainee, roll, 'R')
								regular_absence_counts[classname] -= 1
						else:
							regular_absence_counts[classname] = 1
					# Missed classes with conference or service leave slips results in no class notes
			else:
				# no leaveslip == unexcused absence
				if classname in regular_absence_counts:
					regular_absence_counts[classname] += 1
					if (regular_absence_counts[classname] - number_classnotes) > 2:
						generate_classnotes(trainee, roll, 'R')
						regular_absence_counts[classname] -= 1
				else:
					regular_absence_counts[classname] = 1

# Delete classnotes that are no longer needed based on changes
# made to the trainee's rolls (ie. the trainee was not absent in class)
def update_classnotes_list(trainee):
	classnotes_list = Classnotes.objects.filter(trainee=trainee, status ='U')
	if classnotes_list:
		for classnotes in classnotes_list:
			roll = Roll.objects.filter(trainee=trainee, event=classnotes.event, date=classnotes.date).first()
			if roll and not roll.status == 'A':
				classnotes.delete()
			if roll and roll.status == 'A':
				# check if there is an updated leaveslip for it
				# delete classnotes if the leaveslip is a conference or service
				leavesliplist = get_leaveslip(trainee, roll)
				if leavesliplist:
					for leaveslip in leavesliplist:
						if leaveslip.type == 'CONF' or leaveslip.type == 'SERV':
							classnotes.delete()
							break

def calculate_number_classnotes(trainee, roll):
	classnotes = Classnotes.objects.filter(trainee=trainee, event=roll.event, type='R')
	if not classnotes:
		return 0
	else:
		return len(classnotes)

def get_leaveslip(trainee, roll):
	leavesliplist = [] # potential for multiple leaveslips to a single role
	qset = IndividualSlip.objects.filter(trainee=trainee, status='A')
	if qset:
		for leaveslip in qset:
			if roll in leaveslip.rolls.all():
				leavesliplist.append(leaveslip)
	
	qset = GroupSlip.objects.filter(trainee=trainee, status='A')
	if qset:
		for leaveslip in qset:
			if roll in leaveslip.rolls.all():
				leavesliplist.append(leaveslip)

	return leavesliplist

def generate_classnotes(trainee, roll, type):
	classnotes = Classnotes.objects.filter(trainee=trainee, event=roll.event, \
				date=roll.date).first()
	if not classnotes:
		classnotes = Classnotes(trainee=trainee, event=roll.event, \
								date=roll.date, date_assigned=date.today(), \
								type=type, content='')
	else:
		# In the case of multiple leave slips for one absence,
		# special case has a higher priority.
		if classnotes.type == 'R' and type == 'S':
			classnotes.type = type
	classnotes.save()

def classnotes_owed(trainee):
	classnotes = Classnotes.objects.filter(trainee=trainee, status ='U')
	return len(classnotes)