from selenium.webdriver import Chrome
from Base import InitiateDriver
from Library import ConfigReader
from selenium.webdriver.common.by import By 
from Pages import registrationpage
import pytest
import openpyxl
from DataGenerator import Datagenforexceldata



@pytest.mark.parametrize('data',Datagenforexceldata.dataGenerator())
def test_Registration(data):
    driver = InitiateDriver.startbrowser() 
    register = registrationpage.RegistrationClass(driver)
    register.enter_username(data[0])
    register.enter_password(data[1])
    


    