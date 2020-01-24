from selenium import webdriver
from time import sleep
import os


class InstaBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.username = os.environ.get('INSTA_USER')
        self.password = os.environ.get('INSTA_PASS')
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(self.username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(self.password)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(2)

InstaBot()