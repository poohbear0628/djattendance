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
import djattendance_test_api as api

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Firefox()
#driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX)


# get Firefox webdriver and load web page
#server = {	"domain" : "http://attendance.ftta.lan/", "username" : "joonjo", "password" : "ftta2016" }
server = { 	"domain" : "http://ap.ftta.lan/", "username" : "ap@gmail.com", "password" : "ap" }
driver.get(server["domain"])
driver.maximize_window()

# wait until it sees the title 
time.sleep(3)
#driver.implicitly_wait(10) # seconds
#wait = WebDriverWait(driver, 10)
#element = wait.until(EC.element_to_be_clickable((By.ID,'someid')))
#element = wait.until(EC.presence_of_element_located((By.ID, "addresses")))
#print element

# get the FTTA Login
myHeader = driver.find_elements_by_xpath("//*[contains(text(), 'FTTA Login')]")
#myHeader = driver.find_element_by_id("Header")

# retreive the attributes 
#attrs = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', myHeader)

# Login
api.send_text_by_tag_name(driver, "username", server["username"])
api.send_text_by_tag_name(driver, "password", server["password"], True)

#
api.click_element_by_text(driver, "Bible Reading Tracker")
time.sleep(2)


#
api.click_element_by_id(driver, "select_menu")

# select by id
#elem = driver.find_element_by_id("0")
#elem.click()
#time.sleep(2)

# xpath
api.click_element_by_tag_value(driver, "week-0")
api.click_element_by_xpath(driver, '//*[@id="status-day-0"]/label[1]')
api.click_element_by_xpath(driver, '//*[@id="status-day-1"]/label[1]')
api.click_element_by_xpath(driver, '//*[@id="status-day-2"]/label[2]')
api.click_element_by_xpath(driver, '//*[@id="status-day-3"]/label[3]')
api.click_element_by_xpath(driver, '//*[@id="status-day-4"]/label[1]')
api.click_element_by_xpath(driver, '//*[@id="status-day-5"]/label[2]')
api.click_element_by_xpath(driver, '//*[@id="status-day-6"]/label[3]')



#click_element_by_text(driver, "Submit Web Access Request")
#click_element_by_text(driver, "Fellowship")

#send_text_by_tag_name(driver, "comments", "I need to pay my bills, thank you.")
#time.sleep(3)

#elem = driver.find_element_by_name("minutes")
#elem.click()
#elem.send_keys('45')
#elem.click()
#time.sleep(3)

#send_text_by_tag_name(driver, "usageTime", "1:15 pm - 2:00 pm")
time.sleep(2)

#assert "No results found." not in driver.page_source

driver.close()
driver.quit()