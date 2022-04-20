from asyncio.log import logger
from importlib.resources import path

from pytest import fail
from PageObjects.LoginPage import LoginPage
from Utilities.ReadProperties import ReadConfig
from Utilities.CustomLogger import LogGen
from Utilities import xlUtils
import time

class Test_002_LoginDDT: #For pytest the class should start with Test
    baseURL     = ReadConfig.getApplicationURL()
    path        = ReadConfig.getTestData()
    sheetName   = ReadConfig.getTestDataSheetName()
    logger      = LogGen.loggen()
    
    def test_loginDDT(self, setup):
        self.logger.info("****************************test_loginDDT***************************")
        self.logger.info("Verifying Login test")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)

        test_status = []
        i=0

        self.rows = xlUtils.getRowCount(self.path,self.sheetName)
        for r in range(2,self.rows+1):
            i=i+1
            self.email = xlUtils.readData(self.path,self.sheetName,r,1)
            self.password = xlUtils.readData(self.path,self.sheetName,r,2)
            self.exp_result = xlUtils.readData(self.path,self.sheetName,r,3)

            self.login_page.setEmail(self.email)
            self.login_page.setPassword(self.password)
            self.login_page.clickLogin()

            time.sleep(3)

            act_title = self.driver.title
            if act_title == "Dashboard / nopCommerce administration":
                if self.exp_result == "pass":
                    self.logger.info("TestData "+str(i)+": Validation result : PASSED")
                    self.login_page.clickLogout()
                    test_status.append("Pass")
                    
                elif self.exp_result == "fail":
                    self.logger.info("TestData "+str(i)+": Validation result : FAILED")
                    self.driver.save_screenshot(".\\Screenshots\\"+"TestData_"+i+"_test_login.png")
                    self.login_page.clickLogout()
                    test_status.append("Fail")

            elif act_title != "Dashboard / nopCommerce administration":
                if self.exp_result == "pass":
                    self.logger.info("TestData "+str(i)+": Validation result : FAILED")   
                    self.driver.save_screenshot(".\\Screenshots\\"+"TestData_"+i+"_test_login.png")                 
                    test_status.append("Fail")
                elif self.exp_result == "fail":
                    self.logger.info("TestData "+str(i)+": Validation result : PASSED")                    
                    test_status.append("Pass")

            
        
        if "Fail" not in test_status:
            self.logger.info("loginDDT Validation PASSED")
            self.driver.close()
            assert True
        else:
            self.logger.info("loginDDT Validation FAILED")
            self.driver.close()
            assert False

        self.logger.info("loginDDT Validation Completed")





        
        
        
                
        

