import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import math

links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    # browser.implicitly_wait(10)
    yield browser
    browser.quit()


@pytest.mark.parametrize('link', links)
def test_pages_links(browser, link):
    answer = math.log(int(time.time()))
    browser.implicitly_wait(50)
    browser.get(link)
    field = browser.find_element_by_id("ember69")
    field.send_keys(str(answer))
    browser.find_element_by_class_name("submit-submission").click()
    # hint = WebDriverWait(browser, 15).until(ec.text_to_be_present_in_element((By.CLASS_NAME("smart-hints__hint")), "Correct!"))
    hint = browser.find_element_by_class_name("smart-hints__hint")
    hint_text = hint.text
    assert hint_text == "Correct!", "Text is incorrect!"

# The owls are not what they seem! OvO