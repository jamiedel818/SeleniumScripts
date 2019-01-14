#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 16:07:50 2018

@author: jamie
"""

import time
import secrets
from selenium import webdriver

#username
user = (secrets.x)

#password
pwd = (secrets.y)

#Chrome Driver
driverpath = "/Users/jamie/Downloads/chromedriver"
driver = webdriver.Chrome(driverpath)

#open gmail
driver.get("http://www.gmail.com")

#enter username
elem = driver.find_element_by_id("identifierId")
elem.send_keys(user)

driver.find_element_by_xpath("//*[@id='identifierNext']/content/span").click()
time.sleep(2)

#enter password
elem = driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")
elem.send_keys(pwd)
time.sleep(2)

driver.find_element_by_xpath("//*[@id='passwordNext']/content/span").click()
time.sleep(6)

z = 'ebay'
elem = driver.find_element_by_xpath('//*[@id="gbqfq"]')
elem.send_keys(z)
time.sleep(1)

driver.find_element_by_xpath('//*[@id="gbqfb"]/span').click()
time.sleep(2)

driver.find_element_by_xpath('//*[@id=":ii"]/div[1]/span/div').click()
time.sleep(1)

driver.find_element_by_xpath('//*[@id=":5"]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div/div').click()
driver.close



