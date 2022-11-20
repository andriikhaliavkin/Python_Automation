import os
from selenium import webdriver
os.environ['PATH'] += r"C:\Users\khali\Desktop\projects\Python_Automation\chromedriver_win32"
driver = webdriver.Chrome()


url = "https://www.x-kom.pl/"
driver.get(url)
