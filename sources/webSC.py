from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException


#Create new instance of Chrome in Incognito mode

option = webdriver.ChromeOptions()
option.add_argument(' — incognito')

#reate a new instance of Chrome

browser = webdriver.Chrome(executable_path='/Users/book/Desktop/chromedriver', chrome_options=option)

#Open a link
link = "https://www.yahoo.com"
browser.get(link)
