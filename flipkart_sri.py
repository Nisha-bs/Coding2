#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.flipkart.com/')

driver.implicitly_wait(5)

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

login_btn = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="container"]/div/div[1]/div[1]/div[2]/div[3]/div/div/div/a')))

mob_number = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input').send_keys('8428259394')
passwd = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input').send_keys('9600pdsv')

login = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button')
login.click()
sleep(3)

mouse = ActionChains(driver)
sleep(4)
Electronics = driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/div/div/div[5]/a/div[2]/div/div')
sleep(5)
mouse.move_to_element(Electronics).perform()
sleep(4)
Mobile = driver.find_element_by_link_text('MobileAccessory').click()
sleep(4)
Watch = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div[2]/div/div[2]/div/div/div[1]/div/div[6]/div/a/div[2]')

Watch.click()

sleep(4)
