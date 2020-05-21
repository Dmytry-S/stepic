from selenium import webdriver
import os
import time


link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)
first_name = browser.find_element_by_css_selector(".form-control:nth-child(2)")
first_name.send_keys("N")
last_name = browser.find_element_by_css_selector(".form-control:nth-child(4)")
last_name.send_keys("L")
email = browser.find_element_by_css_selector(".form-control:nth-child(6)")
email.send_keys("e@m.l")
cur_dir = os.getcwd()
file_dir = os.path.join(cur_dir, 'test.txt')
add_file = browser.find_element_by_id("file")
add_file.send_keys(file_dir)
button = browser.find_element_by_class_name("btn")
button.click()
time.sleep(10)
browser.quit()