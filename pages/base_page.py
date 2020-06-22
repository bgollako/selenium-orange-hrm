from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def load_page(self, url):
        self.driver.get(url)

    def populate_field(self, locator, value):
        element = self.driver.find_element(*locator)
        element.send_keys(value)

    def get_field(self, locator):
        return self.driver.find_element(*locator)

    def click_btn(self, locator):
        element = self.driver.find_element(*locator)
        element.click()

    def get_page_url(self):
        return self.driver.current_url

    def click_link(self, locator):
        for link in self.driver.find_elements(*locator):
            link.click()