#!/usr/bin/python3
import unittest
import HtmlTestRunner
from selenium import webdriver
import time
import sys
sys.path.append("/home/nisha/PYTHON/SELENIUM/Unittest_based_POM_project")
from page_objects.LoginPage import LoginPage

class LoginTest(unittest.TestCase):
    username = 'admin@yourstore.com'
    password = 'admin'
    url = 'http://admin-demo.nopcommerce.com/'
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
    
    def test_login(self):
        time.sleep(5)
        lp = LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.setLogin()
        time.sleep(2)
        self.assertEquals('Dashboard / nopCommerce administration', self.driver.title)

    @classmethod
    def tearDown(cls):
        time.sleep(5)
        cls.driver.close()
        
unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output = "/home/nisha/PYTHON/SELENIUM/Unittest_based_POM_project/reports"))
