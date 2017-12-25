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
  	ta = User(is_active=True, email='jeromekeh@lsm.com', firstname='Jerome', lastname='Keh', type='T', date_of_birth='1983-11-15', is_staff=True, is_admin=True)
  	ta.set_password('ap')
  	ta.is_superuser=True
  	ta.save()
  	for i in range(len(request["reason"])):
  		WebRequest.objects.create(status='P', guest_name=None, trainee=trainee, time_started=None, urgent=True, comments=request["comment"][i], date_expire=(datetime.datetime.now() + timedelta(days=1)), reason=request["reason_val"][i], mac_address=None, minutes=request["minutes"][i], date_assigned=datetime.datetime.now(), TA_comments=None)

  def test_approve_war(self):
    """
    Test approving a web access request.
    """
    api.initialize_test(testname, drivername="chrome", email="jeromekeh@lsm.com", password="ap")
    api.go_to_login_page('%s%s' % (self.live_server_url, '/accounts/login/'))
    try:
      api.log_into_account(api.auto.get_email(), api.auto.get_password())
    except Exception as e:
      api.handle_exception(e)
      api.time.sleep(2)
    api.select_dropdown_menu("text", data["main_menu"], data["sub_menu"], 1)
    req_date = '{dt:%b}. {dt.day}, {dt.year}'.format(dt=api.auto.get_current_date() + timedelta(days=1))
    request_table = {}
    # verify each content
    for i in range(len(request["reason"])):
      api.click_element("xpath", "//*[@class='panel-heading']//*[contains(text(),'" + request["reason"][i] + "')]")
      api.wait_for("text", response["heading"])
      request_table["Status:"] = response["status_org"]
      request_table["Reason:"] = request["reason"][i]
      request_table["Minutes:"] = request["minutes"][i]
      request_table["Expires on:"] = req_date
      request_table["Comments:"] = request["comment"][i]
      request_table["TA comments:"] = response["ta_comment_org"]
      if i % 2 == 0:
        request_table["Urgent:"] = "True"
      else:
        request_table["Urgent:"] = "False"
      # get the list of value and examine it
      res = api.get_element_text("class", "table").splitlines()
      # print "request_table[web_access]: ", res # debug

      for j, item in enumerate(res):
        if ':' in item:  # table key contains ":"
          item = item.lstrip().rstrip()
          # print res[j+1].lstrip().rstrip(), request_table[item] # debug
          self.assertEqual(res[j + 1].lstrip().rstrip(), request_table[item])

      api.browser_back_and_forward("back", "text", data["default_page"]["title"])

      # mark the request
      ta_response = "//*[@class='panel-heading']//*[contains(text(), '" + request["reason"][i]
      ta_response += "')]/../..//*[@title='" + response["status_title"][i] + "']"
      api.click_element("xpath", ta_response)
      if response["status_title"][i] == "Comment":
        api.send_text("name", response["ta_comment_tag"], response["ta_comment_res"], True)

    api.wait_for_brand()
