from lib2to3.pgen2 import driver


class GithubLogin():

    input_username = '//input[@id="user_login"]'
    input_email = '//input[@id="user_email"]'
    input_password = '//input[@id="user_password"]'
    checkbox = '//input[@id="all_emails"]'
    signup_button = '//button[@id="signup_button"]'

    def __init__(self, driver):
        self.driver = driver

    def create_account(self, username, email, password):
        self.driver.find_element_by_xpath(self.input_username).send_keys(username)
        self.driver.find_element_by_xpath(self.input_email).send_keys(email)
        self.driver.find_element_by_xpath(self.input_password).send_keys(password)
    def permission(self):
        self.driver.find_element_by_xpath(self.checkbox).click()
    def signup(self):
        self.driver.find_element_by_xpath(self.signup_button).click()
