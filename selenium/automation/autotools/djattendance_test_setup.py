#!/usr/bin/env python2.7

#--------------------------------------------------------------------------
# 
# Title: djattendance_test_setup.py
#
# Purpose: setup for the automation running
##
#--------------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from autotools import djattendance_test_api as api
from autotools import HTMLTestRunner
from datetime import datetime, timedelta
from optparse import OptionParser
import time, unittest, os, json, sys
# saucelabs 
from sauceclient import SauceClient

with open("data/saucelab.json") as data_file:
    saucelab_setting = json.load(data_file)

class AutomationSetup:

    def __init__(self, testname, drivertype=None, integration=None):
        self.testname = testname
        self.drivertype = drivertype
        self.integration = integration
        self.current_date = datetime.now()
        self.urladdress = None
        self.webdriver = None
        self.Sauce_Client = None
        self.USE_SAUCE = False
        self.test_failcounts = 0
        self.saucelab_environment_details = saucelab_setting
        self.saucelab_environment_details['name'] = testname

        if integration == "travisci": 
            # travisci-saucelab tunnel
            saucelab_environment_details['tunnel-identifier'] = os.environ.get('TRAVIS_JOB_NUMBER')
            saucelab_environment_details['build'] = os.environ.get('TRAVIS_BUILD_NUMBER')
            saucelab_environment_details['tags'] = [os.environ.get('TRAVIS_PYTHON_VERSION'), 'CI']

    def set_webdriver(self):        
        if self.drivertype == "chrome":
            if sys.platform == 'darwin':
                chromedriver = "../chromedriver_mac"
            elif sys.platform.startswith('linux'):
                chromedriver = "../chromedriver_linux"
            else:
                print "You must run these scripts with mac or linux."
                exit()
            self.webdriver = webdriver.Chrome(chromedriver)
        # saucelabs
        elif self.drivertype == "sauce":
            # travisci environment variables
            self.USE_SAUCE = True
            username = os.environ.get('SAUCE_USERNAME')
            access_key = os.environ.get('SAUCE_ACCESS_KEY')
            self.Sauce_Client = SauceClient(username, access_key)
            self.saucelab_environment_details['username'] = username
            self.saucelab_environment_details['key'] = access_key
            self.webdriver = webdriver.Remote(
                command_executor='http://%s:%s@ondemand.saucelabs.com:80/wd/hub' % (username, access_key),
                desired_capabilities=self.saucelab_environment_details
            )
        # default firefox webdriver
        else: 
            profile = webdriver.FirefoxProfile()
            profile.set_preference("xpinstall.signatures.required", False)
            self.webdriver = webdriver.Firefox(firefox_profile=profile)

    def set_urladdress(self, urladdress):
        self.urladdress = urladdress

    def update_saucelab(self, res=False):
        if res == False: self.test_failcounts += 1
        self.Sauce_Client.jobs.update_job(self.webdriver.session_id, passed=res)

    def get_testname(self): return self.testname
    def get_current_date(self): return self.current_date
    def get_urladdress(self): return self.urladdress
    def get_webdriver(self): return self.webdriver
    def get_saucelab_client(self): return self.Sauce_Client
    def get_test_failcounts(self): return self.test_failcounts
    def is_sauce_used(self): return self.USE_SAUCE

 