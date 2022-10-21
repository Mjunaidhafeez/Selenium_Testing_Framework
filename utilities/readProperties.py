import configparser
config=configparser.RawConfigParser()
config.read('H:\\Selenium_Test_Project\Configuration\config.ini')

class ReadConfig:
    @staticmethod
    def getApplicaationURL():
        url=config.get('CommonInfo','baseURL')
        return url

    @staticmethod
    def getUsername():
        usernme=config.get('CommonInfo','username')
        return usernme

    @staticmethod
    def getPassword():
        password=config.get('CommonInfo','password')
        return password

    @staticmethod
    def get_login_sheet_path():
        login_path = config.get('CommonInfo', 'Login_Sheet')
        return login_path

    @staticmethod
    def get_patient_data_sheet_path():
        patient_data_path = config.get('CommonInfo', 'Patient_Data_Sheet')
        return patient_data_path
