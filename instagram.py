from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import hidden


class Instagram:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach",True)

        self.driver = webdriver.Chrome(options= self.options)

    def login(self):
        self.username = self.driver.find_element(By.XPATH,value = '//*[@id="loginForm"]/div/div[1]/div/label/input')
        self.username.send_keys("jakestasi92@gmail.com")

        self.password = self.driver.find_element(By.XPATH,value= '//*[@id="loginForm"]/div/div[2]/div/label/input')
        self.password.send_keys(hidden.gmail_password)

        enter = self.driver.find_element(By.XPATH,value = '//*[@id="loginForm"]/div/div[3]/button/div')
        enter.click()
    def search(self):
        david = self.driver.find_element(By.XPATH,value='//*[@id="mount_0_0_JI"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[2]/span/div/a/div/div[1]/div/div/svg')
        david.click()
        david.send_keys("David Goggins")

        goggins = self.driver.find_element(By.XPATH, value = '//*[@id="mount_0_0_qv"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]/div[1]/div/div/div[2]/div/div/div/span')
        goggins.click()

    def find_followers(self):
        find_followers = self.driver.find_element(By.CLASS_NAME,value="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _alvs _a6hd")
        find_followers.click()

        time.sleep(2)
        followers = self.driver.find_elements(By.CLASS_NAME,value="_ap3a _aaco _aacw _aacx _aad7 _aade")

        for x in followers:
            print(x.text)


