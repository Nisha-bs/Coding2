#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://jqueryui.com/datepicker/")

driver.switch_to.frame(0)
#driver.find_element(By.CLASS_NAME,'hasDatepicker').send_keys('03/21/1998')

expected_month = 'March'
expected_year = '2023'
expected_date = '21'

driver.find_element(By.XPATH,'//input[@id="datepicker"]').click()
while True:
    month = driver.find_element(By.XPATH,'//span[@class="ui-datepicker-month"]').text
    year = driver.find_element(By.XPATH,'//span[@class="ui-datepicker-year"]').text

    if month ==  expected_month and year == expected_year:
        break
    elif year > expected_year:
        driver.find_element(By.LINK_TEXT,'Prev').click()
    elif year < expected_year:
        driver.find_element(By.LINK_TEXT,'Next').click()
    else:
        continue

dates = driver.find_elements(By.XPATH,'//table[@class="ui-datepicker-calendar"]/tbody/tr/td')
for date in dates:
    print(date.text)

    if date.text == expected_date:
        date.click()
        break
    else:
        continue 




