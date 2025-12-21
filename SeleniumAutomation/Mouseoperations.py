from selenium.webdriver import Chrome   
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 

driver = Chrome()     #Object Created
driver.get("https://www.facebook.com")

act = ActionChains(driver)  #Create ActionChains object to perform keyboard actions or mouse actions in the same browser session

#Click Operations
act.click().perform()           #Clicks wherever the cursor is placed
act.click(driver.find_element(By.XPATH, "//input[@name='email']")).perform()  #Clicks on the element specified in the find_element method


#Context Click/Right Click Operations
# act.context_click().perform()   #Right click wherever the cursor is placed
# act.context_click(driver.find_element(By.XPATH, "//input[@name='email']")).perform() 

#Double Click Operations
act.double_click().perform()     #Double click wherever the cursor is placed
act.double_click(driver.find_element(By.XPATH, "//input[@name='email']")).perform()  #Double click on the element specified in the find_element method

#Hovering the mouse to an element
act.move_to_element(driver.find_element(By.XPATH, "//button[@name='login']")).perform()




input("Press Enter to close the browser...")