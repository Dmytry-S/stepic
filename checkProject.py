from selenium import webdriver
import time


class Chrometest():
    def testChrome(self):
        # global driver #Browser stays open after test
        driver = webdriver.Chrome(executable_path="browserDrivers/chromedriver")
        driver.get("http://www.google.com")
        driver.maximize_window()
        time.sleep(5)


chrometest = Chrometest()
chrometest.testChrome()
