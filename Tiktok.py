import time
from selenium import webdriver

driver = webdriver.Chrome(r"\path\chromedriver.exe")
driver.get("https://www.tiktok.com/login")
time.sleep(30)

XPATH_CONTINUEWITHFACEBOOK = '//*[@id="root"]/div/div[1]/div/div[1]/div[2]/div[3]/div[2]'
XPATH_EMAILORPHONE= '//*[@id="email"]'
XPATH_PASSWORD = '/*[@id="pass"]'
XPATH_LOGIN = '//*[@id="loginbutton"]'

elemCont =driver.find_element_by_xpath(XPATH_CONTINUEWITHFACEBOOK)
elemCont.click()
time.sleep(30)

elemEmail = driver.find_element_by_xpath(XPATH_EMAILORPHONE)
elemEmail.send_keys("email or phone")

elemPassword = driver.find_element_by_xpath(XPATH_PASSWORD)
elemPassword.send_keys("password")

elemLogin = driver.find_element_by_xpath(XPATH_LOGIN)
elemLogin.click()
