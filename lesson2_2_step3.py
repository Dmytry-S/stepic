from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    num_1 = browser.find_element_by_id("num1")
    num_1_data = num_1.text
    num_2 = browser.find_element_by_id("num2")
    num_2data = num_2.text
    result = str(int(num_1_data) + int(num_2data))
    dropdown_list = Select(browser.find_element_by_id("dropdown"))
    answer = dropdown_list.select_by_value(result)
    submit = browser.find_element_by_class_name("btn")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()

