#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
'''driver.get('https://www.snapdeal.com/?utm_term=437025299421_104151711009_%7Bbidstrategy%7D&gclid=EAIaIQobChMI87fp0Yel9wIVhTUrCh29tAxZEAAYASAAEgIrg_D_BwE&utm_campaign=brand_account_brandcat_cpt_1d_ftu&utm_source=earth_sembrand&utm_medium=snapdeal')

searchbox = driver.find_element(By.XPATH,'//*[@id="inputValEnter"]')
print("Displayed or not",searchbox.is_displayed())
print("Enabled or not",searchbox.is_enabled())'''

driver.get('https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp')
select = driver.find_element(By.XPATH,"//input[@id='i3']")
print(select.is_selected())
driver.close()
