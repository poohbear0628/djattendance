from seasonal_service_schedule import *
from service import *
from worker import *
from workergroup import *
from exception import *
from assignment import *
from week_schedule import *
from service_hours import *

""" services models.py

The services model defines both weekly and permanent (designated) services in the

Data Models:
    - Category: This is a broad category that contains specific services. For
    example,Cleanup is a category that contains services such as Tuesday
    Breakfast Cleanup or Saturday Lunch Cleanup. Guard contains Guards A, B, C,
    and D.

    - Service: This refers to a specific service that repeats on a weekly basis.
    I.e. Tuesday Breakfast Prep is a service. It repeats every week. A specific
    instance of that service is defined in the service scheduler module as a
    service Instance.

    - SeasonalServiceSchedule: This is a period in which services are active and generally
    changes with the schedule of the training. Most of the time, the regular
    FTTA schedule will be in effect, but there are exceptions such as Service
    Week and the semiannual training.
"""



"""

Worker Specs

 - gender
 - qualifications
 - WORKER_ROLE_TYPES
 - term_types
 - worker_group
 - count
 - workload

worker_group join


class Assignment(models.Model):

    ROLES = WORKER_ROLE_TYPES

    # schedule = models.ForeignKey('Schedule')
    instance = models.ForeignKey(Instance)
    worker = models.ForeignKey(Worker)
    role = models.CharField(max_length=3, choices=ROLES, default='wor')

"""
