import time

from selenium.webdriver.common.by import By
class loginpage:

    txtbox_username_name='username'
    txtbox_password_name='password'
    btn_login_id='login'
    btncancel_xpath='//*[@id="ethizoWebApp"]/div[3]/div/div/div[3]/button[1]'
    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element(By.NAME, self.txtbox_username_name).clear()
        self.driver.find_element(By.NAME,self.txtbox_username_name).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.NAME, self.txtbox_password_name).clear()
        self.driver.find_element(By.NAME,self.txtbox_password_name).send_keys(password)

    def loginclick(self):
        self.driver.find_element(By.ID,self.btn_login_id).click()
        time.sleep(5)

    def clickcancel(self):
         self.driver.find_element(By.XPATH, self.btncancel_xpath).click()
         time.sleep(5)
         self.driver.implicitly_wait(10)

