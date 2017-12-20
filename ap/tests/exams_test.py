#!/usr/bin/env python2.7

#-----------------------------------------------------------------------------
# 
# How to run a script 
#   - you can run the script with different webdrivers
#     (refer comments in 'api.initialize_test()' )
#     (eg. python script.py -d chrome -u localhost:8000)
#
#   - -u or --url option cannot take the actual IP address.
#      Hence, use site name and port
#     (ex. -u localhost:8000, not -u 127.0.0.1:8000)
#
#-----------------------------------------------------------------------------
testname = "ExamsTest"


import djattendance_test_api as api
#import django; django.setup()
#import os
#import sys
#sys.path.append('/../../ap/exams/')
#import Exam
#dir_path = os.path.dirname(os.path.realpath(__file__)).replace("/selenium/automation", "/ap")
#print "dir_path is: " + dir_path
#sys.path.append(dir_path)

#import Exam
#from django.contrib.postgres.fields import HStoreField

from django.db import models
from django.utils.timezone import timedelta
#from ..exams.models import Exam
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__))))
from exams.models import Exam
#from models import Exam
#from terms.models import Term
#from exams.models import Exam
#from django.db.models import Exam


inputdata = "data/" + testname + ".json"
with open(inputdata) as data_file:
    data = api.json.load(data_file)
    request = data["request_page"]
    response = data["response_page"]

