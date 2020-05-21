from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

browser = webdriver.Chrome()
browser.get(link)
mag_button = browser.find_element_by_class_name("btn")
mag_button.click()
confirm_but = browser.switch_to.alert
confirm_but.accept()
x = browser.find_element_by_id("input_value")
x_text = int(x.text)
y = calc(int(x_text))
answer = browser.find_element_by_id("answer")
answer.send_keys(y)
sub_button = browser.find_element_by_class_name("btn")
sub_button.click()
data_answer = browser.switch_to.alert
a_text = data_answer.text
add_text = a_text.split(': ')[-1]
print(add_text)
time.sleep(10)
browser.quit()



