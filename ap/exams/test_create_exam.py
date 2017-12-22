"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
testname = "TestCreateExam"

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

@override_settings(ROOT_URLCONF = 'ap.ap.urls')
class TestCreateExam(LiveServerTestCase):
  def setUp(self):
  	term = Term.objects.create(current=True, season='Fall', year=2017, start=datetime.date(2017, 8, 14), end=datetime.date(2017, 12, 30))
  	fmoc_class = Event.objects.create(type='C', name='Full Ministry of Christ', code='FMoC', av_code='FM', class_type='MAIN', monitor='AM', start=datetime.time(8, 25), end=datetime.time(10, 00), weekday=1)
  	trainee = Trainee(email='kevin.y.sung@gmail.com',firstname='Kevin', lastname='Sung', gender='B', type='R', date_of_birth='1993-1-19', current_term=3, is_active=True, is_staff=True, is_admin=True)
  	ta = User(is_active=True, email='jeromekeh@lsm.com', firstname='Jerome', lastname='Keh', type='T', date_of_birth='1983-11-15', is_staff=True, is_admin=True)
  	trainee.set_password('ap')
  	trainee.save()
  	ta.set_password('ap')
  	ta.save()
  	
  def test_create_exam(self):
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

    api.click_element("text", "Exams")
    api.click_element("text", "Create Exam")
    api.time.sleep(2)
    api.send_text("id", "id_description", "This is a description/test...what more do you want?!")
    api.click_element("CSS", "label.btn.btn-default")
        
    #create five sections for the five types of questions
    api.click_element("value", "Add Section")
    api.click_element("value", "Add Section")
    api.click_element("value", "Add Section")
    api.click_element("value", "Add Section")
    api.click_element("value", "Add Section")
    sections = api.get_list_elements("name", "section_type")
    section_instructions = api.get_list_elements("name", "section_instructions")
    add_question_buttons = api.get_list_elements("class", "btnAddQuestion")        
    api.time.sleep(1)

    #Multiple choice create
    api.select_from_dropdown("value", sections[0], "MC")
    api.send_keys_to_element(section_instructions[0], "Multiple Choice Instructions")
    api.click_on_element(add_question_buttons[0])
    api.send_text("name", "question-point", "1", False)
    api.send_text("name", "question-prompt", "Which stage below is not part of Christ's Full Ministry?", False)
    api.click_element("text", "Add Choice")
    api.click_element("text", "Add Choice")
    api.click_element("text", "Add Choice")
    api.click_element("text", "Add Choice")
    checkboxes = api.get_list_elements("xpath", "//*[@type='checkbox']")
    api.send_text("name", "question-option-1", "Imperialism")
    api.send_text("name", "question-option-2", "Incarnation")
    api.send_text("name", "question-option-3", "Inclusion")
    api.send_text("name", "question-option-4", "Intensification")
    api.click_on_element(checkboxes[0])
    api.time.sleep(1)
        
    #Essay create
    api.select_from_dropdown("value", sections[1], "E")
    api.send_keys_to_element(section_instructions[1], "Essay Instructions")
    api.click_on_element(add_question_buttons[1])
    input_points_list = api.get_list_elements("name", "question-point")
    api.send_keys_to_element(input_points_list[1], "5")
    question_prompts = api.get_list_elements("name", "question-prompt")
    api.send_keys_to_element(question_prompts[1], "Explain Christ's full ministry")
    api.time.sleep(1)

    #Matching create
    api.select_from_dropdown("value", sections[2], "M")
    api.send_keys_to_element(section_instructions[2], "Matching Instructions")
    api.click_on_element(add_question_buttons[2])
    input_points_list = api.get_list_elements("name", "question-point")
    api.send_keys_to_element(input_points_list[2], "2")
    question_prompts = api.get_list_elements("name", "question-prompt")
    api.send_keys_to_element(question_prompts[2], "The Word became flesh")
    api.send_text("name", "question-match", "John 1:14")
    api.time.sleep(1)

    #True False Create
    api.select_from_dropdown("value", sections[3], "TF")
    api.send_keys_to_element(section_instructions[3], "True False Instructions")
    api.click_on_element(add_question_buttons[3])
    input_points_list = api.get_list_elements("name", "question-point")
    api.send_keys_to_element(input_points_list[3], "1")
    question_prompts = api.get_list_elements("name", "question-prompt")
    api.send_keys_to_element(question_prompts[3], "Christ's Full Ministry is in three stages.")
    api.click_element("xpath", "//div[@id='tf_0']/label")
    api.time.sleep(1)

    #Fill in the Blank Create
    api.select_from_dropdown("value", sections[4], "FB")
    api.send_keys_to_element(section_instructions[4], "Fill in the Blank Instructions")
    api.click_on_element(add_question_buttons[4])
    input_points_list = api.get_list_elements("name", "question-point")
    api.send_keys_to_element(input_points_list[4], "3")
    api.send_text("name", "question-point", "3", False)
    question_prompts = api.get_list_elements("name", "question-prompt")
    api.send_keys_to_element(question_prompts[4], "1 $1 6:17 But he who is $2 to the Lord is one $3", 1)
    add_buttons = api.get_list_elements("xpath", "//button[@type='button']")
    api.click_element("CSS", ".fitb-add-answer-button")
    api.click_element("CSS", ".fitb-add-answer-button")
    api.click_element("CSS", ".fitb-add-answer-button")
    api.send_text("name", "answer-text-1", "Cor")
    api.send_text("name", "answer-text-2", "joined")
    api.send_text("name", "answer-text-3", "spirit")
    api.click_element("id", "exam-submit", 3)
    api.time.sleep(1)
