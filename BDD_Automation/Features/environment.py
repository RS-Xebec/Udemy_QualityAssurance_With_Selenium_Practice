from selenium.webdriver import Chrome

def before_all(context):
    context.driver = Chrome()
def after_all(context):
    context.driver.close()


# def before_feature(context):
#     context.driver = Chrome()
# def after_feature(context):
#     context.driver.close() 
#Expalination:
#The before_feature and after_feature  are executed before and after each feature file, respectively.



# def before_scenario(context):
#     context.driver = Chrome()
# def after_scenario(context):
#     context.driver.close()
#The before_scenario and after_scenario are executed before and after each scenario, respectively.



# def before_tag(context):
#     context.driver = Chrome()
# def after_tag(context):
#     context.driver.close()
#The before_tag and after_tag are executed before and after each tag, respectively.



# def before_step(context):
#     context.driver = Chrome()
# def after_step(context):
#     context.driver.close()
# #The before_step and after_step are executed before and after each step, respectively.



#The following command is used to generate the report in xml format
# behave -f allure_behave.formatter:AllureFormatter -o "D:\UDEMY\BDD_Automation"




