from selenium import webdriver
 
# Specify the location of ChromeDriver when instantiating

driver = webdriver.Chrome(r'C:\Users\mafom\Downloads\chromedriver_win32\chromedriver.exe') 

driver.get("https://tiktok.com/login")

username_account = "enter your username/email"

password = "enter your password"


# To navigate the xpath of the username: 

# firstly, move your mouse to the username botton

# press right click - inspect

# from copy go to copy xpath 

# press right click to copy the xpath  

# lastly, paste the xpath  of the id element below 

driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username_account)
  
  
# To navigate the xpath of the password:

# firstly move your mouse to the password botton

# press right click - inspect

# from copy go to copy xpath 

# press right click to copy the xpath  

# lastly, paste the xpath  of the id element below 

driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
  

# xpath for clicking login/signing: 

# To navigate the xpath of the login/signing:

# firstly move your mouse to the login botton

# press right click - inspect

# from copy go to copy xpath 

# press right click to copy the xpath 
 
# lastly, paste the xpath  of the id element below

driver.find_element_by_xpath('//*[@id="loginbutton"]').click()

