#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers")

driver.find_element(By.ID,'txtUsername').send_keys('Admin')
driver.find_element(By.ID,'txtPassword').send_keys('admin123')
driver.find_element(By.ID,'btnLogin').click()

Admin = driver.find_element(By.XPATH,'//a[@id="menu_admin_viewAdminModule"]')
UserManagement = driver.find_element(By.XPATH,'//a[@id="menu_admin_UserManagement"]')
Users = driver.find_element(By.XPATH,'//a[@id="menu_admin_viewSystemUsers"]')

mouse = ActionChains(driver)
mouse.move_to_element(Admin).move_to_element(UserManagement).move_to_element(Users).click().perform()
