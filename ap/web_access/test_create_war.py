"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
testname = "TestCreateWAR"

from django.test import override_settings
from django.test import LiveServerTestCase
from djtests import djattendance_test_api as api
from django.db import models
from web_access.models import WebRequest
from terms.models import Term
from schedules.models import Event
from accounts.models import User
from accounts.models import Trainee
from accounts.models import APUserManager
import datetime
from datetime import date, time, timedelta
from datetime import datetime as dt
from time import strftime
from schedules.constants import WEEKDAYS
from django.contrib.auth.models import Group

inputdata = "djtests/data/WebAccessRequestsTest.json"
with open(inputdata) as data_file:
  data = api.json.load(data_file)
  request = data["request_page"]
  response = data["response_page"]

#@override_settings(ROOT_URLCONF = 'ap.ap.urls')
class TestCreateWAR(LiveServerTestCase):
  def setUp(self):
  	term = Term.objects.create(current=True, season='Fall', year=2017, start=datetime.date(2017, 8, 14), end=datetime.date(2017, 12, 30))
  	trainee = Trainee(email='kevin.y.sung@gmail.com',firstname='Kevin', lastname='Sung', gender='B', type='R', date_of_birth='1993-1-19', current_term=3, is_active=True, is_staff=True, is_admin=True)
  	trainee.set_password('ap')
  	trainee.save()

  def test_create_war(self):
    """
    Test creating a web access request.
    """
    api.initialize_test(testname, drivername="chrome", email="kevin.y.sung@gmail.com", password="ap")
    api.go_to_login_page('%s%s' % (self.live_server_url, '/accounts/login/'))
    try:
      api.log_into_account(api.auto.get_email(), api.auto.get_password())
    except Exception as e:
      api.handle_exception(e)
      api.time.sleep(2)
    api.click_element("text", "Requests")
    api.click_element("text", "Web Access Requests", 2)
    # create four requests
    req_date = dt.strftime(datetime.datetime.now() + datetime.timedelta(days=1), "%m/%d/%Y")  # get the current time and +1 day
    for i in range(len(request["reason"])):
      api.click_element("text", "Create new web request", 2)
      api.click_element("value", request["reason_val"][i])
      api.get_element_focused("id", request["reason_id"])
      api.click_element("value", request["minutes"][i])
      api.get_element_focused("id", request["minutes_id"])
      api.send_text("id", request["expire_id"], req_date)
      # mark as urgent
      if i % 2 == 0:
        api.click_element("id", request["urgent_id"])
      api.send_text("id", request["comment_id"], request["comment"][i], True)
