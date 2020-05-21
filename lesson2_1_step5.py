from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    what_is_x = browser.find_element_by_id("treasure")
    what_is = what_is_x.get_attribute("valuex")
    y = calc(int(what_is))
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    check_box = browser.find_element_by_id("robotCheckbox")
    check_box.click()
    radio_b = browser.find_element_by_id("robotsRule")
    radio_b.click()
    submit = browser.find_element_by_class_name("btn")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
    




