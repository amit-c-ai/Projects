#############################################################
# @package Youtube-Bot --- Python                           #
# @author Amit                                              #
#############################################################


from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
serial = []
start_time = []
title = []
desc = []
status = []
duration = []
in_time = []
changes = []
days = ["monday.xls","tuesday.xls","wednesday.xls","thursday.xls","friday.xls","saturday.xls","sunday.xls"]
dayname = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]


#Function for extracting data from Excel file
def excelinput(day):
    loc = (day)
    print(loc)
    wb = xlrd.open_workbook(loc) 
    sheet = wb.sheet_by_index(0)
    w = copy(wb)
    
    
    
    for i in range(sheet.nrows):
        if(i!=0):
            x = sheet.cell_value(i, 2)
            x = int(x * 24 * 3600)
            my_time = datetime.time(x//3600, (x%3600)//60)
            my_time1 = str(my_time)
            #print(my_time1)
            start_time.append(''.join(my_time1.rsplit(':00', 1)))
            
    for i in range(sheet.nrows):
        if(i!=0):
            x = sheet.cell_value(i, 3)
            title.append(x)

    for i in range(sheet.nrows):
        if(i!=0):
            x = sheet.cell_value(i, 4)
            desc.append(x)
            
    
    for i in range(sheet.nrows):
        if(i!=0):
            x = sheet.cell_value(i, 5)
            status.append(x)

    for i in range(sheet.nrows):
        if(i!=0):
            x = sheet.cell_value(i, 6)                
            duration.append(x)
            
            
    for i in range(sheet.nrows):
        if(i!=0):
            x = sheet.cell_value(i, 7)
            intime = x
            intime =''.join(intime.rsplit(':00', 1))
            intime= re.sub(':|l', ':', intime)
            in_time.append(intime)
            #print(intime,in_time)
    
    for i in range(sheet.nrows):
        if(i!=0):
            x = sheet.cell_value(i, 0)
            serial.append(x)

    for s in range(2):
        for i in range(sheet.nrows):
            for j in range(sheet.ncols):
                if(i!=0 and (j==1 or j==2)):
                    x = sheet.cell_value(i, j)
                    x = int(x * 24 * 3600)
                    my_time = datetime.time(x//3600, (x%3600)//60)
                    my_time1 = str(my_time)
                    w.get_sheet(s).write(i,j,my_time1)
       
    w.save('new'+day)

#Xpaths to interact with Youtibe
createHighlight_x = '//*[@id="button"]/yt-icon'
title_x = '//*[@id="input-27"]/input'
description_x = '//*[@id="textarea"]'
in_time_x = '/html/body/ytcp-app/ytls-popup-container/paper-dialog/ytls-live-highlight-editor-renderer/div[3]/div[1]/div/ytve-framestamp-input[1]/div/ytve-formatted-input/input'
cancel_x = '//*[@id="text"]'
cancel1_x = '/html/body/ytcp-app/ytls-popup-container/paper-dialog/ytls-live-highlight-editor-renderer/div[7]/div[1]/ytls-button-renderer/a/paper-button/yt-formatted-string'
title_x = '/html/body/ytcp-app/ytls-popup-container/paper-dialog/ytls-live-highlight-editor-renderer/div[6]/ytls-metadata-collection-renderer/div[2]/ytls-metadata-control-renderer[1]/div/ytls-mde-title-renderer/paper-input/paper-input-container/div[2]/div/iron-input/input'
status_x = '/html/body/ytcp-app/ytls-popup-container/paper-dialog/ytls-live-highlight-editor-renderer/div[6]/ytls-metadata-collection-renderer/div[2]/ytls-metadata-control-renderer[2]/div/ytls-dropdown-renderer/div/paper-dropdown-menu/paper-menu-button/div/div/paper-input/paper-input-container/div[2]/div/iron-input/input'
status_public_x = '/html/body/ytcp-app/ytls-popup-container/paper-dialog/ytls-live-highlight-editor-renderer/div[6]/ytls-metadata-collection-renderer/div[2]/ytls-metadata-control-renderer[2]/div/ytls-dropdown-renderer/div/paper-dropdown-menu/paper-menu-button/iron-dropdown/div/div/paper-listbox/paper-item[1]/paper-item-body'
status_private_x = '/html/body/ytcp-app/ytls-popup-container/paper-dialog/ytls-live-highlight-editor-renderer/div[6]/ytls-metadata-collection-renderer/div[2]/ytls-metadata-control-renderer[2]/div/ytls-dropdown-renderer/div/paper-dropdown-menu/paper-menu-button/iron-dropdown/div/div/paper-listbox/paper-item[3]/paper-item-body'
status_unlisted_x = '/html/body/ytcp-app/ytls-popup-container/paper-dialog/ytls-live-highlight-editor-renderer/div[6]/ytls-metadata-collection-renderer/div[2]/ytls-metadata-control-renderer[2]/div/ytls-dropdown-renderer/div/paper-dropdown-menu/paper-menu-button/iron-dropdown/div/div/paper-listbox/paper-item[2]/paper-item-body'
desc_x = '/html/body/ytcp-app/ytls-popup-container/paper-dialog/ytls-live-highlight-editor-renderer/div[6]/ytls-metadata-collection-renderer/div[2]/ytls-metadata-control-renderer[3]/div/ytls-mde-description-renderer/paper-textarea/paper-input-container/div[2]/div/iron-autogrow-textarea/div[2]/textarea'
create_x = '/html/body/ytcp-app/ytls-popup-container/paper-dialog/ytls-live-highlight-editor-renderer/div[7]/div[2]/ytls-button-renderer/a/paper-button/yt-formatted-string'




#Function to automate the Task on Youtube
def job(title,status,desc,in_time,dura):
    print("I'm working...")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("user-data-dir=C:\\Users\\Os\\Desktop\\youtube bot\\User Data")
    chrome_options.add_argument('profile-directory=Profile 5')   
    driver = webdriver.Chrome(executable_path='C:\\Users\\Os\\Desktop\\youtube bot\\chromedriver.exe',options=chrome_options)
    driver.get('https://studio.youtube.com/video/azAVZYrJrAA/livestreaming')
    time.sleep(15)
    h1 = driver.find_element_by_xpath(createHighlight_x)
    h1.click()
    time.sleep(7)
    h2 = driver.find_element_by_xpath(cancel1_x)
    h2.click()
    h3 = driver.find_element_by_xpath(createHighlight_x)
    h3.click()
    time.sleep(5)
    
    h4 = driver.find_element_by_xpath(in_time_x)
    
    time.sleep(5)
    
    h4.send_keys(Keys.CONTROL,'a')
    intime_content = h4.send_keys(Keys.CONTROL, 'c')       #if not worked use driver.find_element_by_xpath(in_time_x).send_keys(Keys.CONTROL, "a")
    hr=int(intime_content[i].split(':')[0])
    mins=int(intime_content[i].split(':')[1])
    t1=timedelta(hours=hr,minutes=mins)
    dura=int(dura)
    t2=timedelta(hours=0,minutes=dura)
    diff=t1-t2
    h4.send_keys(diff)

    h5 = driver.find_element_by_xpath(title_x)
    h5.send_keys(title)
    h6 = driver.find_element_by_xpath(status_x)
    h6.click()
    statuslower = status.lower()
    if(statuslower == 'public'):
        h7 = driver.find_element_by_xpath(status_public_x)
        h7.click()
    if(statuslower == 'private'):
        h8 = driver.find_element_by_xpath(status_private_x)
        h8.click()
    if(statuslower == 'unlisted'):
        h9 = driver.find_element_by_xpath(status_unlisted_x)
        h9.click()
    h10 = driver.find_element_by_xpath(desc_x)
    h10.send_keys(desc)
    time.sleep(2)
    h11 = driver.find_element_by_xpath(create_x)
    h11.click()
    time.sleep(5)
    driver.close()
    

print ("Hey program Started........:)")
print ("Jobs Scheduled. will run on their time.......:)")
print ("Please Exit the bot manually after 10 mins of last task......:)")

for day in (days):
    # excelinput(days[i])
    dayname= re.sub('.xlsx|l', '', day)
    start_time.clear()
    title.clear()
    desc.clear()
    status.clear()
    in_time.clear()
    serial.clear()
    dura.clear()
    
    
    excelinput(day)
    #Scheduling for Tasks
    for x in serial:
        i = int(x) - 1
        starttime = start_time[i]
        title1 = title[i]
        status1 = status[i]
        desc1 = desc[i]
        in_time1 = in_time[i]
        dura = duration[i]
        print('Will start at :', starttime,'intime1',in_time1)
        if(dayname == 'monday'): 
            schedule.every().monday.at(starttime).do(job,title1,status1,desc1,in_time1, dura)
        if(dayname == 'tuesday'):   
            schedule.every().tuesday.at(starttime).do(job,title1,status1,desc1,in_time1, dura)
        if(dayname == 'wednesday'):  
            schedule.every().wednesday.at(starttime).do(job,title1,status1,desc1,in_time1, dura)
        if(dayname == 'thursday'): 
            schedule.every().thursday.at(starttime).do(job,title1,status1,desc1,in_time1, dura)
        if(dayname == 'friday'): 
            schedule.every().friday.at(starttime).do(job,title1,status1,desc1,in_time1, dura)
        if(dayname == 'saturday'):  
            schedule.every().saturday.at(starttime).do(job,title1,status1,desc1,in_time1, dura)
        if(dayname == 'sunday'):   
            schedule.every().sunday.at(starttime).do(job,title1,status1,desc1,in_time1, dura)        

while 1:
    schedule.run_pending()
    time.sleep(1)


'''    
    h4.send_keys("")
    P.hotkey("ctrl", "a")
    intime_content = P.hotkey("ctrl", "c")
    final = intime_content-dura
    P.write(final)
    time.sleep(1)

    
    h4.send_keys(in_time)'''
