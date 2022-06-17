import unittest
from selenium import webdriver
import Page
class ApressSearch(unittest.TestCase):
#Sample test case using Page Object Model
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.apress.com")

    def test_apress_search(self):
        #Visits aprèss.com
        home_page = Page.HomePage(self.driver)
        #Searches "Python Selenium" keyword
        home_page.search_text ="Python Selenium"
        home_page.click_submit_button()
        search_results_page = Page.ResultPage(self.driver)
        #Checks if page is not empty
        assert search_results_page.check_search_results(), "No results found."
    def tearDown(self):
        self.driver.close()
if __name__ =="__main__":
    unittest.main()