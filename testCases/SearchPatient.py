import random
import string
import time

import pytest
from selenium.webdriver.common.by import By
from pageObjects.EthizoLoginPage import loginpage
from utilities.readProperties import ReadConfig
from pageObjects.SearchPatientPage import SearchPatient
from pageObjects.CreatePatientPage import CreatePatient
from utilities.customLoger import LogGen
from pageObjects.Edit_Demographic_page import EditPatient
# from RandomData.randamDataGenerate import RandomDataclass
from  utilities import XLUtils
class Test_003_Add_Patient():

    baseURL = ReadConfig.getApplicaationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger=LogGen.loggen()
    # login_data_path=ReadConfig.get_login_sheet_path()
    patient_data_path = ReadConfig.get_patient_data_sheet_path()
    # randomdata = RandomDataclass.random_generator()
    def test_SearchPatientPage(self,setup):
        self.logger.info("********************Test_003_Add_Patient******************")
        self.driver=setup
        self.driver.implicitly_wait(5)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp=loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.loginclick()
        self.logger.info("********************Login Successfull******************")
        self.logger.info("********************Home Page******************")
        # self.lp.clickcancel()
        self.searchpatient=SearchPatient(self.driver)
        self.searchpatient.clickonadrppatient()
        self.searchpatient.clickonaddnewpatient()
        self.logger.info("******************** Reading Patient Information From patient data sheeet******************")
        self.rows = XLUtils.getRowCount(self.patient_data_path, 'Sheet1')
        print("Number of rows in an Patient Data Sheet:", self.rows)
        for r in range(2,self.rows+1):
            self.logger.info("******************** Providing Patient Information******************")
            self.first_name = XLUtils.readData(self.patient_data_path, 'Sheet1', r, 1)
            self.last_name = XLUtils.readData(self.patient_data_path, 'Sheet1', r, 2)
            self.gender = XLUtils.readData(self.patient_data_path, 'Sheet1', r, 3)
            self.date_of_birth = XLUtils.readData(self.patient_data_path, 'Sheet1', r, 4)
            self.nick_name = XLUtils.readData(self.patient_data_path, 'Sheet1', r, 5)
            self.suffix = XLUtils.readData(self.patient_data_path, 'Sheet1', r, 6)
            self.ssn = XLUtils.readData(self.patient_data_path, 'Sheet1', r, 7)
            self.race = XLUtils.readData(self.patient_data_path, 'Sheet1', r, 8)
            self.ethinicity = XLUtils.readData(self.patient_data_path, 'Sheet1', r, 9)
            self.external_id = XLUtils.readData(self.patient_data_path, 'Sheet1', r, 10)
            self.default_location = XLUtils.readData(self.patient_data_path, 'Sheet1', r, 11)
            self.city = XLUtils.readData(self.patient_data_path, 'Sheet1', r, 12)
            self.state = XLUtils.readData(self.patient_data_path, 'Sheet1', r, 13)
            self.searchpatient.setfirstname(self.first_name)
            self.searchpatient.setlastame(self.last_name)
            self.searchpatient.setgender(self.gender)
            self.searchpatient.setdateofbirth(self.date_of_birth)
            self.searchpatient.clickonsearchbtn()
            self.logger.info("********************Search Patient Successsfully******************")
            try:
                new_patient=self.searchpatient.click_btn_create_patient()
                if new_patient>0:
                    self.logger.info("********************Create Patient Start******************")
                    # self.createpatient.setlastname(self.randomdata)
                    # self.createpatient.setlastname(self.last_name)
                    self.createpatient = CreatePatient(self.driver)
                    self.createpatient.setnickname(self.nick_name)
                    self.createpatient.setsuffix(self.suffix)
                    self.createpatient.setssn(self.ssn)
                    self.createpatient.setpatientid(self.external_id)
                    self.createpatient.setrace(self.race)
                    self.createpatient.setethinicicty(self.ethinicity)
                    self.createpatient.setdefault_location(self.default_location)
                    self.createpatient.setstate(self.state)
                    self.createpatient.setcity(self.city)
                    self.createpatient.click_btn_save()

                else:
                    self.logger.info("********************Edit Patient Start******************")
                    self.eidtpatient=EditPatient(self.driver)
                    self.eidtpatient.setdemo_suffix(self.suffix)
                    self.eidtpatient.click_btndemo_save()

            except Exception as e:
                print("Oops!", e, "occurred.")
                break



            # self.city = XLUtils.readData(self.patient_data_path, 'Sheet1', r, 14)
            # self.city = XLUtils.readData(self.patient_data_path, 'Sheet1', r, 15)
            # self.city = XLUtils.readData(self.patient_data_path, 'Sheet1', r, 16)
            # self.city = XLUtils.readData(self.patient_data_path, 'Sheet1', r, 17)



        # self.logger.info("********************Create Patient Start******************")
        # self.createpatient=CreatePatient(self.driver)
        # self.createpatient.clickoncreatepatient()
        # self.logger.info("********************Providing New Patient Data******************")
        # # self.email=random_generator() + "@gmail.com" #generate of email templates
        # # self.createpatient.setlastname(self.randomdata)
        # self.createpatient.setlastname('j')
        # self.createpatient.setnickname('juni')
        # self.createpatient.setsuffix('mr')
        # self.createpatient.setssn('565-65-6565')
        # self.createpatient.setpatientid('9898965656')
        #
        # self.logger.info("********************New Patient Data Saved Successfully******************")
        #
        # self.logger.info("********************Validation Of New Patient Data******************")
        #
        # self.msg= self.driver.find_element(By.TAG_NAME,'Body').text
        # print(self.msg)
        #
        # if 'New Patient Data Saved Successfully' in self.msg:
        #     assert True==True
        #     self.logger.info("********************New Patient Data Add Test Passed******************")
        # else:
        #     self.driver.save_screenshot('H:\\Selenium_Test_Project\\ScreenShots\\' + 'test_AddPatient_src.png')
        #     self.logger.error("********************New Patient Data Add Test Failed******************")
        #     assert True==False
        #
        # self.driver.close()
        # self.logger.info("********************Ending Of Patient Data Page******************")
# def random_generator(size=8, chars=string.ascii_lowercase +string.digits):
#     return ''.join(random.choice(chars) for x in range(size)) #generate random data





