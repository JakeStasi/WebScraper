from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from instagram import Instagram
import hidden


options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options)

driver.get("https://www.instagram.com/accounts/login/")
time.sleep(3)
username = driver.find_element(By.XPATH,value = '//*[@id="loginForm"]/div/div[1]/div/label/input')
username.send_keys("jakestasi92@gmail.com")

password = driver.find_element(By.XPATH,value= '//*[@id="loginForm"]/div/div[2]/div/label/input')
password.send_keys(hidden.gmail_password)

enter = driver.find_element(By.XPATH,value = '//*[@id="loginForm"]/div/div[3]/button/div')
enter.click()

driver.get("https://www.instagram.com/davidgoggins/followers/")

time.sleep(3)

followers = driver.find_elements(By.CLASS_NAME,value = "_ap3a _aaco _aacw _aacx _aad7 _aade")

for x in followers:
    print(x.text)