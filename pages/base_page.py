from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:

    URL = "https://opensource-demo.orangehrmlive.com/"

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(BasePage.URL)

    def load_page(self, url):
        self.driver.get(url)

    def populate_field_by_id(self, id, value):
        element = self.driver.find_element_by_id(id)
        element.send_keys(value)

    def click_btn(self, id):
        element = self.driver.find_element_by_id(id)
        element.click()

    def click_link(self, link_text):
        for link in self.driver.find_elements_by_link_text(link_text):
            link.click()