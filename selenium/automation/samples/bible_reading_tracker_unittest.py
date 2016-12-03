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
import time
import unittest
import djattendance_test_api as api

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

server = { 	"domain" : "http://ap.ftta.lan/", "username" : "ap@gmail.com", "password" : "ap" }

class BibleReadingTracker(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()   

    def setUp(self):
        print "setUp"

    def test_001_get_domain(self):
    	self.driver.get(server["domain"])
    	self.driver.maximize_window()
    	time.sleep(3)
        #self.assertEqual(self.widget.size(), (50,50), 'incorrect default size')

    def test_002_log_in(self):
    	# Login
    	#myHeader = driver.find_elements_by_xpath("//*[contains(text(), 'FTTA Login')]")
		api.send_text_by_tag_name(self.driver, "username", server["username"])
		api.send_text_by_tag_name(self.driver, "password", server["password"], True)
        #self.assertEqual(self.widget.size(), (100,150), 'wrong size after resize')

    def test_003_bible_reading_tracker(self):
        api.click_element_by_text(self.driver, "Bible Reading Tracker")
        time.sleep(2)
        #self.assertEqual(self.widget.size(), (100,150), 'wrong size after resize')

    def test_004_select_bible_reading(self):
        #self.assertEqual(self.widget.size(), (100,150), 'wrong size after resize')
        api.click_element_by_id(self.driver, "select_menu")
        api.click_element_by_tag_value(self.driver, "week-0")
        api.click_element_by_xpath(self.driver, '//*[@id="status-day-0"]/label[1]')
        api.click_element_by_xpath(self.driver, '//*[@id="status-day-1"]/label[1]')
        api.click_element_by_xpath(self.driver, '//*[@id="status-day-2"]/label[2]')
        api.click_element_by_xpath(self.driver, '//*[@id="status-day-3"]/label[3]')
        api.click_element_by_xpath(self.driver, '//*[@id="status-day-4"]/label[1]')
        api.click_element_by_xpath(self.driver, '//*[@id="status-day-5"]/label[2]')
        api.click_element_by_xpath(self.driver, '//*[@id="status-day-6"]/label[3]')
        time.sleep(2)

    def tearDown(self):
        print "tearDown"

    @classmethod
    def tearDownClass(cls):
        print "test done"
        cls.driver.close()
        cls.driver.quit()



if __name__ == '__main__':
    #unittest.main()

    suite = unittest.TestLoader().loadTestsFromTestCase(BibleReadingTracker)
    #unittest.TextTestRunner(verbosity=2).run(suite)

    import HTMLTestRunner
    import os
    from datetime import datetime 
    #HTMLTestRunner.main()

    # output to a file
    if not os.path.exists('reports'): os.mkdir('reports')

    test_time = datetime.strftime(datetime.now(), '%Y-%m-%d_%H:%M:%S')

    test_report = 'reports/BibleReadingTrackerTest_' + test_time + '_.html'
    fp = file(test_report, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title='My unit test',
                description='This demonstrates the report output by HTMLTestRunner.'
                )

    # Use an external stylesheet.
    # See the Template_mixin class for more customizable options
    #runner.STYLESHEET_TMPL = '<link rel="stylesheet" href="my_stylesheet.css" type="text/css">'

    # run the test    
    runner.run(suite)
    fp.close()
