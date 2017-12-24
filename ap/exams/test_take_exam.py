"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
testname = "TestTakeExam"

from django.test import TestCase, override_settings
from django.test import LiveServerTestCase
from tests import djattendance_test_api as api
from django.db import models
from django.utils.timezone import timedelta
from exams.models import Exam
from exams.models import Section
from terms.models import Term
from schedules.models import Event
from accounts.models import User
from accounts.models import Trainee
from accounts.models import APUserManager
import datetime
from datetime import timedelta, date, time
from schedules.constants import WEEKDAYS

#@override_settings(ROOT_URLCONF = 'ap.ap.urls')
class TestTakeExam(LiveServerTestCase):
  def setUp(self):
  	term = Term.objects.create(current=True, season='Fall', year=2017, start=datetime.date(2017, 8, 14), end=datetime.date(2017, 12, 30))
  	fmoc_class = Event.objects.create(type='C', name='Full Ministry of Christ', code='FMoC', av_code='FM', class_type='MAIN', monitor='AM', start=datetime.time(8, 25), end=datetime.time(10, 00), weekday=1)
  	trainee = Trainee(email='kevin.y.sung@gmail.com',firstname='Kevin', lastname='Sung', gender='B', type='R', date_of_birth='1993-1-19', current_term=3, is_active=True, is_staff=True, is_admin=True)
  	ta = User(is_active=True, email='jeromekeh@lsm.com', firstname='Jerome', lastname='Keh', type='T', date_of_birth='1983-11-15', is_staff=True, is_admin=True)
  	trainee.set_password('ap')
  	trainee.save()
  	ta.set_password('ap')
  	ta.save()
  	exam = Exam.objects.create(pk=1, training_class=fmoc_class,description='FMoC Midterm',is_open='True', term=term, category='M',total_score=5)
  	section_mc = Section.objects.create(exam=exam, section_type="MC", section_index=0, exam_id=1, questions={'0': '{"answer": "1", "points": 1, "prompt": "Who is Christ?", "options": "The Son of the living God;I don\'t know;Huh?;A prophet only;Jeremiah"}'}, first_question_index=1, id=1, question_count=1, instructions='mc instr')
  	section_essay = Section.objects.create(exam=exam, section_type="E", section_index=1, exam_id=1, questions={'0': '{"answer": "", "points": 5, "prompt": "What is the full ministry of Christ in its three stages?"}'}, first_question_index=1, id=2, question_count=1, instructions='essay instr')
  	section_matching = Section.objects.create(exam=exam, section_type="M", section_index=2, exam_id=1, questions={'0': '{"answer": "John 17:21", "points": 1, "prompt": "That they all may be one"}'}, id=3, question_count=1, instructions='match instr')
  	section_tf = Section.objects.create(exam=exam, section_type="TF", section_index=3, exam_id=1, questions={'0': '{"answer": "true", "points": 1, "prompt": "The Seven Spirits are Christ\'s Stage of Intensification"}'}, first_question_index=1, id=4, question_count=1, instructions='tf instr')
  	section_fitb = Section.objects.create(exam=exam, section_type="FB", section_index=4, exam_id=1, questions={'0': '{"answer": "joined;spirit", "points": 2, "prompt": "He who is $1 to the Lord is one $2"}'}, first_question_index=1, id=5, question_count=1, instructions='fitb instr')

  def test_take_exam(self):
    """
    Test taking an exam.
    """
    api.initialize_test(testname, drivername="chrome", email="kevin.y.sung@gmail.com", password="ap")
    api.go_to_login_page('%s%s' % (self.live_server_url, '/accounts/login/'))
    try:
      api.log_into_account(api.auto.get_email(), api.auto.get_password())
    except Exception as e:
      api.handle_exception(e)
      api.time.sleep(2)
    api.click_element("text", "Current")
    api.click_element("text", "Take Exam", 2)
    api.click_element("text", "Take exam", 2)
    checkboxes = api.get_list_elements("xpath", "//input[@name='1']")
    api.click_on_element(checkboxes[0])
    api.send_text("id", "response-1", "Christ's Full Ministry is awesome!")
    api.select_from_dropdown_adv("name", "matching_answer_field","John 17:21")
    api.click_element("value", "false")
    api.send_text("name", "fitb-textarea-1", "joined")
    api.send_text("name", "fitb-textarea-2", "soul")
    api.click_element("id", "save_button", 3)
    api.click_element("id", "finalize_button")
    api.time.sleep(2)
    if not api.is_element_visible("View graded responses", "text"):
    	raise Exception("Exam not able to be finalized. Should be able to see text: 'View graded responses'.") 
