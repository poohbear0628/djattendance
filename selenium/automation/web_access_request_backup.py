#!/usr/bin/env python2.7

#--------------------------------------------------------------------------
# 
# Title: web_access_request.py
#
# Purpose: test cases for "Web Access Requests" of Django server
#
# Note:
#   - if "-url" option is used, do not use IP address, use string and port
#     (ex. localhost:8000)
#
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

with open("data/login.json") as data_file:
    server = json.load(data_file)

with open("data/test_inputdata.json") as data_file:
    data = json.load(data_file)
    data = data["web_access_requests"]

# name of the test and checking os version
testname = "WebAccessRequestsTest"
if sys.platform == 'darwin':
    chromedriver = "../chromedriver_mac"
elif sys.platform.startswith('linux'):
    chromedriver = "../chromedriver_linux"
else:
    print "You must run these scripts with mac or linux."
    exit()
current_date = datetime.now()
profile = None

# saucelabs
USE_SAUCE = False
Sauce_Client = None
test_passcount = 0
saucelab_environment_details = server["saucelab_env"]
saucelab_environment_details['name'] = testname

# option in command line
parser = OptionParser()
parser.add_option("-d", "--driver", action="store", dest="drivername")
parser.add_option("-u", "--url", action="store", dest="urlname")
parser.add_option("-i", "--integration", action="store", dest="ciname")
(options, args) = parser.parse_args()
# parsing the URL option
if options.urlname: 
    urladdress = options.urlname

    # if another URL used, then set the Firefox preference
    profile = webdriver.FirefoxProfile()
    profile.set_preference("xpinstall.signatures.required", False)
else: urladdress = server["domain"]

# travisci-saucelab tunnel
if options.ciname == "travisci": 
    saucelab_environment_details['tunnel-identifier'] = os.environ.get('TRAVIS_JOB_NUMBER')
    saucelab_environment_details['build'] = os.environ.get('TRAVIS_BUILD_NUMBER')
    saucelab_environment_details['tags'] = [os.environ.get('TRAVIS_PYTHON_VERSION'), 'CI']

# parsing the web browser testing option and checking system os
if options.drivername == "chrome": WebDriver = webdriver.Chrome(chromedriver)
elif options.drivername == "sauce":
    # saucelabs
    # travisci environment variables
    USE_SAUCE = True
    username = os.environ.get('SAUCE_USERNAME')
    access_key = os.environ.get('SAUCE_ACCESS_KEY')
    Sauce_Client = SauceClient(username, access_key)
    saucelab_environment_details['username'] = username
    saucelab_environment_details['key'] = access_key

    WebDriver = webdriver.Remote(
        command_executor='http://%s:%s@ondemand.saucelabs.com:80/wd/hub' % (username, access_key),
        desired_capabilities=saucelab_environment_details
    )
else: WebDriver = webdriver.Firefox(firefox_profile=profile)
#else: WebDriver = webdriver.Firefox()

