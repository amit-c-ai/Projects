from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E
from selenium.webdriver import ActionChains as A
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys as K
from random import seed
from random import randint
from selenium.webdriver.common.proxy import Proxy, ProxyType
import xlrd
import xlwt
from xlutils.copy import copy
import time 
import datetime
import re
import schedule
from datetime import timedelta
import pyautogui as P
import pyperclip as pc

#exec_path='\Users\amitc\'
URL='https://inderpsingh.blogspot.com/2014/08/demowebapp_24.html'
distance_id_locator="distance"
wait_time_out = 15
driver = webdriver.Chrome('chromedriver.exe') 
wait_variable = W(driver, wait_time_out)
driver.get(URL)
#h2='//*[@id="distance"]'
distance_element = driver.find_element_by_id('distance')
distance_element.send_keys("")
P.write("123456")
P.hotkey("ctrl", "a")
P.hotkey("ctrl", "c")
time.sleep(1)
P.press("tab")
P.hotkey("ctrl", "v")
data=pc.paste()
print(data)
'''speed=driver.find_element_by_xpath('//*[@id="BlogSearch1_form"]/form/table/tbody/tr/td[1]/input').text
print("speedis :",speed)'''
