import time
import logging
import pytest
from selenium import webdriver
from pageObjects.EthizoLoginPage import loginpage
from utilities.readProperties import ReadConfig
from utilities.customLoger import LogGen
from  utilities import XLUtils
class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicaationURL()
    path="H:\\Selenium_Test_Project\\TestData\\logindata.xlsx"
    logger = LogGen.loggen(logLevel=logging.INFO)
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("********************Verifying Login Test Page Started******************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=loginpage(self.driver)
        self.lp.loginclick()
        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of rows in an Excel:",self.rows)
        lst_status=[]
        for r in range(2,self.rows+1):
            self.logger.info("********************Verifying Login Test Data Started******************")
            self.username=XLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.expc = XLUtils.readData(self.path, 'Sheet1', r, 3)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.loginclick()
            time.sleep(1)
            act_title=self.driver.title
            exp_title="Office Ally -- [SECURE SECTION]"
            if act_title==exp_title:
                if self.expc=="pass":
                    self.logger.info("***Passed")
                    self.lp.logoutclick()
                    lst_status.append("pass")
                elif self.expc=="fail":
                    self.logger.info("***Failed")
                    self.lp.logoutclick()
                    lst_status.append("fail")
            elif act_title!=exp_title:
                if self.expc=="pass":
                    self.logger.info("***Failed")
                    lst_status.append("fail")
                elif self.expc=="fail":
                    self.logger.info("***Passed")
                    lst_status.append("pass")

        if 'fial' not in lst_status:
            self.logger.info("Login DDT test passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login DDT test failed")
            self.driver.close()
            assert False

        self.logger.info("********************End of Login DDT Test******************")
        self.logger.info("********************completed TC_LoginDDT_002******************")






