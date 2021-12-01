from selenium import webdriver
 
# Specify the location of ChromeDriver when instantiating

driver = webdriver.Chrome(r'/path/to/chromedriver') 

driver.get("https://github.com/login")

username_account = "enter your username/email"

password = "enter your password"

# Xpath of where the user will fill the mail or username

driver.find_element_by_xpath('//*[@id="login_field"]').send_keys(username_account)
  
# Xpath where the user fill the password

driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
  
# Xpath for clicking login/signing 

driver.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[12]').click()
