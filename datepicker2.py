#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.find_element(By.XPATH,'//input[@id="dob"]').click()

birth_date = input('enter birth date')
birth_month = input('enter birth month')
birth_year = input('enter birth year')

years = driver.find_elements(By.XPATH,'//select[@class="ui-datepicker-year"]/option')
driver.find_element(By.XPATH,'//select[@class="ui-datepicker-year"]').click()
for year in years:
    if year.text == birth_year:
        year.click()
        break
    else:
        continue

months = driver.find_elements(By.XPATH,'//select[@class="ui-datepicker-month"]/option')
driver.find_element(By.XPATH,'//select[@class="ui-datepicker-month"]').click()
for month in months:
    print(month.text)
    if month.text == birth_month:
        month.click()
        break
    else:
        continue
dates = driver.find_elements(By.XPATH,'//table[@class="ui-datepicker-calendar"]/tbody/tr/td')
for date in dates:
    if date.text == birth_date:
        date.click()
        break
    else:
        continue





                                                                            
