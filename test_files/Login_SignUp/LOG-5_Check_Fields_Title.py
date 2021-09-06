# Verify the login page
# Check Field label Texts

from selenium import webdriver
from variables import *

driver = webdriver.Firefox(executable_path=EXECUTABLE_PATH)
driver.implicitly_wait(5)
driver.get(LOGIN_PAGE)

email_text_elem = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/form/div[1]/label')
pwd_text_elem = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/form/div[2]/label')

email_text = email_text_elem.text
pwd_text = pwd_text_elem.text

driver.quit()

assert email_text == CORRECT_EMAIL_TEXT
assert pwd_text == CORRECT_PWD_TEXT
