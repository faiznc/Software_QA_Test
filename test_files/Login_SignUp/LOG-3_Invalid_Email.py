# Verify the login of user
# Enter invalid Email and invalid Password

from selenium import webdriver
from time import sleep
import re
from variables import *

username = "wrong@phptravels.com"
password = "demouser"
message = "Wrong credentials. try again!"
# message = "email"   # Added this because to test whether script works if alert is indeed showing up (Wayback machine version)

driver = webdriver.Firefox(executable_path=EXECUTABLE_PATH)
driver.implicitly_wait(5)
driver.get(LOGIN_PAGE)

email_field = driver.find_element_by_name("email")
pwd_field = driver.find_element_by_name("password")
login_btn = driver.find_element_by_class_name("btn.btn-default.btn-lg.btn-block.effect.ladda-button.waves-effect")

email_field.send_keys(username)
pwd_field.send_keys(password)
sleep(1)
login_btn.click()
sleep(1)

source = driver.page_source
text_found = re.search(message, source)

driver.quit()
assert text_found, "Wrong Credentials alert is not showing up."
