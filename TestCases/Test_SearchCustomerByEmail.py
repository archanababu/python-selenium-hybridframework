import time

import pytest
from PageObjects.LoginPage import LoginPage
from PageObjects.AddCustomerPage import AddCustomer
from PageObjects.SearchCustomerPage import SearchCustomer
from Utilities.ReadProperties import ReadConfig
from Utilities.CustomLogger import LogGen

class Test_004_SearchCustomerByEmail:
    baseURL = ReadConfig.getApplicationURL()
    email   = ReadConfig.getEmail()
    password= ReadConfig.getPassword()
    logger  = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("****************************test_searchCustomerByEmail***************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.login_page.setEmail(self.email)
        self.login_page.setPassword(self.password)
        self.login_page.clickLogin()                
        self.logger.info("Login successful")
        
        self.logger.info("Validating search customer by email testing")
        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomersMenu()
        self.addCust.clickOnCustomersMenuItem()

        self.searchCustomer = SearchCustomer(self.driver)
        self.searchCustomer.setEmail("victoria_victoria@nopCommerce.com")
        self.searchCustomer.search()

        time.sleep(5)

        self.status = self.searchCustomer.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        if self.status == True:
            self.logger.info("Search customer by email validation PASSED")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_searchCustomerByEmail.png")
            self.logger.info("Search customer by email validation FAILED")
            assert False

        self.driver.close()
        self.logger.info("Ending test_searchCustomerByEmail test case")

