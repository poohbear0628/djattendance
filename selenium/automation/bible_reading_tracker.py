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
import time, unittest, os, json

with open("data/login.json") as data_file:
    server = json.load(data_file)

with open("data/test_inputdata.json") as data_file:
    data = json.load(data_file)
    data = data["bible_reading_tracker"]

# name of the test
testname = "BibleReadingTracker"
chromedriver = "../chromedriver"

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
            self.driver.get(urladdress)
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
    def test_003_bible_reading_tracker(self):
        text = "Bible Reading Tracker"
        try:
            api.click_element_by_text(self.driver, text)
            time.sleep(1)
        except Exception as e:
            print e
            raise Exception("Cannot click on " + text + ": ", e)

    #@unittest.skip("skipping")
    def test_004_select_bible_reading(self):
        try:
            for xpath in data["click_xpath_daily_read"]:
                api.click_element_by_xpath(self.driver, xpath)

            time.sleep(1)
        except Exception as e:
            print e
            raise Exception("Cannot change the reading record: ", e)

    #@unittest.skip("skipping")
    def test_005_verify_bible_reading_update(self):
        try:
            # click on the menu
            api.click_element_by_text(self.driver, "Full-Time Training in Anaheim")
            text = "Bible Reading Tracker"
            api.click_element_by_text(self.driver, text)

            # update the daily reading assignment
            temp = data["click_xpath_daily_read"]
            api.click_element_by_xpath(self.driver, temp[0])
            #status = "btn-status active"
            status = "test failure"
            for xpath in temp[1:8]:
                val = api.get_element_attribute_by_xpath(self.driver, xpath, 'class')
                #print status in val
                self.assertTrue(status in val, "%s is not clicked properly to be active" % xpath)

            # clean up the test scenario 
            for xpath in temp[1:8]:
                xpath = xpath.split('/label')[0] + '/label[3]'
                api.click_element_by_xpath(self.driver, xpath)
                val = api.get_element_attribute_by_xpath(self.driver, xpath, 'class')
            api.click_element_by_xpath(self.driver, temp[8])

            time.sleep(1)
        except Exception as e:
            print e
            raise Exception("Cannot click on ", e)

    def test_006_select_1stYear_reading(self):        
        try:
            temp = data["1st_year_reading"]
            api.click_element_by_text(self.driver, temp["tabTitle"])
            res = temp["noReading"] in api.get_element_text_by_id(self.driver, temp["tagId"])
            #print res
            self.assertTrue(res, "1stY, the default reading percentage is not %s" % temp["noReading"])
            
            api.click_element_by_xpath(self.driver, temp["genesisXpath"])
            api.click_element_by_xpath(self.driver, temp["exodusXpath"])
            res = temp["twoBooksReading"] in api.get_element_text_by_id(self.driver, temp["tagId"])
            #print res
            self.assertTrue(res, "1stY, the two books reading percentage is not %s" % temp["twoBooksReading"])

            # cleanup the test scenario 
            api.click_element_by_xpath(self.driver, temp["genesisXpath"])            
            api.click_element_by_xpath(self.driver, temp["exodusXpath"])
            res = temp["noReading"] in api.get_element_text_by_id(self.driver, temp["tagId"])
            #print res
            self.assertTrue(res, "cleanup: 1stY, the default reading percentage is not %s" % temp["noReading"])

            time.sleep(1)
        except Exception as e:
            print e
            raise Exception("Cannot click on ", e)

    def test_007_select_2ndYear_reading(self):        
        try:
            temp = data["2nd_year_reading"]
            api.click_element_by_text(self.driver, temp["tabTitle"])
            res = temp["noReading"] in api.get_element_text_by_id(self.driver, temp["tagId"])
            #print res
            self.assertTrue(res, "2ndY, the default reading percentage is not %s" % temp["noReading"])

            api.click_element_by_xpath(self.driver, temp["matthewXpath"])
            api.click_element_by_xpath(self.driver, temp["markXpath"])            
            res = temp["twoBooksReading"] in api.get_element_text_by_id(self.driver, temp["tagId"])
            #print res
            self.assertTrue(res, "2ndY, the two books reading percentage is not %s" % temp["twoBooksReading"])

            # cleanup the test scenario 
            api.click_element_by_xpath(self.driver, temp["matthewXpath"])            
            api.click_element_by_xpath(self.driver, temp["markXpath"])
            res = temp["noReading"] in api.get_element_text_by_id(self.driver, temp["tagId"])
            #print res
            self.assertTrue(res, "cleanup: 2ndY, the default reading percentage is not %s" % temp["noReading"])

            time.sleep(1)
        except Exception as e:
            print e
            raise Exception("Cannot click on ", e)            

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
    # turn on lines below if you want separate reports based on time
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
