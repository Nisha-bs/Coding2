#count no.of rows and columns
#read specific row and column data
#read all rows and columns data
#read data based on condition(list book names whose author name is mukesh)
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

# #count no.of rows and columns
rows = driver.find_elements(By.XPATH,'//table[@name="BookTable"]//tr')
# print(len(rows))
columns = driver.find_elements(By.XPATH,'//table[@name="BookTable"]//tr[1]/th')
# print(len(columns))

# #read specific row and column data
# data = driver.find_element(By.XPATH,'//table[@name="BookTable"]/tbody/tr[5]/td[1]')
# print(data.text)

# #read all rows and columns data
# for row in range(2 ,len(rows)+1):
#     for col in range(1,len(columns)+1):
#         data = driver.find_element(By.XPATH,'//table[@name="BookTable"]/tbody/tr['+str(row)+']/td['+str(col)+']').text
#         print(data,end = "                  ")
#     print()

#read data based on condition(list book names whose author name is mukesh)

for row in range(2,len(rows)):
    author_name = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(row)+"]/td[2]").text
    if author_name == 'Mukesh':
        book_name = driver.find_element(By.XPATH,'//table[@name="BookTable"]/tbody/tr['+str(row)+']/td[1]').text
        price = driver.find_element(By.XPATH,'//table[@name="BookTable"]/tbody/tr['+str(row)+']/td[4]').text
        print(book_name,  author_name,    price     )
