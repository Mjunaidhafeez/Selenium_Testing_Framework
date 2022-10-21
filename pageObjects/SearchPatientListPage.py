from selenium.webdriver.common.by import By


class Searchpatients:
    btndashboard_id="patientTab_0"
    btnallpatients_xpath='//*[@id="awv_dashboard_form"]/div/div[3]/div/div[3]/div/div/div/div[1]/span'
    txtsearch_id='basicSearchInput'
    btnsearch_xpath='//*[@id="homeTabView"]/div[1]/div[1]/button[1]'
    table_path=''
    tableRows_path=''
    tabelColumns_path=''
    def __init__(self,driver):
        self.driver=driver

    def getNoOfRows(self):
       return len(self.driver.find_element(By.XPATH,self.tableRows_path))
    def getNoOfColumns(self):
       return len(self.driver.find_element(By.XPATH,self.tabelColumns_path))

    def searchPatientByEmail(self,email):
        flag=False
        for r in range(1,self.getNoOfColumns()+1):
            table=self.driver.find_element(By.XPATH,self.table_path) #searching of patient from patitient table by patient name,email,phone,etc
            emailid=table.driver.find_element(By.XPATH,'').text
            if emailid==email:
                flag=True
                break
        return flag #return true ofr false if patient is present or not in the table