class DjattendanceAutomation(api.unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print "setUpClass"
        api.initialize_test(testname)

    def setUp(self):
        print "setUp"

    # @api.unittest.skip("skipping")
    #def test_001_log_in(self):
    #    try:
    #        api.login(1)
    #        api.time.sleep(3)
    #    except Exception as e:
    #        api.handle_exception(e)

    #def test_002_login_ta_account(self):
    #    try:
    #        api.click_element("xpath", "//div[@id='navbar-collapse-1']/ul/li/a/span")
    #        api.time.sleep(1)
    #        api.click_element("text", "Logout")
    #        api.wait_for("link", data["guess_access_title"], "clickable")
    #        api.log_into_account(api.auto.get_taemail(), api.auto.get_tapassword())
            #api.wait_for("link", data["main_menu"], "clickable")
    #    except Exception as e:
    #        api.handle_exception(e)

    def test_001_create_exam(self):
        print str(models.Exam.objects.all())
        #Exam.objects.create(pk=1, training_class=c,description='hi',is_open='True', term=t, category='M',total_score=5)
        api.go_to_login_page()
        api.log_into_account(api.auto.get_taemail(), api.auto.get_tapassword())
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

        

    """
    def test_004_login_back_to_trainee(self):
        try:
            api.click_element("xpath", "//div[@id='navbar-collapse-1']/ul/li/a/span")
            api.time.sleep(1)
            api.click_element("text", "Logout")
            api.wait_for("link", data["guess_access_title"], "clickable")
            api.log_into_account(api.auto.get_email(), api.auto.get_password())
        except Exception as e:
            api.handle_exception(e)
        api.time.sleep(2)

    def test_005_take_exam(self):
        api.click_element("text", "Current")
        api.click_element("text", "Take Exam", 2)
        api.click_element("text", "Take exam", 2)
        checkboxes = api.get_list_elements("xpath", "//input[@name='1']")
        api.click_on_element(checkboxes[0])
        api.send_text("id", "response-1", "Christ's Full Ministry is awesome!")
        api.select_from_dropdown_adv("name", "matching_answer_field","John 1:14")
        #api.click_element("name", "matching_answer_field", 1)
        #api.click_element("text", "John 1:14")
        api.click_element("value", "false")
        api.send_text("name", "fitb-textarea-1", "Cor")
        api.send_text("name", "fitb-textarea-2", "joined")
        api.send_text("name", "fitb-textarea-3", "soul")
        api.click_element("id", "save_button", 3)
        api.click_element("id", "finalize_button")
        #xpath=(//input[@id='tf_1'])[2] for FALSE
        api.time.sleep(2)


    def test_006_login_ta_account(self):
        try:
            api.click_element("xpath", "//div[@id='navbar-collapse-1']/ul/li/a/span")
            api.time.sleep(1)
            api.click_element("text", "Logout")
            api.wait_for("link", data["guess_access_title"], "clickable")
            api.log_into_account(api.auto.get_taemail(), api.auto.get_tapassword())
        except Exception as e:
            api.handle_exception(e)
        api.time.sleep(2)

    def test_007_grade_exam(self):
        api.click_element("text", "Exams")
        api.click_element("text", "Manage Exams", 2)
        api.click_element("text", "Enter scores", 2)
        api.click_element("text", "Grade Exam", 2)
        if not api.is_element_visible("Total Exam Score: 7.00/14.00; Percentage: 50.00%", "text"):
            raise Exception("Exam score not correct. Should be: '7.00/14.00' before TA grades the exam portion.") 
        if api.get_element_value("id", "score-1") != '3.00':
            raise Exception("Score for multiple choice not correct. Should be: '3.00'")
        if api.get_element_value("id", "score-2") != '0.00':
            raise Exception("Score for essay not correct. Should be: '0.00'")
        if api.get_element_value("id", "score-3") != '2.00':
            raise Exception("Score for matching not correct. Should be: '2.00'")
        if api.get_element_value("id", "score-4") != '0.00':
            raise Exception("Score for true false not correct. Should be: '0.00'")
        if api.get_element_value("id", "score-5") != '2.00':
            raise Exception("Score for fill in the blank not correct. Should be: '2.00'")
        api.send_text("id", "score-2", "5")
        api.click_element("text", "Finalize", 2)
        #api.click_element("name", "Submit", 2)

    def test_008_login_back_to_trainee(self):
        try:
            api.click_element("xpath", "//div[@id='navbar-collapse-1']/ul/li/a/span")
            api.time.sleep(1)
            api.click_element("text", "Logout")
            api.wait_for("link", data["guess_access_title"], "clickable")
            api.log_into_account(api.auto.get_email(), api.auto.get_password())
        except Exception as e:
            api.handle_exception(e)
        api.time.sleep(2)

    def test_009_check_exam_score(self):
        api.click_element("text", "Current")
        api.click_element("text", "Take Exam")
        api.click_element("text", "View graded exam")
        if not api.is_element_visible("Total Exam Score: 12.00/14.00; Percentage: 85.72%", "text"):
            raise Exception("Exam score not correct. Should be: '12.00/14.00; Percentage: 85.72%'") 
        
    def test_010_login_ta_account(self):
        try:
            api.click_element("xpath", "//div[@id='navbar-collapse-1']/ul/li/a/span")
            api.time.sleep(1)
            api.click_element("text", "Logout")
            api.wait_for("link", data["guess_access_title"], "clickable")
            api.log_into_account(api.auto.get_taemail(), api.auto.get_tapassword())
        except Exception as e:
            api.handle_exception(e)
        api.time.sleep(2)

    def test_011_check_statistics_exam(self):
        api.click_element("text", "Exams")
        api.click_element("text", "Manage Exams")
        api.click_element("text", "View statistics")
        if not api.is_element_visible("12.00", "text"):
            raise Exception("Exam statistics not correct. Should be: '12.00' based off one trainee's score") 
        
    def test_012_delete_exam(self):
        api.click_element("text", "Exams")
        api.click_element("text", "Manage Exams")
        api.click_element("CSS", "a.btn.btn-danger")
        api.click_element("CSS", "button.btn.btn-danger")
    """

if __name__ == '__main__':
    suite = api.unittest.TestLoader().loadTestsFromTestCase(DjattendanceAutomation)

    """ set the format parameter as 'text' to print out the results to console """
    api.generate_report(suite, testname, 'text')