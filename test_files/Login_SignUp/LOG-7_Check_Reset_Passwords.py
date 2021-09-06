# Verify the login page
# Check Reset Password / Forget Password Appearance

from selenium import webdriver
from variables import *

driver = webdriver.Firefox(executable_path=EXECUTABLE_PATH)
driver.implicitly_wait(5)
driver.get(LOGIN_PAGE)

reset_btn_elem = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[2]/div[2]/div[2]/label")

reset_text = reset_btn_elem.text

driver.quit()

assert reset_text == CORRECT_RESET_TEXT
