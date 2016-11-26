# 
# this is testing purpose for webdriver
#
# Ref: 
# http://selenium-python.readthedocs.io/getting-started.html
# 

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX)
#driver.set_window_size(1280,1024)

driver = webdriver.Firefox()
driver.get("http://www.python.org")

#driver.get("http://attendance.ftta.lan/")
#help(driver) # allows you to view a list of variables, functions and comments for an imported module/object

assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
driver.quit()