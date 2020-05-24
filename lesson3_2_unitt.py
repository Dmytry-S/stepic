from selenium import webdriver
import unittest
import time

link_1 = "http://suninjuly.github.io/registration1.html"
link_2 = "http://suninjuly.github.io/registration2.html"


class TestPages(unittest.TestCase):
    def test_page_1(self):
        browser = webdriver.Chrome()
        browser.get(link_1)

        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element_by_xpath("//div[@class='first_block']  //input[contains(@class,'first')]")
        first_name.send_keys("D")
        last_name = browser.find_element_by_xpath("//div[@class='first_block']  //input[contains(@class,'second')]")
        last_name.send_keys("S")
        email_name = browser.find_element_by_class_name("form-control.third")
        email_name.send_keys("e@m.com")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(2)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        # assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Text is incorrect")
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_page_2(self):
        browser = webdriver.Chrome()
        browser.get(link_2)

        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element_by_xpath("//div[@class='first_block']  //input[contains(@class,'first')]")
        first_name.send_keys("D")
        last_name = browser.find_element_by_xpath("//div[@class='first_block']  //input[contains(@class,'second')]")
        last_name.send_keys("S")
        email_name = browser.find_element_by_class_name("form-control.third")
        email_name.send_keys("e@m.com")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(2)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        # assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Text is incorrect")
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()