from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://money.rediff.com/gainers/bse/daily/groupa')
# #self
# text_mag = driver.find_element(By.XPATH,'//a[contains(text(),"Just Dial")]/self::a').text
# print(text_msg)

# #parent
# parent = driver.find_element(By.XPATH,'//a[contains(text(),"Just Dial")]/parent::td').text
# print(parent)

# #child
# childs = driver.find_elements(By.XPATH,'//a[contains(text(),"Just Dial")]/ancestor::tr/child::td')
# for child in childs:
#     print(child.text)

# #ancestor
# text = driver.find_element(By.XPATH,'//a[contains(text(),"Just Dial")]/ancestor::tr').text
# print(text)

# #descendant
# descendants = driver.find_elements(By.XPATH,'//a[contains(text(),"Just Dial")]/ancestor::tr/descendant::*')
# for descendant in descendants:
#     print(descendant.text)

# #following
# following = driver.find_elements(By.XPATH,'//a[contains(text(),"Just Dial")]/ancestor::tr/following::*')
# for ele in following:
#     print('followning',ele.text)

# #following
followingsiblings = driver.find_elements(By.XPATH,'//a[contains(text(),"Just Dial")]/ancestor::tr/following-sibling::*')
for followsib in followingsiblings:
    print('followningsiblings',followsib.text)

# #preceding
# precedings = driver.find_elements(By.XPATH,'//a[contains(text(),"Just Dial")]/ancestor::tr/preceding::*')
# print('precedings',len(precedings))

# #preceding-sibling
# precedingsiblings = driver.find_elements(By.XPATH,'//a[contains(text(),"Just Dial")]/ancestor::tr/preceding-sibling::*')
# print('precedingsiblings',len(precedingsiblings))


