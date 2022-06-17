from lib2to3.pgen2 import driver
from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By

class  Test_tile(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://admin-demo.nopcommerce.com')
    def 