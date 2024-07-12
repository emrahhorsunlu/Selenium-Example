# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 22:11:02 2024

@author: emrah
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome()

driver.get("testurl/")
driver.implicitly_wait(30)

driver.find_element(By.CSS_SELECTOR, '[id="user-message"]').send_keys("Selenium Test Edildi")
sleep(0.5)
driver.find_element(By.CSS_SELECTOR, '[id="showInput"]').click()
response = driver.find_element(By.CSS_SELECTOR, '[id="message"]').text
print(f"Sistem Mesajı = {response} ")

driver.find_element(By.CSS_SELECTOR, '[id="sum1"]').send_keys("10")
driver.find_element(By.CSS_SELECTOR, '[id="sum2"]').send_keys("20")
driver.find_element(By.CSS_SELECTOR, '[id="gettotal"] [type="button"]').click()
response = driver.find_element(By.CSS_SELECTOR, '[id="addmessage"]').text
print(f'Response : {response}')
sleep(3000)



