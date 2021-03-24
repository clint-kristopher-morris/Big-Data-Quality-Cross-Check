import os, sys, time
import json, requests, shutil
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import pyperclip
from selenium.common.exceptions import StaleElementReferenceException, WebDriverException, NoSuchElementException

def waitclick(xpath):
    r= None 
    while r is None:
        try:
            r=driver.find_element_by_xpath(xpath)
            r.click()
        except NoSuchElementException:
#             print('Needs more loading time: 3 more seconds were added')
            time.sleep(1)
            
def resultwait(xpath):
    r= None 
    while r is None:
        try:
            r=driver.find_element_by_xpath(xpath)
            return r
        except NoSuchElementException:
#             print('Needs more loading time: 1 more seconds were added')
            time.sleep(1)

url = f'http://navigator-atms.dot.ga.gov'
driver = webdriver.Firefox()
driver.get(url)

# Find user input
input1 = resultwait(f'//*[@id="loginUsername"]')
pyperclip.copy("username")
input1.send_keys(Keys.CONTROL,'v')

# Find password input
input2 = resultwait(f'//*[@id="loginPassword"]')
pyperclip.copy("pass")
input2.send_keys(Keys.CONTROL,'v')

#remote server
waitclick('/html/body/center/div/form/div/center/div/table/tbody/tr[5]/td/select/option[14]')
#login
waitclick('/html/body/center/div/form/div/center/div/table/tbody/tr[7]/td/input')

# let the program load and select list
time.sleep(20)
result = None
while result is None:
    try:
        driver.switch_to.window(driver.window_handles[-1])
        pass_finder_xp = f'/html/body/table/tbody/tr[1]/td[2]/div/a[7]'
        driver.find_element_by_xpath(pass_finder_xp).click()
        result = True
    except NoSuchElementException:
        print('Needs more loading time: 15 more seconds were added')
        time.sleep(15)
        
time.sleep(15)        
#VDS tab
waitclick('//*[@id="customSwitcherLinkVDS_Inventory"]')
time.sleep(15) 
#drop-down
waitclick('//*[@id="selectButtonInventory"]')

info = {'value':[],
        'VDS_type':[],
        'description':[],
        'Latitude':[],
        'Longitude':[]}

time.sleep(5)
result = None
i = 10300
while result is None:
    try:
        pass_finder_xp = f'/html/body/div[2]/div[3]/div/div[2]/select/option[{i}]'
        item = driver.find_element_by_xpath(pass_finder_xp)
        item.location_once_scrolled_into_view
        value = item.get_attribute("value")
        info['value'].append(value)
        info['description'].append(item.text)
        item.click()
        time.sleep(0.05)
        print(value)
        lat = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/form/div[3]/table[1]/tbody/tr[1]/td[2]/span')
        info['Latitude'].append(lat.text)
        long = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/form/div[3]/table[1]/tbody/tr[2]/td[2]/span')
        info['Longitude'].append(long.text)
        vds = driver.find_element_by_xpath(f'//*[@id="readonly_configInput.VdsTypeInventory"]')
        info['VDS_type'].append(vds.text)
        i += 1
        
    except NoSuchElementException:
        print('Needs more loading time: 15 more seconds were added')
        time.sleep(0.5)
