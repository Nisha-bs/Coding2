from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)
#syntax: http:// username : password @ test.com
driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')
driver.maximize_window()

