from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import  time
class SearchPatient:
    def __init__(self,driver):
        self.driver=driver

    drppatient_id ='dLabel'
    rdaddpatient_xpath = '/html/body/div[2]/header/nav/div/div[2]/ul/li[1]/a'
    txtfirstname_name ="fname"
    txtlastname_name ="lname"
    drpgender_xpath='//*[@id="sex"]'
    txtdob_xpath='//*[@id="DOB"]'
    btnseach_xpath='//*[@id="ethizo-custom-modals_0"]/div/div/form/div[2]/button[2]'
    btn_create_patient_xpath='//*[@id="ethizo-custom-modals_0"]/div/div/div[3]/div[2]/button[2]'
    btn_view_patient_xpath='//*[@id="ethizo-custom-modals_0"]/div/div/div[2]/div[2]/button[2]'

    def clickonadrppatient(self):
        self.driver.find_element(By.ID, self.drppatient_id).click()
    def clickonaddnewpatient(self):
        self.driver.find_element(By.XPATH, self.rdaddpatient_xpath).click()
    def setfirstname(self,fierstname):
        self.driver.find_element(By.NAME, self.txtfirstname_name).clear()
        self.driver.find_element(By.NAME, self.txtfirstname_name).send_keys(fierstname)
    def setlastame(self,lastname):
        self.driver.find_element(By.NAME, self.txtlastname_name).clear()
        self.driver.find_element(By.NAME, self.txtlastname_name).send_keys(lastname)
    def setgender(self,value):
        drp= Select(self.driver.find_element(By.XPATH, self.drpgender_xpath))
        drp.select_by_visible_text(value)
    def setdateofbirth(self,dateofbirth):
        self.driver.find_element(By.XPATH, self.txtdob_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtdob_xpath).send_keys(dateofbirth)
    def clickonsearchbtn(self):
        self.driver.find_element(By.XPATH, self.btnseach_xpath).click()
    def click_btn_create_patient(self):
        create_patient=self.driver.find_elements(By.XPATH, self.btn_create_patient_xpath)
        new_patient = 0
        if len(create_patient) > 0 and create_patient[0].is_displayed():
            create_patient[0].click()
            print("Patient not found! Now created new patient!")
            new_patient = 1
        else:
            print("Patient Already Exist")
            self.driver.find_element(By.XPATH,self.btn_view_patient_xpath).click()
            new_patient = 0
        return new_patient
    def click_btn_view_patient(self):
        self.driver.find_elements(By.XPATH, self.btnseach_xpath).click()









