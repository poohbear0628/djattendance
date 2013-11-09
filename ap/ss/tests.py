"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from ss.models import *


class SimpleTest(TestCase):
    def test(self):
        sc = Scheduler()
        sc.getInstancesOrderByTime()
