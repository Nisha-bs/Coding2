#!/usr/bin/python3
import email
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import sys
sys.path.append('/home/nisha/PYTHON/SELENIUM')
from github.create_github import Github_Login

import time

from github.create_github import Github_Login 

class Test_GitHub(unittest.TestCase):
    username = 'nisha'
    mail = 'nisha@gmail.com' 
    paswword = 'Nisha@1998'
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    @classmethod
    def setUpClass(cls):
        cls.driver.get('https://github.com/join')
        cls.driver.maximize_window()

    def Test_Login(self):
        Log = Github_Login(self.driver)
        Log.create_account(self.username, self.email, self.password)
        time.sleep(10)
        Log.permission()
        Log.signup()

    @classmethod
    def tearDown(cls):
        cls.driver.close()

unittest.main()
         
