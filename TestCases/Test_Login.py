from asyncio.log import logger
import py

import pytest
from PageObjects.LoginPage import LoginPage
from Utilities.ReadProperties import ReadConfig
from Utilities.CustomLogger import LogGen

class Test_001_Login: #For pytest the class should start with Test 
    baseURL= ReadConfig.getApplicationURL()
    email= ReadConfig.getEmail()
    password= ReadConfig.getPassword()
    logger= LogGen.loggen()

    @pytest.mark.sanity
    def test_homePageTitle(self, setup):
        self.logger.info("****************************test_homePageTitle***************************")
        self.logger.info("Verifying Home Page Title")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        
        if act_title == "Your store. Login":
            self.driver.close()
            self.logger.info("Validation result : PASSED")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("Validation result : FAILED")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("****************************test_login***************************")
        self.logger.info("Verifying Login test")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.login_page.setEmail(self.email)
        self.login_page.setPassword(self.password)
        self.login_page.clickLogin()
        act_title = self.driver.title
                
        if act_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            self.logger.info("Validation result : PASSED")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.error("Validation result : FAILED")
            assert False

