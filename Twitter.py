from selenium import webdriver

import time
# Specify the location of ChromeDriver when instantiating

driver = webdriver.Chrome(r'\path\chromedriver.exe') 

driver.get("https://twitter.com/i/flow/login")

time.sleep(30)

username = "enter your username or email address"

password = "enter your password"

elemUser = driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input')
elemUser.send_keys(username)           
time.sleep(10)

elemNext= driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div/span/span')
elemNext.click()


elemPasswd = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input')
elemPasswd.send_keys(password)


elemLogin = driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/span/span')
elemLogin.click()


