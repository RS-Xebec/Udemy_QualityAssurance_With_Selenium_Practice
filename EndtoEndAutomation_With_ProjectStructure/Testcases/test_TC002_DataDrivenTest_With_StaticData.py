from selenium.webdriver import Chrome
from Base import InitiateDriver
from Library import ConfigReader
from selenium.webdriver.common.by import By 
from Pages import registrationpage
import pytest

def dataGenerator():
    li = [['user1','pass1'],['user2','pass2'],['user3','pass3']]
    return li

@pytest.mark.parametrize('data',dataGenerator())
def test_InvalidRegistration(data):
    driver = InitiateDriver.startbrowser() 
    register = registrationpage.RegistrationClass(driver)
    register.enter_username(data[0])
    register.enter_password(data[1])

    