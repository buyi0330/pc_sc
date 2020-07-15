#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time


# Please change the below path if you are using WINDOWS!!!!!
driver = webdriver.Chrome(executable_path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver.get('http://127.0.0.1:8000')     # "get"
username=driver.find_element_by_xpath('//*[@id="id_username"]')
password=driver.find_element_by_xpath('//*[@id="id_password"]')
username.send_keys('alice')
password.send_keys('alice')
submit=driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input')
submit.click()
time.sleep(1)

driver.find_element_by_xpath('//*[@id="content-main"]/div[2]/table/tbody/tr[3]/td[1]/a').click()#add side chain
time.sleep(1)

driver.find_element_by_xpath('//*[@id="id_project_id"]').send_keys(123)#input project id

driver.find_element_by_xpath('//*[@id="sidechain_form"]/div/div/input[1]').click()#click save
time.sleep(1)

driver.find_element_by_xpath('//*[@id="container"]/div[2]/a[1]').click()#back to home
time.sleep(1)

driver.find_element_by_xpath('//*[@id="content-main"]/div[2]/table/tbody/tr[2]/td[1]/a').click()#add side chain block
time.sleep(1)

driver.find_element_by_xpath('//*[@id="id_block_size"]').send_keys(32)
driver.find_element_by_xpath('//*[@id="id_block_version"]').send_keys('2.0')
driver.find_element_by_xpath('//*[@id="id_project_id"]').send_keys(1)
driver.find_element_by_xpath('//*[@id="id_contributor_id"]').send_keys(2)
Select(driver.find_element_by_xpath('//*[@id="id_side_chain"]')).select_by_index(1)
driver.find_element_by_xpath('//*[@id="id_log_file"]').send_keys('This is log')
driver.find_element_by_xpath('//*[@id="sidechainblock_form"]/div/div/input[1]').click()#click save


driver2 = webdriver.Chrome()
driver2.get('http://127.0.0.1:8001')     # "get"
username=driver2.find_element_by_xpath('//*[@id="id_username"]')
password=driver2.find_element_by_xpath('//*[@id="id_password"]')
username.send_keys('bob')
password.send_keys('bob')
submit=driver2.find_element_by_xpath('//*[@id="login-form"]/div[3]/input')
submit.click()
time.sleep(1)
driver2.find_element_by_xpath('//*[@id="content-main"]/div[2]/table/tbody/tr[2]/th/a').click()#check side chain block
time.sleep(2)
driver2.find_element_by_xpath('//*[@id="result_list"]/tbody/tr/th/a').click()#check side chain block
# driver.quit()   # Make sure to exit your Chrome when you leave. Otherwise, chromedriver.exe will be in your RAM