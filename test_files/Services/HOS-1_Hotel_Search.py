# Verify Hotels searching process.
# Search for Hotels.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from variables import *

# set city input name
city_input = CITY_NAME

driver = webdriver.Firefox(executable_path=EXECUTABLE_PATH)
driver.implicitly_wait(5)
driver.get(HOTEL_PAGE)

city_field = driver.find_element_by_class_name("select2-selection.select2-selection--single")
submit_btn = driver.find_element_by_id("submit")

city_field.click()
input_field = driver.find_element_by_class_name("select2-search__field")
input_field.send_keys(city_input)
sleep(1)    # Hard wait to load city list.
input_field.send_keys(Keys.ENTER)
sleep(1)
submit_btn.click()
driver.implicitly_wait(10)
lists = driver.find_elements_by_class_name("hotels_amenities_")

driver.quit()
assert (len(lists) > 0), "Search function failed. Cannot found any data."
