from behave import *
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By 


@given(u'User is on Registration Page')
def step_impl(context):
   
   context.driver.get("https://www.facebook.com/r.php?entry_point=login")
  


@when(u'User enters username')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//input[@type='text' and @name='firstname']").send_keys("testing")


@when(u'User enters email id')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//input[@type='text' and @name='reg_email__']").send_keys("testingusername@gmail.com") 

@when(u'User enters password')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//input[@type='password' and @name='reg_passwd__']").send_keys("testing123password")


@when(u'User click on signup button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//button[@type='submit' and @name='websubmit']").click()


@then(u'User should be registered successfully')
def step_impl(context):
    print("User registered successfully")

@when(u'User enters duplicate username')
def step_impl(context):
    print("Not Registered")
