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
pyautogui.FAILSAFE= False
name=input("Name: ").upper()
print(name)

date=input("Date(dd/mm/yy): ")
d1 = date.split('/')
print(d1)

browser = webdriver.Chrome(executable_path=os.path.join(os.getcwd(), 'chromedriver'))

browser.get("https://docs.google.com/forms/d/e/1FAIpQLSdQ-sJWYyoGZny9ZD-PmPTXrkfiSW0dhg5vj58iDSUws3KYpA/formResponse")

time.sleep(1)
nextbutton = browser.find_element_by_class_name("appsMaterialWizButtonPaperbuttonLabel")
nextbutton.click()
time.sleep(1)
radiobuttons = browser.find_elements_by_class_name("appsMaterialWizToggleRadiogroupOffRadio")
textboxes = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
submitbuttons = browser.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonContent")
try:
    pyautogui.press('tab')
    time.sleep(0.5)

except pyautogui.FailSafeException:
    pyautogui.press('tab')
    time.sleep(0.5)


pyautogui.write(d1[0])
time.sleep(0.2)
pyautogui.write(d1[1])
time.sleep(0.2)
pyautogui.write(d1[2])
time.sleep(0.2)
radiobuttons[0].click()
time.sleep(0.2)
radiobuttons[5].click()
time.sleep(1)
textboxes[1].send_keys(name)
time.sleep(0.2)
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
