import time
from selenium import webdriver

driver = webdriver.Chrome(r'\path\chromedriver.exe')
driver.get("https://www.instagram.com")
time.sleep(10)

XPATH_USERNAME = '//*[@id="loginForm"]/div/div[1]/div/label/input'
XPATH_PASSWORD = '//*[@id="loginForm"]/div/div[2]/div/label/input'
XPATH_LOGIN = '//*[@id="loginForm"]/div/div[3]'

driver.find_element_by_xpath(XPATH_USERNAME).send_keys("username")
driver.find_element_by_xpath(XPATH_PASSWORD).send_keys("password")
driver.find_element_by_xpath(XPATH_LOGIN).click()
