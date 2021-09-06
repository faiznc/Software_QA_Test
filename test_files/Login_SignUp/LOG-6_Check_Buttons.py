# Because of unresponsive website that occur on 06-09-2021, this test currently just a UI testing. Real response from server cannot be obtained

# Verify the login page
# Check Field label Texts

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import re
from variables import *

driver = webdriver.Firefox(executable_path=EXECUTABLE_PATH)
driver.implicitly_wait(5)
driver.get(LOGIN_PAGE)

login_btn_elem = driver.find_element_by_class_name("btn.btn-primary.btn-lg.btn-block.loginbtn")
signup_btn_elem = driver.find_element_by_class_name("btn.btn-success.br25.btn-block.form-group")

login_text = login_btn_elem.text
signup_text = signup_btn_elem.text

driver.quit()

assert login_text == "LOGIN"
assert signup_text == "SIGN UP"
