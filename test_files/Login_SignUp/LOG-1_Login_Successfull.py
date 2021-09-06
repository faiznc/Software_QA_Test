# Because of unresponsive website that occur on 06-09-2021, this test currently just a UI testing. Real response from server cannot be obtained

# Verify the login of user
# Enter valid Username and valid Password

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from variables import *

username = "user@phptravels.com"
password = "demouser"

driver = webdriver.Firefox(executable_path= EXECUTABLE_PATH)
driver.implicitly_wait(5)
driver.get(LOGIN_PAGE)

email_field = driver.find_element_by_name("username")
pwd_field = driver.find_element_by_name("password")
login_btn = driver.find_element_by_class_name("btn.btn-primary.btn-lg.btn-block.loginbtn")

email_field.send_keys(username)
pwd_field.send_keys(password)
sleep(1)
login_btn.click()
sleep(5)
title = driver.title

driver.quit()
assert "Dashboard" in title, "Registered User failed to login."  # For now, unable to check