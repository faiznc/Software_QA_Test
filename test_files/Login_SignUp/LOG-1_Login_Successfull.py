# Verify the login of user
# Enter valid Username and valid Password

from selenium import webdriver
from time import sleep
from variables import *

username = "user@phptravels.com"
password = "demouser"

driver = webdriver.Firefox(executable_path= EXECUTABLE_PATH)
driver.implicitly_wait(5)
driver.get(LOGIN_PAGE)

email_field = driver.find_element_by_name("email")
pwd_field = driver.find_element_by_name("password")
login_btn = driver.find_element_by_class_name("btn.btn-default.btn-lg.btn-block.effect.ladda-button.waves-effect")

email_field.send_keys(username)
pwd_field.send_keys(password)
sleep(1)
login_btn.click()
sleep(5)
title = driver.title

driver.quit()
assert "Dashboard" in title, "Registered User failed to login."