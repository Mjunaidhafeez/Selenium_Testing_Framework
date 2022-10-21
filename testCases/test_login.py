import pytest
import logging
from selenium import webdriver
from pageObjects.EthizoLoginPage import loginpage
from utilities.readProperties import ReadConfig
from utilities.customLoger import LogGen
class Test_001_Login():

    baseURL = ReadConfig.getApplicaationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    # log=LogGen.loggen(logLevel=logging.INFO)
    log = LogGen.loggen()
    @pytest.mark.regression
    def test_homePage(self,setup):
        self.log.info("*********************Verifying Home Pagr Title*****************")
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title=='ethiz':
            assert True
            self.driver.close()
            self.log.info("********************Home Page Title Test Is Passed******************")
        else:
            self.driver.save_screenshot('H:\\Selenium_Test_Project\\ScreenShots\\' + 'test_homePage.png')
            self.driver.close()
            self.log.error("********************Home Page Title Test Is Failed******************")
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_login(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.log=LogGen.loggen()
        self.log.info("********************Verifying Login Test Page Started******************")
        self.lp=loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.loginclick()
        act_title=self.driver.title
        if act_title=='ethizo':
            assert True
            self.driver.close()
            self.log.info("********************Login Page Title Test Is Passed******************")
        else:
            self.driver.save_screenshot('H:\\Selenium_Test_Project\\ScreenShots\\' + 'test_login.png')
            self.driver.close()
            self.log.error("********************Login Page Title Test Is Fialed******************")
            assert False
