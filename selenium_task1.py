from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webriver.Firefox()
driver.get('http://www.google.com')
inputElement = driver.find_element_by_name('q')
input_Element.send_keys('cheese!')
inputElement.submit()
print(driver.title)
