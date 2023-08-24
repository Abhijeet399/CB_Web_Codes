from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("../Drivers/chromedriver.exe")


driver.get("https://www.google.com")
time.sleep(1)

textfield = driver.find_element(By.NAME, "q")
#textfield = driver.find_element_by_name("q") #find_element_by_xpath("//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input")

textfield.send_keys("Hello world" + Keys.RETURN)
time.sleep(2)

home_button = driver.find_element(By.ID, "logo")
#home_button = driver.find_element_by_id("logo")

home_button.click()
#home_button.send_keys()
time.sleep(2)

driver.quit()