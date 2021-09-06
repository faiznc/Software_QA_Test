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

email_text_elem = driver.find_element_by_xpath('//*[@id="loginfrm"]/div[3]/div[1]/label/span')
pwd_text_elem = driver.find_element_by_xpath('//*[@id="loginfrm"]/div[3]/div[2]/label/span')

email_text = email_text_elem.text
pwd_text = pwd_text_elem.text

driver.quit()

assert email_text == "Email"
assert pwd_text == "Password"
