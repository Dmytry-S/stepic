from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import math
import time


link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element(By.ID, "book")
WebDriverWait(browser, 15).until(ec.text_to_be_present_in_element((By.ID, "price"), "100"))
button.click()
x = browser.find_element_by_id("input_value")
x_text = int(x.text)
y = calc(int(x_text))
answer = browser.find_element_by_id("answer")
answer.send_keys(y)
sub_button = browser.find_element_by_id("solve")
sub_button.click()
time.sleep(3)
data_answer = browser.switch_to.alert
a_text = data_answer.text
add_text = a_text.split(': ')[-1]
print(add_text)
time.sleep(10)
browser.quit()