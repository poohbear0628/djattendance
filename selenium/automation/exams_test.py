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


from autotools import djattendance_test_api as api
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
    def test_001_log_in(self):
        try:
            api.login(1)
            api.time.sleep(3)
        except Exception as e:
            api.handle_exception(e)

    def test_002_login_ta_account(self):
        try:
            api.click_element("CSS", data["logout_toggle"])
            api.click_element("xpath", data["logout_button"])
            api.wait_for("link", data["guess_access_title"], "clickable")
            api.log_into_account(api.auto.get_taemail(), api.auto.get_tapassword())
            api.wait_for("link", data["main_menu"], "clickable")
        except Exception as e:
            api.handle_exception(e)

    def test_003_create_exam(self):
    	api.click_element("text", "Exams")
    	api.click_element("text", "Create Exam")
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
        
        #Essay create
        api.select_from_dropdown("value", sections[1], "E")
        api.send_keys_to_element(section_instructions[1], "Essay Instructions")
        api.click_on_element(add_question_buttons[1])
        input_points_list = api.get_list_elements("name", "question-point")
        api.send_keys_to_element(input_points_list[1], "5")
        api.send_text("id", "E-question-template-blank", "Explain Christ's full ministry")
        
        #Matching create
        api.select_from_dropdown("value", sections[2], "M")
        api.send_keys_to_element(section_instructions[2], "Matching Instructions")
        api.click_on_element(add_question_buttons[2])
        input_points_list = api.get_list_elements("name", "question-point")
        api.send_keys_to_element(input_points_list[2], "2")
        api.send_text("id", "M-question-template-blank", "The Word became flesh")
        api.send_text("name", "question-match", "John 1:14")
        
        #True False Create
        api.select_from_dropdown("value", sections[3], "TF")
        api.send_keys_to_element(section_instructions[3], "True False Instructions")
        api.click_on_element(add_question_buttons[3])
        input_points_list = api.get_list_elements("name", "question-point")
        api.send_keys_to_element(input_points_list[3], "1")
        api.send_text("id", "TF-question-template-blank", "Christ's Full Ministry is in three stages")
        api.click_element("xpath", "//div[@id='tf_0']/label")
        
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

    def test_004_login_back_to_trainee(self):
        try:
            api.click_element("CSS", data["logout_toggle"])
            api.click_element("xpath", data["logout_button"])
            api.wait_for("link", data["guess_access_title"], "clickable")
            api.log_into_account(api.auto.get_email(), api.auto.get_password())
            api.wait_for("link", data["main_menu"], "clickable")
        except Exception as e:
            api.handle_exception(e)
        api.time.sleep(3)

    def test_005_take_exam(self):
        api.click_element("text", "Current")
        api.click_element("text", "Take Exam")
        api.click_element("text", "Take exam")
        api.click_element("name", "1")
        api.send_text("id", "response-1", "Christ's Full Ministry is awesome!")
        api.click_element("name", "matching_answer_field")
        api.click_element("text", "John 1:14")
        api.click_element("value", "false")
        api.send_text("name", "fitb-textarea-1", "Cor")
        api.send_text("name", "fitb-textarea-2", "joined")
        api.send_text("name", "fitb-textarea-3", "soul")
        api.click_element("id", "save_button", 3)
        api.click_element("id", "finalize_button")
        #xpath=(//input[@id='tf_1'])[2] for FALSE
        api.time.sleep(3)


    def test_006_login_ta_account(self):
        try:
            api.click_element("CSS", data["logout_toggle"])
            api.click_element("xpath", data["logout_button"])
            api.wait_for("link", data["guess_access_title"], "clickable")
            api.log_into_account(api.auto.get_taemail(), api.auto.get_tapassword())
            api.wait_for("link", data["main_menu"], "clickable")
        except Exception as e:
            api.handle_exception(e)
        api.time.sleep(3)

    def test_007_grade_exam(self):
        api.click_element("text", "Exams")
        api.click_element("text", "Manage Exams",3)
        api.click_element("text", "Enter scores",3)
        api.click_element("text", "Unfinalize Exam",3)
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
        api.click_element("name", "Submit", 2)

    def test_008_login_back_to_trainee(self):
        try:
            api.click_element("CSS", data["logout_toggle"])
            api.click_element("xpath", data["logout_button"])
            api.wait_for("link", data["guess_access_title"], "clickable")
            api.log_into_account(api.auto.get_email(), api.auto.get_password())
            api.wait_for("link", data["main_menu"], "clickable")
        except Exception as e:
            api.handle_exception(e)
        api.time.sleep(3)

    def test_009_check_exam_score(self):

        api.click_element("text", "Current")
        api.click_element("text", "Take Exam")
        api.click_element("text", "View graded exam")
        if not api.is_element_visible("Total Exam Score: 12.00/14.00; Percentage: 85.72%", "text"):
            raise Exception("Exam score not correct. Should be: '12.00/14.00; Percentage: 85.72%'") 
        
    def test_010_login_ta_account(self):
        try:
            api.click_element("CSS", data["logout_toggle"])
            api.click_element("xpath", data["logout_button"])
            api.wait_for("link", data["guess_access_title"], "clickable")
            api.log_into_account(api.auto.get_taemail(), api.auto.get_tapassword())
            api.wait_for("link", data["main_menu"], "clickable")
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
        

if __name__ == '__main__':
    suite = api.unittest.TestLoader().loadTestsFromTestCase(DjattendanceAutomation)

    """ set the format parameter as 'text' to print out the results to console """
    api.generate_report(suite, testname, 'text')