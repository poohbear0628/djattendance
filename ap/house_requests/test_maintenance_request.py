"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
testname = "TestCreateMaintenanceRequest"

import sys
from django.test import override_settings
from django.test import LiveServerTestCase
from djtests import djattendance_test_api
from django.db import models
from terms.models import Term
from schedules.models import Event
from accounts.models import User
from accounts.models import Trainee
from accounts.models import APUserManager
import datetime
from datetime import date, time
from schedules.constants import WEEKDAYS
from django.contrib.auth.models import Group

#@override_settings(ROOT_URLCONF = 'ap.ap.urls')
class TestCreateMaintenanceRequest(LiveServerTestCase):
  def setUp(self):
  	term = Term.objects.create(current=True, season='Fall', year=2017, start=datetime.date(2017, 8, 14), end=datetime.date(2017, 12, 30))
  	fmoc_class = Event.objects.create(type='C', name='Full Ministry of Christ', code='FMoC', av_code='FM', class_type='MAIN', monitor='AM', start=datetime.time(8, 25), end=datetime.time(10, 00), weekday=1)
  	trainee = Trainee(email='kevin.y.sung@gmail.com',firstname='Kevin', lastname='Sung', gender='B', type='R', date_of_birth='1993-1-19', current_term=3, is_active=True, is_staff=True, is_admin=True)
  	ta = User(is_active=True, email='jeromekeh@lsm.com', firstname='Jerome', lastname='Keh', type='T', date_of_birth='1983-11-15', is_staff=True, is_admin=True)
  	trainee.set_password('ap')
  	trainee.save()
  	ta.set_password('ap')
  	ta.save()

  def test_create_maintenance_request(self):
    """
    Test create a maintenance request
    """
    djattendance_test_api.initialize_test(testname, drivername="chrome", email="kevin.y.sung@gmail.com", password="ap")
    djattendance_test_api.go_to_login_page('%s%s' % (self.live_server_url, '/accounts/login/'))
    try:
      djattendance_test_api.log_into_account(djattendance_test_api.auto.get_email(), djattendance_test_api.auto.get_password())
    except Exception as e:
      djattendance_test_api.handle_exception(e)
      djattendance_test_api.time.sleep(2)
    djattendance_test_api.click_element("text", "Requests")
    djattendance_test_api.click_element("text", "Manage maintenance requests", 2)
    djattendance_test_api.click_element("text", "Create new maintenance request", 2)
    djattendance_test_api.click_element("id", "id_house")
    djattendance_test_api.click_element("xpath", "//option[@value='2']")
    djattendance_test_api.click_element("id", "id_request_type")
    djattendance_test_api.click_element("xpath", "//option[@value='AIR']")
    djattendance_test_api.send_text("id", "id_description", "Lord grant us a heavenly atmosphere!")
    djattendance_test_api.click_element("id", "id_urgent")
    djattendance_test_api.click_element("xpath", "//button[@type='submit']")
