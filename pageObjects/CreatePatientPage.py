from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import  time
class CreatePatient:
    def __init__(self,driver):
        self.driver=driver

    btncreatepatient_xpath ='//*[@id="ethizo-custom-modals_0"]/div/div/div[3]/div[2]/button[2]'
    txtlastname_xpath = '//*[@id="frmAddPatient"]/div/div[1]/div[2]/div[1]/div/div/div[1]/div/div[1]/div/div[2]/div[1]/div[3]/div/input'
    txtnicktname_id="nickname"
    txtsuffix_name ="suffix"
    txtssn_name='ssn'
    txtpatientexternelid_id='external_id'
    txt_race_css='#add-races > div > input'
    txt_ethinicity_css='#add-ethnicties > div > input'
    sel_defaultlocation_css='#default_locations > div > span > span.ui-select-match-text.pull-left'
    txt_defaultlocation_css='#default_locations > input.form-control.ui-select-search.ng-pristine.ng-valid'
    txt_state_id='state'
    txt_city_id='city'
    txt_race1_css='#ui-select-choices-row-3-0 > a > div'
    txt_ethinicity1_css = '#ui-select-choices-row-4-0 > a > div'
    txt_defaultlocation1_css = '#ui-select-choices-row-5-0 > a > span'
    btn_save_xpath='/html/body/div[2]/div[10]/div[1]/div[2]/div[2]/div/div/form/div/div[2]/div/button[2]'
    # txt_state1_css = '#default_locations > input.form-control.ui-select-search.ng-pristine.ng-valid.ng-hide'


    def clickoncreatepatient(self):
        self.driver.find_element(By.XPATH, self.btncreatepatient_xpath).click()
        time.sleep(2)
    def setlastname(self,lastname):
        self.driver.find_element(By.XPATH, self.txtlastname_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtlastname_xpath).send_keys(lastname)
    def setnickname(self,nickname):
        self.driver.find_element(By.ID, self.txtnicktname_id).clear()
        self.driver.find_element(By.ID, self.txtnicktname_id).send_keys(nickname)
    def setsuffix(self,suffix):
        self.driver.find_element(By.NAME, self.txtsuffix_name).clear()
        self.driver.find_element(By.NAME, self.txtsuffix_name).send_keys(suffix)
    def setssn(self,ssn):
        self.driver.find_element(By.NAME, self.txtssn_name).clear()
        self.driver.find_element(By.NAME, self.txtssn_name).send_keys(ssn)
    def setpatientid(self,patientid):
        self.driver.find_element(By.ID, self.txtpatientexternelid_id).clear()
        self.driver.find_element(By.ID, self.txtpatientexternelid_id).send_keys(patientid)
    def setrace(self,value):
        try:
            self.driver.find_element(By.CSS_SELECTOR, self.txt_race_css).send_keys(value)
            self.driver.find_element(By.CSS_SELECTOR, self.txt_race1_css).click()
        except Exception as e:
            print(e)
    def setethinicicty(self,value):
        self.driver.find_element(By.CSS_SELECTOR, self.txt_ethinicity_css).send_keys(value)
        self.driver.find_element(By.CSS_SELECTOR, self.txt_ethinicity1_css).click()

    def setdefault_location(self,value):
        try:
            self.driver.find_element(By.CSS_SELECTOR, self.sel_defaultlocation_css).click()
            self.driver.find_element(By.CSS_SELECTOR, self.txt_defaultlocation_css).send_keys(value)
            self.driver.find_element(By.CSS_SELECTOR, self.txt_defaultlocation1_css).click()
        except Exception as e:
            print(e)

    def setstate(self,value):
        try:
            drp = Select(self.driver.find_element(By.ID, self.txt_state_id))
            drp.select_by_visible_text(value)
        except Exception as e:
            print(e)
    def setcity(self,value):
        self.driver.find_element(By.ID, self.txt_city_id).clear()
        self.driver.find_element(By.ID, self.txt_city_id).send_keys(value)

    def click_btn_save(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()









