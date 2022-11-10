from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import  time
class EditPatient:
    def __init__(self,driver):
        self.driver=driver

    edit_demographics_xpath='//*[@id="patient_main_container"]/div[2]/div[1]/div[1]/div[2]/button'
    btn_demo_link='Demographics'
    # patient_title_xpath='//*[@id="title"]/option[3]'
    demo_suffix_xapth='//*[@id="frmEditPatient_1"]/fieldset/div/div[1]/div[1]/div/div[1]/div/div[2]/div[1]/div[6]/div/input'
    demographics_save_xpath='//*[@id="frmEditPatient_1"]/fieldset/div/div[2]/div/button[3]'
    def clickon_btnedit_demo(self):
        self.driver.find_element(By.XPATH, self.edit_demographics_xpath).click()

    def clickon_btn_demo(self):
        self.driver.find_element(By.LINK_TEXT, self.btn_demo_link).click()
    # def set_patient_title(self,title):
    #     self.driver.find_element(By.XPATH, self.patient_title_xpath).clear()
    #     self.driver.find_element(By.XPATH, self.patient_title_xpath).send_keys(title)
    def setdemo_suffix(self,suffix):
        self.driver.find_element(By.XPATH, self.demo_suffix_xapth).clear()
        self.driver.find_element(By.XPATH, self.demo_suffix_xapth).send_keys(suffix)
    def click_btndemo_save(self):
        self.driver.find_element(By.XPATH, self.demographics_save_xpath).click()








