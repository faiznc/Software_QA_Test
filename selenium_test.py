#Test case to try whether selenium is working or not.
from selenium import webdriver
driver = webdriver.Firefox(executable_path=r'driver\geckodriver.exe')

driver.get("https://www.google.com")
assert "Google" in driver.title

driver.quit()
