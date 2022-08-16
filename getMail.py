#Getting temp mail from internet

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
 

driver = webdriver.Chrome(executable_path="D:\snapchat\chromedriver.exe")
driver.maximize_window()

url = "https://10minutemail.net/?lang=tr"
driver.get(url)

time.sleep(5)

copy_click = driver.find_element(By.CSS_SELECTOR , "#copy-button").click()

url2 = "https://www.google.com.tr/"
driver.get(url2)

mail = driver.find_element(By.XPATH , "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")

act = ActionChains(driver)
act.key_down(Keys.CONTROL).send_keys('V').key_up(Keys.CONTROL).perform() #Paste