class DjattendanceAutomation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global WebDriver        
        cls.driver = WebDriver
        global Sauce_Client
        cls.sauce_client = Sauce_Client

    def setUp(self):
        print "setUp"

    def test_001_get_domain(self):
        try:
            self.driver.get(urladdress)
            self.driver.maximize_window()
            time.sleep(5)
            if api.is_element_visible(self.driver, "djHideToolBarButton"):
                api.click_element_by_id(self.driver, "djHideToolBarButton")

            time.sleep(3)
        except Exception as e:
            if USE_SAUCE: 
                self.sauce_client.jobs.update_job(self.driver.session_id, passed=False)
                global test_passcount
                test_passcount += 1 
            print e
            raise Exception("Cannot open URL: ", e)
        #self.assertEqual(self.widget.size(), (50,50), 'incorrect default size')

    #@unittest.skip("skipping")
    def test_002_log_in(self):
        try:
            api.send_text_by_tag_name(self.driver, "username", server["username"])
            api.send_text_by_tag_name(self.driver, "password", server["password"])
            api.click_element_by_tag_value(self.driver, "Login")
            time.sleep(3)
        except Exception as e:    
            if USE_SAUCE: 
                self.sauce_client.jobs.update_job(self.driver.session_id, passed=False)
                global test_passcount
                test_passcount += 1             
            print e
            raise Exception("Login failed: ", e)            

    #@unittest.skip("skipping")
    def test_003_menu_web_access_requests(self):
        try:
            temp = data["default_page"]            
            api.click_element_by_xpath(self.driver, temp["menu_xpath"])
            time.sleep(1)
        except Exception as e:
            if USE_SAUCE: 
                self.sauce_client.jobs.update_job(self.driver.session_id, passed=False)
                global test_passcount
                test_passcount += 1             
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
            if USE_SAUCE: 
                self.sauce_client.jobs.update_job(self.driver.session_id, passed=False)
                global test_passcount
                test_passcount += 1             
            print e
            raise Exception("Two titles not equal: %s(web), %s(json)" % (res, temp["title"]), e)

    #@unittest.skip("skipping")
    def test_005_verify_creating_new_requests(self):
        try:
            # create four reuqests
            temp = data["request_page"] 
            # get the current time and +1 day
            req_date = datetime.strftime(current_date + timedelta(days=1), "%m/%d/%Y")

            for i in range(4):
                api.click_element_by_text(self.driver, data["default_page"]["create"])
                api.click_element_by_id(self.driver, temp["reason_id"])
                api.click_element_by_tag_value(self.driver, temp["reason_val"][i])
                api.get_element_focused(self.driver, value=temp["reason_id"])
                api.click_element_by_id(self.driver, temp["minutes_id"])                
                api.click_element_by_text(self.driver, temp["minutes"][i])
                api.get_element_focused(self.driver, value=temp["minutes_id"])
                api.click_element_by_id(self.driver, temp["expire_id"])
                api.send_text_by_tag_name(self.driver, temp["expire_tag"], req_date)

                # send comments
                api.click_element_by_id(self.driver, temp["comment_id"])
                api.send_text_by_tag_name(self.driver, temp["comment_tag"], temp["comment"][i])

                # mark as urgent 
                if i%2 == 0:
                    api.click_element_by_id(self.driver, temp["urgent_id"])

                # submit
                api.click_element_by_xpath(self.driver, temp["submit_xpath"])

            time.sleep(1)
        except Exception as e:
            if USE_SAUCE: 
                self.sauce_client.jobs.update_job(self.driver.session_id, passed=False)
                global test_passcount
                test_passcount += 1             
            print e
            raise Exception("Web Access Request page error: ", e)

    #@unittest.skip("skipping")
    def test_006_login_ta_account(self):
        try:
            api.click_element_by_clsname(self.driver, "dropdown-toggle")            
            api.click_element_by_xpath(self.driver, data["logout_xpath"])
            time.sleep(1)
            api.send_text_by_tag_name(self.driver, "username", data["ta_test"]["username"])
            api.send_text_by_tag_name(self.driver, "password", data["ta_test"]["password"], True)
            time.sleep(1)
        except Exception as e:
            if USE_SAUCE: 
                self.sauce_client.jobs.update_job(self.driver.session_id, passed=False)
                global test_passcount
                test_passcount += 1             
            print e
            raise Exception("Trainer Assistance account login error: ", e)

    #@unittest.skip("skipping")
    def test_007_verify_requests_from_ta_account(self):
        try:
            temp = data["request_page"] 

            # click based on xpath and verify each content 
            date = '{dt:%b}. {dt.day}, {dt.year}'.format(dt=current_date  + timedelta(days=1))
            request_dict = temp["request_dict"]
            for i in range(4):
                api.click_element_by_xpath(self.driver, data["default_page"]["menu_xpath"])
                api.click_element_by_xpath(self.driver, "//*[@class='panel-heading']//*[contains(text(),'" + temp["reason"][i] + "')]")
                request_dict["Status:"] = temp["status_org"]
                request_dict["Reason:"] = temp["reason"][i]
                request_dict["Minutes:"] = temp["minutes_res"][i]
                request_dict["Expires on:"] = date
                request_dict["Comments:"] = temp["comment"][i]
                request_dict["TA comments:"] = temp["ta_comment_org"]

                # get the list of value and examine it
                res = api.get_element_text_by_clsname(self.driver, "table").splitlines()
                for j, item in enumerate(res):
                    if ':' in item: # table key contains ":"
                        item = item.lstrip().rstrip()
                        #print res[j+1].lstrip().rstrip(), request_dict[item] #debugging
                        self.assertEqual(res[j+1].lstrip().rstrip(), request_dict[item])

                # mark the request
                api.click_element_by_xpath(self.driver, data["default_page"]["menu_xpath"])
                response = "//*[@class='panel-heading']//*[contains(text(),'" + temp["reason"][i] + "')]/../..//*[@title='" + temp["status_title"][i] + "']"
                api.click_element_by_xpath(self.driver, response)
                if temp["status_title"][i] == "Comment":
                    api.send_text_by_tag_name(self.driver, temp["ta_comment_tag"], temp["ta_comment_res"])
                    api.click_element_by_xpath(self.driver, temp["submit_xpath"])
                    
            time.sleep(1)
        except Exception as e:
            if USE_SAUCE: 
                self.sauce_client.jobs.update_job(self.driver.session_id, passed=False)
                global test_passcount
                test_passcount += 1             
            print e
            raise Exception("Error in verifying requests: ", e)

    #@unittest.skip("skipping")
    def test_008_ta_direct_web_access(self):
        try:
            api.click_element_by_xpath(self.driver, data["default_page"]["menu_xpath"])
            temp = data["direct_access"]
            api.click_element_by_text(self.driver, temp["title"])
            api.send_text_by_tag_name(self.driver, temp["mag_tag"], temp["mag_value"])
            api.click_element_by_id(self.driver, temp["time_id"])
            api.click_element_by_tag_value(self.driver, temp["time_value"])            
            api.get_element_focused(self.driver, value=temp["mag_id"])
            api.click_element_by_xpath(self.driver, temp["allow_xpath"])
            msg = api.get_element_text_by_clsname(self.driver, data["msg_clsname"])
            self.assertTrue(temp["granted_msg"] in msg)
 
            time.sleep(1)
        except Exception as e:
            if USE_SAUCE: 
                self.sauce_client.jobs.update_job(self.driver.session_id, passed=False)
                global test_passcount
                test_passcount += 1             
            print e
            raise Exception("Error in direct web access: ", e)

    #@unittest.skip("skipping")
    def test_009_login_back_to_trainee(self):
        try:
            api.click_element_by_clsname(self.driver, "dropdown-toggle")
            api.click_element_by_xpath(self.driver, data["logout_xpath"])
            time.sleep(1)
            api.send_text_by_tag_name(self.driver, "username", server["username"])
            api.send_text_by_tag_name(self.driver, "password", server["password"], True)
            time.sleep(1)
        except Exception as e:
            if USE_SAUCE: 
                self.sauce_client.jobs.update_job(self.driver.session_id, passed=False)
                global test_passcount
                test_passcount += 1             
            print e
            raise Exception("Trainee account login error: ", e)

    #@unittest.skip("skipping")
    def test_010_verify_responses_from_ta(self):
        try:
            api.click_element_by_xpath(self.driver, data["default_page"]["menu_xpath"])
            clsname = data["response_page"]["res_clsname"]
            reason = data["request_page"]["reason"]

            # focus on hover over to the corresponding link 
            for i in range(3, -1, -1):
                xpath = "//*[@class='" + clsname[i] + "']//*[text()='" + reason[i] + "']"
                elem = self.driver.find_element_by_xpath(xpath)
                api.get_element_focused(self.driver, xpath, "xpath")
                ActionChains(self.driver).move_to_element(elem).perform()
                time.sleep(1)
                    
            time.sleep(1)
        except Exception as e:
            if USE_SAUCE: 
                self.sauce_client.jobs.update_job(self.driver.session_id, passed=False)
                global test_passcount
                test_passcount += 1             
            print e
            raise Exception("Error in locating element: ", e)

    #@unittest.skip("skipping")
    def test_011_verify_approved_webaccess(self):
        try:
            # click start web access button
            temp = data["response_page"]
            xpath = "//*[@title='" + temp["approved_title"] + "']"
            api.click_element_by_xpath(self.driver, xpath)

            # check the approved message
            text = api.get_element_text_by_clsname(self.driver, data["msg_clsname"])
            self.assertTrue(temp["web_granted_msg"] in text, "%s(expected) is not in the string, %s(web)" % (temp["web_granted_msg"], text))

            # visit website in tab and get the title
            ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()
            time.sleep(1)
            self.driver.get(temp["demo_website"])
            time.sleep(1)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "panel1d-heading")))
            api.click_element_by_text(self.driver, temp["demo_button"])
            res = api.get_element_text_by_clsname(self.driver, temp["demo_clsname"])        
            self.assertEqual(temp["demo_text"], res)
            ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('w').key_up(Keys.CONTROL).perform()
            
            time.sleep(3)
        except Exception as e:
            if USE_SAUCE: 
                self.sauce_client.jobs.update_job(self.driver.session_id, passed=False)
                global test_passcount
                test_passcount += 1             
            print e
            raise Exception("Error in: ", e)

    #@unittest.skip("skipping")
    def test_012_verify_eShepherding_request(self):
        try:
            # at this point, the page should be still within "Web Access Request"
            temp = data["e-shepherding"]
            api.click_element_by_text(self.driver, temp["title"])
            api.send_text_by_tag_name(self.driver, temp["companion_tag"], temp["companion"])
            api.click_element_by_tag_value(self.driver, temp["submit_value"])
            
            # Cannot get the popup message when attempting to start e-shepherding without companion
            #WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            #alert = self.driver.switch_to_alert()

            # open Gamil and attempt to login
            ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()
            time.sleep(1)
            self.driver.get(temp["demo_website"])
            time.sleep(10)

            if api.is_element_visible(self.driver, "scroll-caret"):
                api.click_element_by_text(self.driver, temp["demo_button"])    

            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "identifier-shown")))
            api.click_element_by_tag_value(self.driver, temp["demo_tagvalue"])
            time.sleep(1)
            ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('w').key_up(Keys.CONTROL).perform()
            
            time.sleep(3)
        except Exception as e:
            if USE_SAUCE: 
                self.sauce_client.jobs.update_job(self.driver.session_id, passed=False)
                global test_passcount
                test_passcount += 1             
            print e
            raise Exception("Error in: ", e)

    #@unittest.skip("skipping")
    def test_013_delete_submitted_request(self):        
        try:
            api.click_element_by_xpath(self.driver, data["default_page"]["menu_xpath"])
            clsname = data["response_page"]["res_clsname"]
            reason = data["request_page"]["reason"]
            temp = data["delete"]

            # focus on hover over to the corresponding link 
            for i in range(4):
                xpath = "//*[@class='" + clsname[i] + "']//*[text()='" + reason[i] + "']/../.." + temp["delete_xpath"]
                api.click_element_by_xpath(self.driver, xpath)
                api.click_element_by_xpath(self.driver, temp["delete_confirm"])
                time.sleep(1)

        except Exception as e:
            if USE_SAUCE: 
                self.sauce_client.jobs.update_job(self.driver.session_id, passed=False)
                global test_passcount
                test_passcount += 1             
            print e
            raise Exception("Error in deleting: ", e)

    #@unittest.skip("skipping")
    def test_014_verify_request_deleted(self):
        try:
            api.click_element_by_xpath(self.driver, data["default_page"]["menu_xpath"])
            reason = data["request_page"]["reason"]
            for i in range(4):
                xpath = "//*[text()='" + reason[i] + "']"
                if api.is_element_visible(self.driver, xpath):
                    raise Exception("Trainee web access request is not deleted: %s" % reason[i])
                    time.sleep(1)

        except Exception as e:
            if USE_SAUCE: 
                self.sauce_client.jobs.update_job(self.driver.session_id, passed=False)
                global test_passcount
                test_passcount += 1             
            print e
            raise Exception("Error in verifying deleted request: ", e)

    def tearDown(self):
        print "tearDown"

    @classmethod
    def tearDownClass(cls):
        print "test done"
        global test_passcount
        if USE_SAUCE and test_passcount != 0:
            cls.sauce_client.jobs.update_job(self.driver.session_id, passed=False)       
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
    #runner.run(suite)

    # output result on console for debugging
    unittest.TextTestRunner(verbosity=2).run(suite)
    
    # close output file
    fp.close()


