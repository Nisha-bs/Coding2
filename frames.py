from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
#syntax: http:// username : password @ test.com
driver.get('https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html')
driver.maximize_window()

driver.switch_to.frame('packageListFrame')
driver.find_element(By.LINK_TEXT,'org.openqa.selenium').click()

driver.switch_to.default_content()
driver.switch_to.frame('packageFrame')
driver.find_element(By.LINK_TEXT,'WebDriver').click()

driver.switch_to.default_content()
driver.switch_to.frame('classFrame')
driver.find_element(By.LINK_TEXT,'SearchContext').click()