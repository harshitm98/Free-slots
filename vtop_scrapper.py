# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 09:24:11 2018

@author: Harshit Maheshwari
"""

# Getting inside the VTOP pop up
# Opening VtopBeta with chrome and the following extension
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_argument('--load-extension=C:/Users/Ambika/AppData/Local/Google/Chrome/User Data/Default/Extensions/hafeeaangmkbibcaahfjdmmmeappjbbp/2.4_0')
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://vtopbeta.vit.ac.in/vtop/')

# Setting up main_window_handle so that it can be changed when the pop up opens
main_window_handle = None
while not main_window_handle:
    main_window_handle = driver.current_window_handle

# Opening login page
vtopLogin = driver.find_element_by_xpath('/html/body/div/div[2]/div/section/div[2]/div[1]/div/div[2]/button')
vtopLogin.click()

# Changing the focus on to the pop up
signin_window_handle = None
while not signin_window_handle:
    for handle in driver.window_handles:
        if handle != main_window_handle:
            signin_window_handle = handle
            break
driver.switch_to_window(signin_window_handle)

# Filling up the fields and logging in
username = input("Enter the username: ")
password = input("Enter the password: ")

usernameField = driver.find_element_by_xpath('//*[@id="uname"]')
passwordFeild = driver.find_element_by_xpath('//*[@id="passwd"]')

usernameField.send_keys(username)
passwordFeild.send_keys(password)

signIn = driver.find_element_by_xpath('//*[@id="form-signin_v1"]/div[4]/div[2]/button')
signIn.click()

# Opening the timetable
time.sleep(10)
driver.find_element_by_xpath('//*[@id="page-content"]/header/nav/a').click()
driver.find_element_by_xpath('//*[@id="dbMenu"]/ul/li[2]/a').click()
driver.find_element_by_xpath('//*[@id="idOf4"]').click()
time.sleep(10)
driver.find_element_by_xpath('//*[@id="semesterSubId"]/option[2]').click()
driver.find_element_by_xpath('//*[@id="studentTimeTable"]/div/div[2]/div/button').click()
time.sleep(10)

i = 3
slots = []
while True:
    try:
        ids = '//*[@id="studentDetailsList"]/table/tbody/tr['+str(i)+']/td[9]/p'
        slot = driver.find_element_by_xpath(ids).text
        slots.append(slot)
        i += 1
    except NoSuchElementException:
        print(slots)
        break

# Successfully logging out    
driver.find_element_by_xpath('//*[@id="page-content"]/header/nav/div/ul/li/a').click()
driver.find_element_by_xpath('//*[@id="btnLogout"]').click()