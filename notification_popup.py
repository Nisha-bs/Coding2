from selenium import webdriver
from selenium.webdriver.common.by import By

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

driver = webdriver.Chrome(options = ops)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://whatmylocation.com/')
