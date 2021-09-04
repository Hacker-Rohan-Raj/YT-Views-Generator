import selenium
from selenium import webdriver
import time

views = input('Enter How many views do You Want')
time.sleep(2)
videolink = input('Enter the Link of Your Video')
chromedriver = input('Enter the Path of Your Chrome Driver')



driver = webdriver.Chrome(chromedriver)

for i in range(views):
    driver.get(videolink)
    time.sleep(3)
    driver.refresh()
