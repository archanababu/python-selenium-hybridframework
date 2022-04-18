import pytest
from selenium import webdriver
#from PageObjects.LoginPage import LoginPage

class Test_001_Login: #For pytest the class
    baseURL = "https://admin-demo.nopcommerce.com/"
    email = "admin@yourstore.com"
    password = "admin"

    def test_homePageTitle(self, setup): 
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()

        if act_title == "Your store. Login":
            assert True
        else:
            assert False
""" 
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login_page = LoginPage(self.driver)
        self.login_page.setEmail(self.email)
        self.login_page.setPassword(self.password)
        self.login_page.clickLogin()
        act_title = self.login_page.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
        else:
            assert False """

