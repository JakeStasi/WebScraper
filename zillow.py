from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#automated webscraper that searches home prices on zillow and stores the price, the link, and the address via a google form 

GOOGLE_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSdweo60pWUzpoQZJMo8CetJkIVnM3gVa7Zw0_anJHdAzn8QjQ/viewform?usp=sf_link"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options)



driver.get("https://appbrewery.github.io/Zillow-Clone/")

links = driver.find_elements(By.CLASS_NAME,value="property-card-link")
links = [x.get_attribute("href") for x in links]



prices = driver.find_elements(By.CLASS_NAME,value = "PropertyCardWrapper__StyledPriceLine")
prices = [x.text.strip(" + /mo 1 bd") for x in prices]



addresses = driver.find_elements(By.CSS_SELECTOR,value="address")
addresses = [x.text for x in addresses]


driver.get(GOOGLE_FORM)
time.sleep(3)
send_address = driver.find_element(By.XPATH,value= '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
send_price = driver.find_element(By.XPATH,value= '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
send_link = driver.find_element(By.XPATH,value= '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
submit = driver.find_element(By.XPATH,value = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')


for x in range (len(prices)):
    send_address = driver.find_element(By.XPATH,
                                       value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    send_price = driver.find_element(By.XPATH,
                                     value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    send_link = driver.find_element(By.XPATH,
                                    value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    send_address.send_keys(f"{addresses[x]}")
    send_price.send_keys(f"{prices[x]}")
    send_link.send_keys(f"{links[x]}")
    submit.click()
    time.sleep(2)
    another_response = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response.click()
    time.sleep(1)



















