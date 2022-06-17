from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.find_element(By.LINK_TEXT,'OrangeHRM, Inc').click()

windowids = driver.window_handles

# parent_windowid = windowids[0]
# child_windowid = windowids[1]

# driver.switch_to.window(parent_windowid)
# print('parent_title',driver.title)

# driver.switch_to.window(child_windowid)
# print('child_title',driver.title)

# for windowid in windowids:
#     driver.switch_to.window(windowid)
#     print(driver.title)

for windowid in windowids:
    driver.switch_to.window(windowid)
    if driver.title == 'OrangeHRM':
        driver.close()