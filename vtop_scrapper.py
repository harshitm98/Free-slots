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
time.sleep(3)
driver.find_element_by_xpath('//*[@id="idOf4"]').click()
time.sleep(10)
driver.find_element_by_xpath('//*[@id="semesterSubId"]/option[2]').click()
driver.find_element_by_xpath('//*[@id="studentTimeTable"]/div/div[2]/div/button').click()
time.sleep(10)

# Going through the slots
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

# Creating or updating the excel file
singled_out_slots = []
for slot in slots:
    if('+' in slot):
        splitted_slot = slot.split('+')
        for i in splitted_slot:
            singled_out_slots.append(i)
    else:
        singled_out_slots.append(slot)
        
# Removing duplicate values
singled_out_cleaned = []
for slot in singled_out_slots:
    if slot not in singled_out_cleaned:
        singled_out_cleaned.append(slot)

# Turning them in terms of lab slots
converted_lab_slot = []
for slot in singled_out_cleaned:
    if slot == 'A1':
        converted_lab_slot.append('L1')
        converted_lab_slot.append('L14')
    elif slot == 'TA1':
        converted_lab_slot.append('L27')
    elif slot == 'TAA1':
        converted_lab_slot.append('L11')
    
    elif slot == 'A2':
        converted_lab_slot.append('L31')
        converted_lab_slot.append('L44')
    elif slot == 'TA2':
        converted_lab_slot.append('L57')
    elif slot == 'TAA2':
        converted_lab_slot.append('L41')
    
    elif slot == 'B1':
        converted_lab_slot.append('L7')
        converted_lab_slot.append('L20')
    elif slot == 'TB1':
        converted_lab_slot.append('L4')
    
    elif slot == 'B2':
        converted_lab_slot.append('L37')
        converted_lab_slot.append('L50')
    elif slot == 'TB2':
        converted_lab_slot.append('L34')
    elif slot == 'TBB2':
        converted_lab_slot.append('L47')
        
    elif slot == 'C1':
        converted_lab_slot.append('L13')
        converted_lab_slot.append('L26')
    elif slot == 'TC1':
        converted_lab_slot.append('L10')
    elif slot == 'TCC1':
        converted_lab_slot.append('L23')
    
    elif slot == 'C2':
        converted_lab_slot.append('L43')
        converted_lab_slot.append('L56')
    elif slot == 'TC2':
        converted_lab_slot.append('L40')
    elif slot == 'TCC2':
        converted_lab_slot.append('L53')
        
    elif slot == 'D1':
        converted_lab_slot.append('L19')
        converted_lab_slot.append('L3')
    elif slot == 'TD1':
        converted_lab_slot.append('L29')
    
    elif slot == 'D2':
        converted_lab_slot.append('L49')
        converted_lab_slot.append('L33')
    elif slot == 'TD2':
        converted_lab_slot.append('L46')
    elif slot == 'TDD2':
        converted_lab_slot.append('L59')
        
    elif slot == 'E1':
        converted_lab_slot.append('L9')
        converted_lab_slot.append('L25')
    elif slot == 'TE1':
        converted_lab_slot.append('L22')
    
    elif slot == 'E2':
        converted_lab_slot.append('L39')
        converted_lab_slot.append('L55')
    elif slot == 'TE2':
        converted_lab_slot.append('L52')
        
    elif slot == 'F1':
        converted_lab_slot.append('L2')
        converted_lab_slot.append('L15')
    elif slot == 'TF1':
        converted_lab_slot.append('L28')
    
    elif slot == 'F2':
        converted_lab_slot.append('L32')
        converted_lab_slot.append('L45')
    elif slot == 'TF2':
        converted_lab_slot.append('L58')
        
    elif slot == 'G1':
        converted_lab_slot.append('L8')
        converted_lab_slot.append('L21')
    elif slot == 'TG1':
        converted_lab_slot.append('L5')
    
    elif slot == 'G2':
        converted_lab_slot.append('L38')
        converted_lab_slot.append('L51')
    elif slot == 'TG2':
        converted_lab_slot.append('L35')
        
    elif slot == 'V1':
        converted_lab_slot.append('L16')
        
    elif slot[0] == 'L':
        converted_lab_slot.append(slot)
    else:
        converted_lab_slot.append(slot)
    print(slot, converted_lab_slot[-1])
converted_lab_slot.sort()
print(converted_lab_slot)

# Writing to the excel file