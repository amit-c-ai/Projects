import selenium
from selenium import webdriver
from selenium import common
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
import os, time
import pyautogui
name=input("Name: ").upper()
print(name)
date= input("Date(dd/mm/yy): ")
d1 = date.split('/')
print(d1)

browser = webdriver.Chrome(executable_path=os.path.join(os.getcwd(), 'chromedriver'))

#change url below
browser.get("https://docs.google.com/forms/d/e/1FAIpQLScQYYWBe1WWq8OVdU4AzLGSoG-9mcBTmA0R3CYnRUbdfQxxsQ/formResponse")

pyautogui.press('tab')
time.sleep(0.3)
pyautogui.press('tab')
time.sleep(0.3)

pyautogui.keyDown('shift')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.keyUp('shift')
time.sleep(0.3)
pyautogui.write(d1[0])
time.sleep(0.5)
pyautogui.write(d1[1])
time.sleep(0.5)
pyautogui.write(d1[2])

nextbutton = browser.find_element_by_class_name("appsMaterialWizButtonPaperbuttonLabel")

time.sleep(0.5)
nextbutton.click()
time.sleep(0.5)

radiobuttons = browser.find_elements_by_class_name("appsMaterialWizToggleRadiogroupOffRadio")
textboxes = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
submitbuttons = browser.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonContent")

for i in range(0, len(radiobuttons), 2):
    try:
        radiobuttons[i].click()
        time.sleep(0.2)
    except selenium.common.exceptions.ElementNotInteractableException:
        continue

time.sleep(0.3)
textboxes[0].send_keys(name)
time.sleep(0.5)

submitbuttons[1].click()

browser.close()



#option = webdriver.ChromeOptions()
#option.add_argument('--disable-web-security')
#option.add_argument('--user-data-dir')
#option.add_argument('--allow-running-insecure-content')
#option.add_argument("-incognito")
#option.add_experimental_option("excludeSwitches", ['enable-automation']);
#option.add_argument("--headless")
#option.add_argument("disable-gpu")
#bot = webdriver.Firefox(executable_path= os.path.join(os.getcwd(), 'geckodriver') )     #, options=option)
#bot = webdriver.Firefox(executable_path=GeckoDriverManager().install())
