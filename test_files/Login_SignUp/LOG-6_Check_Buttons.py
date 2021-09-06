# Verify the login page
# Check Button label Texts

from selenium import webdriver
from variables import *

driver = webdriver.Firefox(executable_path=EXECUTABLE_PATH)
driver.implicitly_wait(5)
driver.get(LOGIN_PAGE)

login_btn_elem = driver.find_element_by_class_name("btn.btn-default.btn-lg.btn-block.effect.ladda-button.waves-effect")
signup_btn_elem = driver.find_element_by_class_name("btn.btn-outline-primary.btn-block.form-group.effect.ladda-sm.ladda-button.waves-effect")

login_text = login_btn_elem.text
signup_text = signup_btn_elem.text

driver.quit()

assert login_text == CORRECT_LOGIN_BTN
assert signup_text == CORRECT_SIGNUP_BTN
