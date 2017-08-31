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
#   - this script tests API functions 
#-----------------------------------------------------------------------------

from autotools import djattendance_test_api as api

with open("data/test_inputdata.json") as data_file:
    data = api.json.load(data_file)
    data = data["web_access_requests"]

#testname = "WebAccessRequestsTest"
testname = "Test_API_Functionalities"

class DjattendanceAutomation(api.unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print "setUpClass"
        api.initialize_test(testname)

    def setUp(self):
        print "setUp"

    @api.unittest.skip("skipping")
    def test_001_log_in(self):
        try:
            #import pdb; pdb.set_trace()
            api.login("joon.jo@gmail.com", "ap", 3)
        except Exception as e:
            api.handle_exception(e)

    """ note: if want to skip the test, enable skip() """
    @api.unittest.skip("skipping")
    def test_002_verify_element_text(self):
        try:
            print "welcome:         ", api.get_element_text("id", "content")
            print "panel-title:     ", api.get_element_text("class", "panel-title")
        except Exception as e:    
            api.handle_exception(e)

    @api.unittest.skip("skipping")
    def test_003_verify_javascript_execution(self):
        try:
            """ synchronous execution """
            # expect string output 
            script = "document.URL"
            print "Page URL(sync):    ", api.execute_javascript(script)

            # toggle the bage in the home page 
            script = "document.getElementsByClassName('badge')[0].click()"
            api.execute_javascript(script)
            api.time.sleep(1)
            api.execute_javascript(script)
            api.time.sleep(1)

            # the same operation as above, but return the actual web element
            script = "document.getElementsByClassName('badge')"
            api.execute_javascript(script)[0].click()
            api.time.sleep(1)
            api.execute_javascript(script)[0].click()
            api.time.sleep(1)
        except Exception as e:    
            api.handle_exception(e)

    @api.unittest.skip("skipping")
    def test_004_verify_focusing_element(self):
        try:
            api.select_dropdown_menu("text", "Misc.", "Bible Reading Tracker", 2)
            api.wait_for("link", "1st Year")
            api.click_element("text", "1st Year", 1)
            api.get_element_focused("id", "38", 1)              # Malachi
            api.get_element_focused("class", "navbar-brand", 1) # FTTA logo  
        except Exception as e:    
            api.handle_exception(e)

    @api.unittest.skip("skipping")
    def test_005_verify_week_selection(self):
        try:
            # import pdb; pdb.set_trace()
            api.select_dropdown_menu("text", "Misc.", "Bible Reading Tracker", 2)
            api.wait_for("link", "Daily")
            api.select_dropdown_menu("id", "select_menu", "3", 2)
            # api.select_dropdown_menu("id", "select_menu", "6", 2)
        except Exception as e:    
            api.handle_exception(e)

    @api.unittest.skip("skipping")
    def test_006_verify_moving_browser(self):
        try:
            # import pdb; pdb.set_trace()
            api.driver.get("https://www.ftta.org")
            api.time.sleep(2)
            api.browser_back_and_forward("back", "class", "navbar-brand")
            api.time.sleep(2)
            api.browser_back_and_forward("forward", "xpath", '//*[@src="/img/logo-lsm-ftta-title.png"]')
            api.time.sleep(2)
            api.browser_back_and_forward("back", "class", "navbar-brand")
            api.time.sleep(2)

        except Exception as e:    
            api.handle_exception(e)

    @api.unittest.skip("skipping")
    def test_007_verify_search_and_select(self):
        try:
            # test with group leave slip 
            api.select_dropdown_menu("text", "Attendance", "Personal Attendance", 2)
            api.discard_message_server_used(2)
            api.click_element("id", "noanim-tab-example-tab-3", 5)
            # api.debug()
            api.search_and_select("name", "trainees", "Joon", "Joon Jo", 2)
            api.search_and_select("name", "trainees", "Matt", "Matt Martin", 2)

            # test with e-shepherding
            api.select_dropdown_menu("text", "Requests", "Web Access Requests", 2)
            api.click_element("text", "Create e-shepherding request", 2)
            # api.debug()
            api.search_and_select("class", "select2-chosen", "Matt", "Matt Martin", 2)

        except Exception as e:    
            api.handle_exception(e)

    # @api.unittest.skip("skipping")
    def test_008_verify_context_click(self):
        try:
            # api.debug()
            api.driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
            api.time.sleep(5)
            api.element_context_click("CSS", ".context-menu-one.btn.btn-neutral", \
                                      "xpath", "//*[text()='Edit']", 10)

        except Exception as e:    
            api.handle_exception(e)

    def tearDown(self):
        print "tearDown"

    @classmethod
    def tearDownClass(cls):
        print "tearDownClass"
        api.finalize_test()


if __name__ == '__main__':
    suite = api.unittest.TestLoader().loadTestsFromTestCase(DjattendanceAutomation)

    """ set the format parameter as 'text' to print out the results to console """
    api.generate_report(suite, testname, 'text')

