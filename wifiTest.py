import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import hidden

home_download = 200
home_upload = 200

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options)

driver.get("https://www.speedtest.net/")


internet = driver.find_element(By.CLASS_NAME,value = "start-text")
internet.click()

time.sleep(65)
download = driver.find_element(By.XPATH,value = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
download_speed = float(download.text)

upload = driver.find_element(By.XPATH,value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
upload_speed = float(upload.text)

if download_speed < home_download or upload_speed < home_upload:

    driver.get("https://x.com/i/flow/login")

    time.sleep(3)
    login = driver.find_element(By.XPATH, value = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
    login.send_keys("jakestasi92@gmail.com",Keys.ENTER)

    time.sleep(3)
    login2 = driver.find_element(By.XPATH,value = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
    login2.send_keys(hidden.phone_no,Keys.ENTER)

    time.sleep(3)
    password = driver.find_element(By.XPATH,value = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    password.send_keys(hidden.password,Keys.ENTER)


    time.sleep(3)
    post = driver.find_element(By.XPATH,value= '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
    post.send_keys(f"My internet speed is suppose to be {home_download} mbps and {home_upload} mbps not {download_speed} and {upload_speed} >:( ")


