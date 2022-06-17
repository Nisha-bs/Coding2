from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import pyautogui
import unittest
import HtmlTestRunner
# s=Service( r'C:\Users\swetha\Downloads\chromedriver.exe')

class DummyTicketTest(unittest.TestCase): 

  @classmethod
  def setUpClass(cls):
    ops = webdriver.ChromeOptions()
    ops.add_argument("--disable-notifications")
    cls.browser = webdriver.Chrome(options = ops)
    cls.browser.maximize_window()
    sleep(3)
    

  '''def test_homePageTitle(self):
    self.browser.get('https://www.dummyticket.com/')
    sleep(3)'''

  def test_login(self):
    self.browser.get('https://www.dummyticket.com/')
    sleep(10)
    self.browser.find_element(By.CSS_SELECTOR,'a.ffb-block-button-1-0').click()
    sleep(3)
    self.alrt = self.browser.switch_to.alert
    self.alrt.dismiss()
    #print(self.alrt.text)
 
  


  '''@classmethod
  def tearDownClass(cls):
    cls.browser.quit()
    print("Test completed.....")'''



if __name__ == "__main__":
  unittest.main()