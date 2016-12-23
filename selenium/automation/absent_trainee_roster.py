#!/usr/bin/env python2.7

#--------------------------------------------------------------------
# 
# Title: bible_reading_tracker.py
#
# Purpose: test cases for "Bible Reading Tracker" of Django server
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
from datetime import datetime
from optparse import OptionParser
import time, unittest, os, json, sys

with open("data/login.json") as data_file:
    server = json.load(data_file)

with open("data/test_inputdata.json") as data_file:
    data = json.load(data_file)
    data = data["absent_trainee"]

# name of the test and checking os version
testname = "AbsentTraineeRoster"
if sys.platform == 'darwin':
    chromedriver = "../chromedriver_mac"
elif sys.platform.startswith('linux'):
    chromedriver = "../chromedriver_linux"
else:
    print "You must run these scripts with mac or linux."
    exit()
profile = None

# option in command line
parser = OptionParser()
parser.add_option("-d", "--driver", action="store", dest="drivername")
parser.add_option("-u", "--url", action="store", dest="urlname")
(options, args) = parser.parse_args()
# parsing the URL option
if options.urlname:
    urladdress = options.urlname

    # if another URL used, then set the Firefox preference
    profile = webdriver.FirefoxProfile()
    profile.set_preference("xpinstall.signatures.required", False)
else: urladdress = server["domain"]

# parsing the web browser testing option and checking system os
if options.drivername == "chrome": WebDriver = webdriver.Chrome(chromedriver)
else: WebDriver = webdriver.Firefox(firefox_profile=profile)
#else: WebDriver = webdriver.Firefox()

class AbsentTraineeRoster(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()   

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
    def test_003_absent_trainee_roster(self):
        text = "Absent Trainee Roster"
        try:
            api.click_element_by_text(self.driver, text)
            time.sleep(1)
        except Exception as e:
            print e
            raise Exception("Cannot click on " + text + ": ", e)

    #@unittest.skip("skipping")
    def test_004_manual_trainee_entry(self):
        atxpath = "//*[@href='/absent_trainee_roster/absent_trainee_form/']"
        api.click_element_by_xpath(self.driver, atxpath)
        try:
            for xpath in data["click_xpath_absent_trainee"]:
                if "id" in xpath:
                    api.click_element_by_xpath(self.driver, xpath)
                else:
                    api.send_text_by_tag_name(self.driver, "form-0-comments", xpath)
        except Exception as e:
            print e
            raise Exception("Cannot select trainee or reason: ", e)

    #@unittest.skip("skipping")
    def test_005_add_multiple_trainees(self):
        try:
            # click on the menu
            api.click_element_by_text(self.driver, "Full-Time Training in Anaheim")
            text = "Absent Trainee Roster"
            api.click_element_by_text(self.driver, text)
            # update the daily reading assignment
            temp = data["trainee_array"]
            status = "btn-status active"
            for i, xpath in enumerate(temp):
                for item in xpath:
                    if "id" in str(item):
                        api.click_element_by_xpath(self.driver, item)
                    else:
                        print xpath[2]
                        api.send_text_by_tag_name(self.driver, "form-"+str(i)+"-comments", item)
                if i<len(temp)-1:
                    api.click_element_by_text(self.driver, "Add another trainee")
                    print "adding one", i
                    time.sleep(1)
            api.click_element_by_xpath(self.driver, data["save"])
                #val = api.get_element_attribute_by_xpath(self.driver, xpath, 'class')
                #print status in val
                #self.assertTrue(status in val, "%s is not clicked properly to be active" % xpath)
            # clean up the test scenario
        except Exception as e:
            print e
            raise Exception("Cannot select trainee or reason: ", e)

    #@unittest.skip("skipping")
    def test_006_delete_trainees(self):
        try:
            # remove the trainees
            temp = data["trainee_array"]
            delete = data["remove"]
            print delete
            status = "btn-status active"
            for i, xpath in enumerate(temp):
                print i, xpath[0]
                whichTrainee=xpath[0].split('/o')[0]+delete
                val = api.get_element_attribute_by_xpath(self.driver, whichTrainee, 'class')
                api.click_element_by_xpath(self.driver, whichTrainee)
            api.click_element_by_xpath(self.driver, data["save"])
        except Exception as e:
            print e
            raise Exception("Cannot delete the trainee: ", e)           

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

    suite = unittest.TestLoader().loadTestsFromTestCase(AbsentTraineeRoster)
    #test_time = datetime.strftime(datetime.now(), '%Y-%m-%d_%H:%M:%S')
    #test_report = 'reports/AbsentTraineeRosterTest_' + test_time + '_.html'

    test_report = 'reports/'+ testname + '.html'
    fp = file(test_report, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title='My unit test',
                description='This demonstrates the report output by HTMLTestRunner.'
                )

    # run the test
    runner.run(suite)

    # output result on console for debugging
    #unittest.TextTestRunner(verbosity=2).run(suite)
    fp.close()
