from selenium import webdriver
 
# Specify the location of ChromeDriver when instantiating

driver = webdriver.Chrome(r'\path\chromedriver.exe')
 
driver.get("https://facebook.com/login")

username_account = "enter your username or email adress here"

password = "enter your password here"

#xpath of were the user fill the mail or username

driver.find_element_by_xpath('//*[@id="email"]').send_keys(username_account)
  
#xpath where the user fill the password

driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
  
# xpath for clicking login/signing 

driver.find_element_by_xpath('//*[@id="loginbutton"]').click()
