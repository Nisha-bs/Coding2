#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.google.com/')
driver.maximize_window()
link = driver.find_element(By.NAME,'q')
link.send_keys('create google account')
time.sleep(2)
link.submit()
#driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[2]/ul[1]/div/ul/li[1]/div/div[2]/div[1]/span')
#driver.find_element(By.CSS_SELECTOR,'body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.FPdoLc.lJ9FBc > center > input.gNO89b')
driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[2]/ul[1]/div/ul/li[1]/div/div[2]/div[1]/span').click()
driver.find_element(By.XPATH,'//*[@id="rso"]/div[2]/div/div[1]/div/a/h3').click()
driver.find_element(By.LINK_TEXT,'Create an account').click()
time.sleep(2)



'''
driver.get('https://accounts.google.com/signup/v2/webcreateaccount?continue=https%3A%2F%2Fmyaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dcreate-account-button&flowName=GlifWebSignIn&flowEntry=SignUp')





driver.find_element(By.CSS_SELECTOR,"input[jsname=YPqjbf]").send_keys("nisha")
driver.find_element(By.CSS_SELECTOR,"input[name=lastName]").send_keys("venkatesan")
gmail = 'nishvenget982103'
driver.find_element(By.CSS_SELECTOR,"input[autocomplete=username]").send_keys('nishvenget982103')
password = 'nish@982103'
driver.find_element(By.CSS_SELECTOR,"input[type=password]").send_keys(password)
driver.find_element(By.CSS_SELECTOR,"input[name=ConfirmPasswd]").send_keys(password)
driver.find_element(By.CSS_SELECTOR,"input[type=checkbox]").click()
#driver.find_element(By.CSS_SELECTOR,"button[jscontroller=soHxf]").click()
#driver.find_element(By.CSS_SELECTOR,'[autocomplete=username]').send_keys(input('enter your gmail id'))
time.sleep(5)
driver.find_element(By.XPATH,'//button[@type="button"]/span').click()
driver.find_element(By.CSS_SELECTOR,'input[name=Username]').send_keys('nishvenget982103@gmail.com')
driver.find_element(By.XPATH,'//button[@type="button"]/span').click()
driver.find_element(By.CSS_SELECTOR,'input[name=Username]').send_keys(input('gmail'))
driver.find_element(By.XPATH,'//button[@type="button"]/span').click()
#driver.close()'''


