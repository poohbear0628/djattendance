#!/usr/bin/env python2.7

#--------------------------------------------------------------------
# 
# Title: web_access_request.py
#
# Purpose: test cases for "Web Access Requests" of Django server
#
#--------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from autotools import djattendance_test_api as api
from autotools import HTMLTestRunner
from datetime import datetime, timedelta
from optparse import OptionParser
import time, unittest, os, json

with open("data/login.json") as data_file:
    server = json.load(data_file)

with open("data/test_inputdata.json") as data_file:
    data = json.load(data_file)
    data = data["web_access_requests"]

testname = "WebAccessRequestsTest"
chromedriver = "../chromedriver"
current_date = datetime.now()

# option in command line
parser = OptionParser()
parser.add_option("-d", "--driver", action="store", dest="drivername")
parser.add_option("-u", "--url", action="store", dest="urlname")
(options, args) = parser.parse_args()
# parsing the web browser testing option
if options.drivername == "chrome": WebDriver = webdriver.Chrome(chromedriver)
else: WebDriver = webdriver.Firefox()

# parsing the URL option
if options.urlname: urladdress = options.url
else: urladdress = server["domain"]

class DjattendanceAutomation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global WebDriver
        cls.driver = WebDriver

    def setUp(self):
        print "setUp"

    def test_001_get_domain(self):
        try:
            self.driver.get(server["domain"])
            self.driver.maximize_window()
            time.sleep(3)
        except Exception as e:
            print e
            raise Exception("Cannot open URL: ", e)
        #self.assertEqual(self.widget.size(), (50,50), 'incorrect default size')

    #@unittest.skip("skipping")
    def test_002_log_in(self):
        try:
            api.send_text_by_tag_name(self.driver, "username", server["username"])
            api.send_text_by_tag_name(self.driver, "password", server["password"], True)
        except Exception as e:    
            print e
            raise Exception("Login failed: ", e)            

    #@unittest.skip("skipping")
    def test_003_menu_web_access_requests(self):
        try:
            temp = data["default_page"]            
            api.click_element_by_xpath(self.driver, temp["menu_xpath"])
            time.sleep(1)
        except Exception as e:
            print e
            raise Exception("Cannot click on: ", e)

    #@unittest.skip("skipping")
    def test_004_check_title(self):
        try:
            temp = data["default_page"]
            res = api.get_element_attribute_by_xpath(self.driver, temp["titleXpath"], "textContent")
            #print "title: %s" % res
            if res == "undefined": res = api.get_element_attribute_by_xpath(self.driver, temp["titleXpath"], "innerHTML")
            self.assertEqual(res, temp["title"])
            time.sleep(1)
        except Exception as e:
            print e
            raise Exception("Two titles not equal: %s(web), %s(json)" % (res, temp["title"]), e)

    #@unittest.skip("skipping")
    def test_005_verify_creating_new_request(self):
        try:
            # click on the menu
            temp = data["request_page"]            
            api.click_element_by_text(self.driver, data["default_page"]["create"])
            api.click_element_by_id(self.driver, temp["reason_id"])
            api.click_element_by_text(self.driver, temp["reason"])
            api.click_element_by_id(self.driver, temp["minutes_id"])
            api.click_element_by_text(self.driver, temp["minutes"])

            # get the current time and +1 day
            req_date = datetime.strftime(current_date + timedelta(days=1), "%m/%d/%Y")
            api.click_element_by_id(self.driver, temp["expire_id"])
            api.send_text_by_tag_name(self.driver, temp["expire_tag"], req_date)

            # send comments
            api.click_element_by_id(self.driver, temp["comment_id"])
            api.send_text_by_tag_name(self.driver, temp["comment_tag"], temp["comment"])

            # mark as urgent 
            api.click_element_by_id(self.driver, temp["urgent_id"])

            # submit
            api.click_element_by_xpath(self.driver, temp["submit_xpath"])

            time.sleep(1)
        except Exception as e:
            print e
            raise Exception("Web Access Request page error: ", e)

    #@unittest.skip("skipping")
    def test_006_verify_submitted_request(self):        
        try:
            temp = data["default_page"]
            api.click_element_by_xpath(self.driver, temp["menu_xpath"])
            api.click_element_by_xpath(self.driver, temp["requested_xpath"])
            
            date = '{dt:%b}. {dt.day}, {dt.year}'.format(dt=current_date  + timedelta(days=1))
            request_dict = {
                "Status:": "Pending",
                "Reason:": "Fellowship",
                "Minutes:": "90",
                "Expires on:": date,
                "Comments:": data["request_page"]["comment"],
                "TA comments:": "None"
            }

            # get the list of value and examine it
            res = api.get_element_text_by_clsname(self.driver, "table").splitlines()
            for i, item in enumerate(res):                
                if ':' in item: # table key contains ":"
                    item = item.lstrip().rstrip()
                    #print res[i+1], request_dict[item] #debugging
                    self.assertEqual(res[i+1].lstrip().rstrip(), request_dict[item])
           
            time.sleep(1)
        except Exception as e:
            print e
            raise Exception("Error in submitted form ", e)

    #@unittest.skip("skipping")
    def test_007_delete_submitted_request(self):        
        try:
            temp = data["delete"]
            api.click_element_by_xpath(self.driver, data["default_page"]["menu_xpath"])
            api.click_element_by_xpath(self.driver, temp["delete_xpath"])
            api.click_element_by_xpath(self.driver, temp["delete_confirm"])

            time.sleep(1)
        except Exception as e:
            print e
            raise Exception("Error in deleting: ", e)

    def test_008_verify_request_deleted(self):        
        try:
            temp = data["default_page"]
            api.click_element_by_xpath(self.driver, temp["menu_xpath"])            
            res = api.is_element_visible(self.driver, temp["requested_xpath"])
            self.assertEqual(False, res)

            # testing purpose - DO NOT DELETE
            #wait = WebDriverWait(self.driver, 3)
            #elem = wait.until_not(EC.element_to_be_clickable((By.XPATH, xpath)))
            
            time.sleep(1)
        except Exception as e:
            print e
            raise Exception("Error in verifying deleted request: ", e)

    def tearDown(self):
        print "tearDown"

    @classmethod
    def tearDownClass(cls):
        print "test done"
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    # output to a file
    if not os.path.exists('reports'): os.mkdir('reports')

    suite = unittest.TestLoader().loadTestsFromTestCase(DjattendanceAutomation)
    #test_time = datetime.strftime(datetime.now(), '%Y-%m-%d_%H:%M:%S')
    #test_report = 'reports/' + testname + '_' + test_time + '_.html'

    test_report = 'reports/' + testname + '.html'
    fp = file(test_report, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title=testname,
                description='This demonstrates the report output by HTMLTestRunner.'
                )

    # run the test
    runner.run(suite)

    # output result on console for debugging
    #unittest.TextTestRunner(verbosity=2).run(suite)
    
    # close output file
    fp.close()


