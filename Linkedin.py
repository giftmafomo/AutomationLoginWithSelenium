import time
from selenium import webdriver

driver = webdriver.Chrome(r'\path\chromedriver.exe')
driver.get("https://www.linkedin.com/login")
time.sleep(30)

XPATH_USERNAME = '//*[@id="username"]'
XPATH_PASSWORD = '//*[@id="password"]'
XPATH_LOGIN = '//*[@id="organic-div"]/form/div[3]/button'

driver.find_element_by_xpath(XPATH_USERNAME).send_keys("email")
driver.find_element_by_xpath(XPATH_PASSWORD).send_keys("password")
driver.find_element_by_xpath(XPATH_LOGIN).click()
