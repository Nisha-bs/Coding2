from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers")
driver.find_element(By.ID,'txtUsername').send_keys('Admin')
driver.find_element(By.ID,'txtPassword').send_keys('admin123')
driver.find_element(By.ID,'btnLogin').click()
total_no_of_employees = len(driver.find_elements(By.XPATH,'//tr'))
print(total_no_of_employees)
count = 0
for user in range(1,total_no_of_employees):
    status = driver.find_element(By.XPATH,'//table[@id="resultTable"]/tbody/tr['+str(user)+']/td[5]').text
    if status == 'Disabled':
        user_name = driver.find_element(By.XPATH,'//table[@id="resultTable"]/tbody/tr['+str(user)+']/td[2]').text
        count += 1
print("disabled users",count)
print("enabled users",total_no_of_employees-count)