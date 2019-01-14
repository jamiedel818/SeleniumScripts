#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 31 15:51:18 2018

@author: jamie
"""

import time
from selenium import webdriver
import secrets

username = (maggie.x)
pwd = (maggie.y)


def sakai_log():
    
    #Get driver path
    driverpath = "/Users/jamie/Downloads/chromedriver"
    driver = webdriver.Chrome(driverpath)
    driver.get('https://sakai.uri.edu/portal')
    
    #select element and type
    username_box = driver.find_element_by_id('eid')
    username_box.send_keys(username)
    time.sleep(2)
    
    #select element and type
    pwd_box = driver.find_element_by_id('pw')
    pwd_box.send_keys(pwd)
    time.sleep(2)
    
    #Click login
    login_button = driver.find_element_by_id('submit')
    login_button.submit()
    
    #How long we wait on the website before closing and re-opening
    time.sleep(5)
    driver.close()
    
    
count = 0

while count <= 5:
    sakai_log()
    #How long before it is executed again 
    time.sleep(5)
    count += 1
    
print("All done")

    
