# Verify Hotels searching process.
# Check whether Hotel data displayed correctly

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from variables import *

city_input = CITY_NAME

driver = webdriver.Firefox(executable_path=EXECUTABLE_PATH)
driver.implicitly_wait(5)
driver.get(HOTEL_PAGE)

city_field = driver.find_element_by_class_name("select2-selection.select2-selection--single")

submit_btn = driver.find_element_by_id("submit")

city_field.click()
input_field = driver.find_element_by_class_name("select2-search__field")
input_field.send_keys(city_input)
sleep(1)
input_field.send_keys(Keys.ENTER)
sleep(1)
submit_btn.click()
driver.implicitly_wait(10)

lists = driver.find_elements_by_class_name("hotels_amenities_")
assert (len(lists) > 0), "Search function failed. Cannot found any data."

lists[1].click()
x = lists[1]
x.find_element_by_class_name("more_details.effect.mt-0.btn-block.ladda-button.waves-effect")
x.click()
# Only check whether the "Book Now" button is presence in hotel page.
book_now_btn_elem = driver.find_element_by_class_name("effect.ladda.effect.ladda-button.waves-effect")
book_text = book_now_btn_elem.text

driver.quit()
assert book_text == "Book Now", "Hotel Information does not displayed correctly."