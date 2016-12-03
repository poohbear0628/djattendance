#!/usr/bin/env python2.7

#--------------------------------------------------------------------
# 
# Title: demo_attendance.py
#
# Purpose: demonstrate selenium webdriver for attendance server
#
#--------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def send_text_by_tag_name(driver, tag_name, value, enter=False):
	elem = driver.find_element_by_name(tag_name)
	elem.clear()
	elem.send_keys(value)
	if enter == True:
		elem.send_keys(Keys.RETURN)
		time.sleep(3)

def click_element_by_text(driver, text, pose=2):
	elem = driver.find_element_by_xpath('//*[contains(text(), "'+ text + '")]')
	elem.click()
	time.sleep(pose)


driver = webdriver.Firefox()
#driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX)


# get Firefox webdriver and load web page
server = {	"domain" : "http://attendance.ftta.lan/", "username" : "joonjo", "passwd" : "ftta2016" }
#server = { 	"domain" : "http://ap.ftta.lan/", "username" : "ap", "passwd" : "ap" }
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
send_text_by_tag_name(driver, "username", "joonjo")
send_text_by_tag_name(driver, "password", "ftta2016", True)

# Web Access Request
click_element_by_text(driver, "Web Access Requests")
click_element_by_text(driver, "Submit Web Access Request")
click_element_by_text(driver, "Fellowship")

send_text_by_tag_name(driver, "comments", "I need to pay my bills, thank you.")
time.sleep(3)

elem = driver.find_element_by_name("minutes")
elem.click()
elem.send_keys('45')
elem.click()
time.sleep(3)

send_text_by_tag_name(driver, "usageTime", "1:15 pm - 2:00 pm")
time.sleep(10)

#assert "No results found." not in driver.page_source

driver.close()
driver.quit()