from Library import ConfigReader
from selenium.webdriver.common.by import By

class RegistrationClass:
    def __init__(self,obj):
         global driver
         driver = obj
         


    def enter_username(self,username):
            driver.find_element(By.XPATH,ConfigReader.fetchElementLocators("Registration","username")).send_keys(username)

    def enter_password(self,password):
        driver.find_element(By.XPATH,ConfigReader.fetchElementLocators("Registration","password")).send_keys(password) 