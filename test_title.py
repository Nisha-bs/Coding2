#!/usr/bin/env  python3
from selenium import webdriver
import unittest
import HtmlTestRunner
from selenium.webdriver.common.by import By
import time

class OrangeHRMTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
       

    def test_homePageTitle(self):
        self.driver.get('https://oensource-demo.orangehrmlive.com')
        self.assertEqual("OrangeHRM",self.driver.title,'title is not same')

    def test_login(self):
        self.driver.get('https://oensource-demo.orangehrmlive.com')
        self.driver.find_element(By.NAME,'txtUsername').send_keys('Admin')
        self.driver.find_element(By.NAME,'txtPassword').send_keys('admin123')
        self.driver.find_element(By.NAME,'Submit').click()
        self.assertEqual("OrangeHRM",self.driver.title,'title is not same')

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.quit()
        print('completed')
if __name__ == 'main':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/nisha/PYTHON/SELENIUM/unittest/out'))
