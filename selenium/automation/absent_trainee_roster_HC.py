#!/usr/bin/env python2.7

#--------------------------------------------------------------------
# 
# Title: absent_trainee_roster.py
#
# Purpose: test cases for "Absent Trainee Roster" of Django server
#          testing with the HC role instead of AP role
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
import time, unittest, os, json, sys, random

with open("data/login.json") as data_file:
    server = json.load(data_file)

with open("data/test_inputdata.json") as data_file:
    data = json.load(data_file)
    data = data["absent_trainee"]

# name of the test and checking os version
testname = "AbsentTraineeRosterHC"
if sys.platform == 'darwin':
    chromedriver = "../chromedriver_mac"
elif sys.platform.startswith('linux'):
    chromedriver = "../chromedriver_linux"
else:
    print "You must run these scripts with mac or linux."
    exit()
profile = None
atxpath = data["xpath"]
reasons = data["reasons"]
save = data["save"]

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

class AbsentTraineeRosterHC(unittest.TestCase):

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
    def test_002_login_hc_account(self):
        try:
            api.send_text_by_tag_name(self.driver, "username", data["hc_test"]["username"])
            api.send_text_by_tag_name(self.driver, "password", data["hc_test"]["password"], True)
            time.sleep(3)
        except Exception as e:
            print e
            raise Exception("Cannot login as an HC: ", e)

    #@unittest.skip("skipping")
    def test_003_check_number_in_house(self):
        try:
            api.click_element_by_xpath(self.driver, atxpath)
            res = api.get_element_text_by_clsname(self.driver, "form-control")
            traineelist = res.split("\n")[2:-1]
            self.assertTrue(len(traineelist)<15)
        except Exception as e:
            print e
            raise Exception("could not get the list of housemates", e)
            
    #@unittest.skip("skipping")
    def test_004_select_trainee_with_no_reason(self):
        try:
            api.click_element_by_xpath(self.driver, atxpath)
            res = api.get_element_text_by_clsname(self.driver, "form-control")
            traineelist = res.split("\n")[2:-1]
            print random.choice(traineelist)
            api.click_element_by_text(self.driver, random.choice(traineelist))
            api.click_element_by_xpath(self.driver, save)
            error = api.get_element_text_by_clsname(self.driver, "errorlist")
            print error
            self.assertTrue(error=="This field is required.")
        except Exception as e:
            print e
            raise Exception("could not select a trainee at random", e)

    #@unittest.skip("skipping")
    def test_005_add_a_reason(self):
        try:
            print random.choice(reasons)
            api.click_element_by_xpath(self.driver, random.choice(reasons))
            api.click_element_by_xpath(self.driver, save)
        except Exception as e:
            print e
            raise Exception("could not select a reason at random", e)
    
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

    suite = unittest.TestLoader().loadTestsFromTestCase(AbsentTraineeRosterHC)
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
    # unittest.TextTestRunner(verbosity=2).run(suite)
    fp.close()
