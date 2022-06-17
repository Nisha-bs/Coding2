from atexit import register
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://mypage.rediff.com/login/dologin')
driver.maximize_window()
driver.find_element(By.XPATH,'//input[@value="Login"]').click()
alert = driver.switch_to.alert.accept()