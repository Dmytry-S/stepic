from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/execute_script.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    data_x = browser.find_element_by_id("input_value")
    x_x = int(data_x.text)
    y = calc(x_x)
    answer_field = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer_field)
    answer_field.send_keys(y)
    check_box = browser.find_element_by_id("robotCheckbox")
    check_box.click()
    radio_b = browser.find_element_by_id("robotsRule")
    radio_b.click()
    submit = browser.find_element_by_class_name("btn")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()


